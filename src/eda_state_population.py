import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def main():
    df = pd.read_csv("data/processed/us_top_cities_population_clean.csv")

    # Aggregate: total population (sum of cities in our dataset) by state
    state_pop = (
        df.groupby("state")["population_2024_estimate"]
          .sum()
          .sort_values(ascending=False)
          .head(15)
    )

    output_dir = Path("outputs/figures")
    output_dir.mkdir(parents=True, exist_ok=True)

    plt.figure()
    state_pop.plot(kind="bar")
    plt.title("Top 15 States by Total Population (from Top 346 Cities)")
    plt.xlabel("State")
    plt.ylabel("Total Population (sum of city populations)")
    plt.tight_layout()
    plt.savefig(output_dir / "top15_states_total_city_population.png")
    plt.close()

    print("Saved:", output_dir / "top15_states_total_city_population.png")
    print(state_pop)


if __name__ == "__main__":
    main()
