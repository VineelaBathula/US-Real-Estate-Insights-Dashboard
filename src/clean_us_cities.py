import pandas as pd
from datetime import date


def main():
    # Load raw data
    in_path = "data/raw/us_top_cities_population.csv"
    df = pd.read_csv(in_path)

    print("Initial rows:", len(df))
    print(df.head())

    # -----------------------
    # Clean city names
    # -----------------------
    # Remove Wikipedia footnotes like [h], [i], [c]
    df["city"] = (
        df["city"]
        .astype(str)
        .str.replace(r"\[.*?\]", "", regex=True)
        .str.strip()
    )

    # -----------------------
    # Clean state codes
    # -----------------------
    df["state"] = df["state"].astype(str).str.strip().str.upper()

    # -----------------------
    # Rename population column to include year
    # -----------------------
    df = df.rename(columns={"population_estimate": "population_2024_estimate"})
    df["population_2024_estimate"] = pd.to_numeric(
        df["population_2024_estimate"], errors="coerce"
    )

    # -----------------------
    # Add metadata (governance)
    # -----------------------
    df["population_year"] = 2024
    df["scraped_date"] = date.today().isoformat()
    df["data_source"] = "Wikipedia – List of United States cities by population"

    # -----------------------
    # Remove bad rows & duplicates
    # -----------------------
    before = len(df)
    df = df.dropna(subset=["population_2024_estimate"])
    df = df.drop_duplicates(subset=["city", "state"])
    after = len(df)

    print(f"Dropped {before - after} rows")

    # -----------------------
    # Save processed dataset
    # -----------------------
    out_path = "data/processed/us_top_cities_population_clean.csv"
    df.to_csv(out_path, index=False)

    print("Saved cleaned file to:", out_path)
    print("Final rows:", len(df))
    print(df.head())


if __name__ == "__main__":
    main()
