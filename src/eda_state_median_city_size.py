import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def main():
    df = pd.read_csv("data/processed/us_top_cities_population_clean.csv")

    # Median city population per state
    state_median = (
        df.groupby("state")["population_2024_estimate"]
          .median()
          .sort_values(ascending=False)
          .head(15)
    )

    output_dir = Path("outputs/figures")
    output_dir.mkdir(parents=True, exist_ok=True)

    plt.figure()
    state_median.plot(kind="bar")
    plt.title("Top 15 States by Median City Population (2024)")
    plt.xlabel("State")
    plt.ylabel("Median City Population")
    plt.tight_layout()
    plt.savefig(output_dir / "top15_states_median_city_population.png")
    plt.close()

    print("Saved:", output_dir / "top15_states_median_city_population.png")
    print(state_median)


if __name__ == "__main__":
    main()
