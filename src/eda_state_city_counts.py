import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def main():
    df = pd.read_csv("data/processed/us_top_cities_population_clean.csv")

    # Count cities per state
    state_counts = (
        df.groupby("state")
          .size()
          .sort_values(ascending=False)
          .head(15)
    )

    output_dir = Path("outputs/figures")
    output_dir.mkdir(parents=True, exist_ok=True)

    plt.figure()
    state_counts.plot(kind="bar")
    plt.title("Top 15 States by Number of Cities (in Top 346 Cities Dataset)")
    plt.xlabel("State")
    plt.ylabel("Number of Cities")
    plt.tight_layout()
    plt.savefig(output_dir / "top15_states_city_counts.png")
    plt.close()

    print("Saved:", output_dir / "top15_states_city_counts.png")
    print(state_counts)


if __name__ == "__main__":
    main()
