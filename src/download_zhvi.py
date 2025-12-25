import os
import requests

ZHVI_URL = (
    "https://files.zillowstatic.com/research/public_csvs/zhvi/"
    "City_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv"
)

OUTPUT_DIR = "data/external"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "zillow_zhvi_city.csv")


def download_zhvi():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("Downloading Zillow ZHVI City dataset...")
    response = requests.get(ZHVI_URL, stream=True)
    response.raise_for_status()

    with open(OUTPUT_FILE, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    print(f"Saved file to: {OUTPUT_FILE}")


if __name__ == "__main__":
    download_zhvi()
