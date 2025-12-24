import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def main():
    df = pd.read_csv("data/processed/us_city_affordability_metrics.csv")

    output_dir = Path("outputs/figures")
    output_dir.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(8, 6))

    # Scatter plot
    plt.scatter(
        df["population_2024_estimate"],
        df["median_home_value"],
        alpha=0.6
    )

    # Log scales (critical due to skew)
    plt.xscale("log")
    plt.yscale("log")

    plt.title("City Population vs Median Home Value (Log-Log Scale)")
    plt.xlabel("Population (log scale)")
    plt.ylabel("Median Home Value (log scale)")

    plt.tight_layout()
    plt.savefig(output_dir / "population_vs_home_value_log.png")
    plt.close()

    print("Saved:", output_dir / "population_vs_home_value_log.png")
    print("Rows plotted:", len(df))


if __name__ == "__main__":
    main()
