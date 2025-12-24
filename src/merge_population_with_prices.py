import pandas as pd
from pathlib import Path


def main():
    # Load population dataset
    pop_df = pd.read_csv(
        "data/processed/us_top_cities_population_clean.csv"
    )

    # Load Zillow ZHVI city dataset
    zillow = pd.read_csv(
        "data/external/zillow_zhvi_city.csv"
    )

    # ---- Understand Zillow structure ----
    # Common columns include:
    # RegionName, State, StateName, Metro, CountyName, SizeRank, 2000-01-31, ..., latest date

    # Identify date columns (YYYY-MM-DD)
    date_cols = [
        c for c in zillow.columns if c[:4].isdigit()
    ]

    latest_date = date_cols[-1]

    # Keep only what we need
    price_df = zillow[
        ["RegionName", "State", latest_date]
    ].rename(
        columns={
            "RegionName": "city",
            "State": "state",
            latest_date: "median_home_value"
        }
    )

    # Standardise text for merge
    for col in ["city", "state"]:
        price_df[col] = price_df[col].str.strip()

    pop_df["city"] = pop_df["city"].str.strip()
    pop_df["state"] = pop_df["state"].str.strip()

    # Merge datasets
    merged = pop_df.merge(
        price_df,
        on=["city", "state"],
        how="left"
    )

    # Add metadata
    merged["price_year_month"] = latest_date
    merged["price_source"] = "Zillow ZHVI (City)"

    # Save output
    output_path = Path(
        "data/processed/us_city_population_with_prices.csv"
    )
    merged.to_csv(output_path, index=False)

    print("Saved merged dataset to:", output_path)
    print("Rows:", len(merged))
    print(merged.head())


if __name__ == "__main__":
    main()
