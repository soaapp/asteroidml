import requests
import json
import os
from config import NASA_API_KEY

BASE_URL = f"https://api.nasa.gov/neo/rest/v1/neo/browse?api_key={NASA_API_KEY}"

def fetch_neo_data(pages=3):
    all_asteroids = []
    url = BASE_URL

    for i in range(pages):
        print(f"Fetching page {i + 1}")
        res = requests.get(url)
        if res.status_code != 200:
            print(f"Failed to fetch page {i + 1}")
            continue
        data = res.json()
        all_asteroids.extend(data.get("near_earth_objects", []))
        url = data["links"].get("next")
        if not url:
            break

    os.makedirs("data", exist_ok=True)
    with open("data/neo_raw.json", "w") as f:
        json.dump(all_asteroids, f, indent=2)

    print(f"Fetched {len(all_asteroids)} asteroids")

if __name__ == "__main__":
    fetch_neo_data(pages=3) # ~60 per page
    

        