import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def main():
    df = pd.read_csv("data/processed/us_top_cities_population_clean.csv")

    # Define city size categories
    bins = [0, 100_000, 500_000, 1_000_000, float("inf")]
    labels = ["Small (<100k)", "Medium (100k–500k)", "Large (500k–1M)", "Mega (>1M)"]

    df["city_size_category"] = pd.cut(
        df["population_2024_estimate"],
        bins=bins,
        labels=labels,
        right=False
    )

    # Count cities per category
    category_counts = (
        df["city_size_category"]
        .value_counts()
        .sort_index()
    )

    output_dir = Path("outputs/figures")
    output_dir.mkdir(parents=True, exist_ok=True)

    plt.figure()
    category_counts.plot(kind="bar")
    plt.title("Distribution of U.S. Cities by Population Size (2024)")
    plt.xlabel("City Size Category")
    plt.ylabel("Number of Cities")
    plt.tight_layout()
    plt.savefig(output_dir / "city_size_distribution.png")
    plt.close()

    print("Saved:", output_dir / "city_size_distribution.png")
    print(category_counts)


if __name__ == "__main__":
    main()
