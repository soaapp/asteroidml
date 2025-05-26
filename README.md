# 🚀 AsteroidML: Predicting Close Approaches of Near-Earth Objects

This project uses machine learning to predict how close an asteroid will come to Earth based on its orbital parameters. The model is trained on real data from NASA's Near-Earth Object Web Service (NeoWs) API.

---

## 📊 Objective

To predict the **minimum close-approach distance (in kilometers)** between an asteroid and Earth using features such as orbital eccentricity, inclination, and semi-major axis.

---

## 📁 Project Structure

asteroidml/
├── data/
│ ├── neo_raw.json # Raw data from NASA API
│ └── neo_preprocessed.csv # Cleaned, tabular dataset for ML
├── models/
│ └── approach_predictor.pkl # Trained Random Forest model
│ └── predicted_vs_actual.png # Actual vs predicted distances plot
│ └── feature_importance.png # Orbital feature importance chart
├── src/
│ ├── fetch_asteroids.py # Downloads asteroid data from NASA
│ ├── preprocess.py # Converts raw JSON to CSV
│ ├── train.py # Trains regression model
│ └── evaluate.py # Evaluates & visualizes model
├── config.py # Loads NASA API key from .env
├── .env # Stores your NASA_API_KEY (not committed)
├── requirements.txt # Python dependencies
└── README.md # You're here!

---

## 🔭 Dataset & Features

**Source:**  
NASA NeoWs API – https://api.nasa.gov/

**Target (what you're predicting):**  
`close_approach_km`: How close the asteroid came to Earth in kilometers

**Input Features:**

| Feature             | Description                                                      |
| ------------------- | ---------------------------------------------------------------- |
| eccentricity        | How stretched the orbit is (0 = circle, closer to 1 = elongated) |
| semi_major_axis     | Avg. distance from the Sun in AU (astronomical units)            |
| inclination         | Angle between orbit and Earth's plane (in degrees)               |
| perihelion_distance | Closest point of the orbit to the Sun                            |
| aphelion_distance   | Farthest point of the orbit from the Sun                         |
| orbital_period      | Time to complete one orbit (in days)                             |
| mean_motion         | Degrees the object moves per day                                 |
| epoch_osculation    | Time reference for orbital elements                              |

---

## ⚙️ How It Works

**1. Fetch Data**
python src/fetch_asteroids.py

- Downloads data from NASA API to `data/neo_raw.json`.

**2. Preprocess Data**
python src/preprocess.py

- Parses JSON and extracts orbital features
- Outputs `neo_preprocessed.csv`

**3. Train Model**
python src/train.py

- Trains a RandomForestRegressor
- Saves model to `models/approach_predictor.pkl`

**4. Evaluate Model**
python src/evaluate.py

- Generates two plots:
  - `predicted_vs_actual.png`
  - `feature_importance.png`

---

## 🧪 Requirements

Install all required Python packages:
pip install -r requirements.txt
**requirements.txt**
pandas
scikit-learn
joblib
matplotlib
python-dotenv

---

## 🔐 Environment Variables

Create a `.env` file in your project root:

```
NASA_API_KEY=your_api_key_here
```

## 🧠 Future Improvements

- Add `predict.py` to try the model on new asteroid inputs
- Use more robust time-series data across multiple approaches
- Try XGBoost, LightGBM, or other regressors
- Package this into a REST API (FastAPI or Flask)

---

## 📜 License

MIT License — open for learning, sharing, and expanding.

---

## 👨‍🚀 Author

Built by **Jay Jahanzad** using real NASA data, classical ML models, and a whole lot of curiosity about space.
