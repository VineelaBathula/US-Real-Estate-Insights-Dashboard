import pandas as pd
from pathlib import Path


def main():
    df = pd.read_csv("data/processed/us_city_affordability_metrics.csv")

    out_dir = Path("outputs/tables")
    out_dir.mkdir(parents=True, exist_ok=True)

    # Top 20 cheapest cities overall
    cheapest_overall = df.sort_values("median_home_value", ascending=True).head(20)
    cheapest_overall.to_csv(out_dir / "top20_cheapest_cities_overall.csv", index=False)

    # Top 20 cheapest cities within each city-size category (fair comparison)
    cheapest_by_segment = (
        df.sort_values(["city_size_category", "median_home_value"], ascending=[True, True])
          .groupby("city_size_category", as_index=False)
          .head(20)
    )
    cheapest_by_segment.to_csv(out_dir / "top20_cheapest_cities_by_segment.csv", index=False)

    # Top 20 most expensive cities overall
    expensive_overall = df.sort_values("median_home_value", ascending=False).head(20)
    expensive_overall.to_csv(out_dir / "top20_most_expensive_cities_overall.csv", index=False)

    print("Saved tables to:", out_dir)
    print("Files created:")
    print(" - top20_cheapest_cities_overall.csv")
    print(" - top20_cheapest_cities_by_segment.csv")
    print(" - top20_most_expensive_cities_overall.csv")

    print("\nPreview (cheapest overall):")
    print(cheapest_overall[["city", "state", "city_size_category", "median_home_value"]].head(10))


if __name__ == "__main__":
    main()
