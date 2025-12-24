import pandas as pd
from pathlib import Path


def main():
    df = pd.read_csv("data/processed/us_city_affordability_metrics.csv")

    # Median price within each city-size category
    segment_median = (
        df.groupby("city_size_category")["median_home_value"]
          .transform("median")
    )

    # Affordability flags
    df["affordability_flag"] = "Average for size"
    df.loc[df["median_home_value"] < segment_median * 0.85, "affordability_flag"] = "Affordable for size"
    df.loc[df["median_home_value"] > segment_median * 1.15, "affordability_flag"] = "Expensive for size"

    # Save updated dataset
    out_path = Path("data/processed/us_city_affordability_flagged.csv")
    df.to_csv(out_path, index=False)

    print("Saved:", out_path)
    print(df["affordability_flag"].value_counts())
    print("\nPreview (Affordable for size):")
    print(
        df[df["affordability_flag"] == "Affordable for size"]
        [["city", "state", "city_size_category", "median_home_value"]]
        .head(10)
    )


if __name__ == "__main__":
    main()
