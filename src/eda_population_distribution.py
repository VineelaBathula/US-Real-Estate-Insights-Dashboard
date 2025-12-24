import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def main():
    df = pd.read_csv("data/processed/us_top_cities_population_clean.csv")

    output_dir = Path("outputs/figures")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Normal scale histogram
    plt.figure()
    plt.hist(df["population_2024_estimate"], bins=30)
    plt.title("Distribution of U.S. City Populations (Normal Scale)")
    plt.xlabel("Population")
    plt.ylabel("Number of Cities")
    plt.savefig(output_dir / "population_distribution_normal.png")
    plt.close()

    # Log scale histogram
    plt.figure()
    plt.hist(df["population_2024_estimate"], bins=30)
    plt.xscale("log")
    plt.title("Distribution of U.S. City Populations (Log Scale)")
    plt.xlabel("Population (log scale)")
    plt.ylabel("Number of Cities")
    plt.savefig(output_dir / "population_distribution_log.png")
    plt.close()


if __name__ == "__main__":
    main()
