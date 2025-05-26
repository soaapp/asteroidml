import json
import pandas as pd
import os

INPUT_PATH = "../data/neo_raw.json"
OUTPUT_PATH = "../data/neo_preprocessed.csv"

def load_neo_data():
    with open(INPUT_PATH, "r") as f:
        return json.load(f)

def extract_features(asteroid):
    try:
        orbit = asteroid["orbital_data"]
        approach_data = asteroid.get("close_approach_data", [])
        if not approach_data:
            return None # Skip asteroids if there is no approach data
    
        first_approach = approach_data[0]
        miss_km = first_approach.get("miss_distance", {}).get("kilometers")
        
        return {
            "name": asteroid["name"],
            "eccentricity": float(orbit["eccentricity"]),
            "semi_major_axis": float(orbit["semi_major_axis"]),
            "inclination": float(orbit["inclination"]),
            "perihelion_distance": float(orbit["perihelion_distance"]),
            "aphelion_distance": float(orbit["aphelion_distance"]),
            "orbital_period": float(orbit["orbital_period"]),
            "mean_motion": float(orbit["mean_motion"]),
            "epoch_osculation": float(orbit["epoch_osculation"]),
            "close_approach_km": miss_km,
        }
    except Exception as e:
        print(f"Failed to extract features for asteroid {asteroid['name']}: {e}")
        return None

def main():
    raw_data = load_neo_data()
    rows = [extract_features(a) for a in raw_data]
    rows = [r for r in rows if r is not None]

    df = pd.DataFrame(rows)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"Saved preprocessed data to {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
    