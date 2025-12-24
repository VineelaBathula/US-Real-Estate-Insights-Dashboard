import pandas as pd
import numpy as np
from pathlib import Path


def main():
    in_path = "data/processed/us_city_population_with_prices.csv"
    df = pd.read_csv(in_path)

    # Keep only rows where we have Zillow home values
    df = df.dropna(subset=["median_home_value"]).copy()

    # Ensure numeric
    df["median_home_value"] = pd.to_numeric(df["median_home_value"], errors="coerce")
    df["population_2024_estimate"] = pd.to_numeric(df["population_2024_estimate"], errors="coerce")
    df = df.dropna(subset=["median_home_value", "population_2024_estimate"])

    # -----------------------
    # City size segmentation
    # -----------------------
    bins = [0, 100_000, 500_000, 1_000_000, float("inf")]
    labels = ["Small (<100k)", "Medium (100k–500k)", "Large (500k–1M)", "Mega (>1M)"]
    df["city_size_category"] = pd.cut(
        df["population_2024_estimate"],
        bins=bins,
        labels=labels,
        right=False
    )

    # -----------------------
    # Affordability proxies
    # -----------------------
    # 1) Price per capita (not a real affordability index, but a consistent proxy)
    df["home_value_per_capita"] = df["median_home_value"] / df["population_2024_estimate"]

    # 2) Log transforms for stable comparisons
    df["log_home_value"] = np.log10(df["median_home_value"])
    df["log_population"] = np.log10(df["population_2024_estimate"])

    # -----------------------
    # Within-segment ranks (more fair comparisons)
    # -----------------------
    df["rank_cheapest_in_segment"] = df.groupby("city_size_category")["median_home_value"].rank(method="min", ascending=True)
    df["rank_most_expensive_in_segment"] = df.groupby("city_size_category")["median_home_value"].rank(method="min", ascending=False)

    # -----------------------
    # Simple "value" flag within city-size segment
    # (cheaper than segment median)
    # -----------------------
    segment_median_price = df.groupby("city_size_category")["median_home_value"].transform("median")
    df["below_segment_median_price"] = df["median_home_value"] < segment_median_price

    # Save
    out_path = Path("data/processed/us_city_affordability_metrics.csv")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_path, index=False)

    print("Saved:", out_path)
    print("Rows with prices:", len(df))
    print(df[["city", "state", "median_home_value", "population_2024_estimate", "city_size_category"]].head())


if __name__ == "__main__":
    main()
