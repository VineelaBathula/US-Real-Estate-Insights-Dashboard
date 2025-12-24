import pandas as pd
import requests
from io import StringIO


def normalize_cols(cols):
    out = []
    for c in cols:
        if isinstance(c, tuple):
            c = " ".join([str(x) for x in c if str(x) != "nan"]).strip()
        out.append(str(c).strip().lower())
    return out


def col_contains(cols, needle):
    needle = needle.lower()
    return any(needle in c for c in cols)


def main():
    url = "https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population?action=render"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept-Language": "en-US,en;q=0.9",
    }

    r = requests.get(url, headers=headers, timeout=30)
    r.raise_for_status()

    tables = pd.read_html(StringIO(r.text))

    valid = []
    for i, t in enumerate(tables):
        cols = normalize_cols(t.columns)

        has_city = col_contains(cols, "city")
        has_st = col_contains(cols, "st")  # matches 'st st'
        has_est = col_contains(cols, "estimate")  # matches '2024 estimate 2024 estimate'
        has_2020 = col_contains(cols, "2020 census")  # matches '2020 census 2020 census'
        has_peak = col_contains(cols, "peak")  # excludes the historical table

        if has_city and has_st and has_est and has_2020 and (not has_peak) and len(t) > 100:
            valid.append((i, t.copy(), cols))

    if not valid:
        print("No valid population table found. Debug columns:")
        for i, t in enumerate(tables[:12]):
            print(i, normalize_cols(t.columns))
        raise RuntimeError("Population table not found.")

    best_i, best_df, best_cols = max(valid, key=lambda x: len(x[1]))
    print(f"Selected table index: {best_i} with rows: {len(best_df)}")
    print("Columns:", best_cols)

    best_df.columns = normalize_cols(best_df.columns)

    # Find actual column names (they may be duplicated like 'city city')
    city_col = next(c for c in best_df.columns if "city" in c)
    st_col = next(c for c in best_df.columns if c == "st" or c.endswith("st") or "st" in c)
    est_col = next(c for c in best_df.columns if "estimate" in c)

    out = best_df[[city_col, st_col, est_col]].copy()
    out = out.rename(columns={city_col: "city", st_col: "state", est_col: "population_estimate"})

    out["city"] = out["city"].astype(str).str.strip()
    out["state"] = out["state"].astype(str).str.strip().str.upper()
    out["population_estimate"] = pd.to_numeric(out["population_estimate"], errors="coerce")

    out_path = "data/raw/us_top_cities_population.csv"
    out.to_csv(out_path, index=False)

    print(f"Saved: {out_path}")
    print("Rows:", len(out))
    print(out.head(10))


if __name__ == "__main__":
    main()
