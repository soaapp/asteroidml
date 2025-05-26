import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import joblib
import os

INPUT_CSV = "data/neo_preprocessed.csv"
MODEL_PATH = "models/approach_predictor.pkl"

def main():
    print("🔧 Loading data...")
    df = pd.read_csv(INPUT_CSV)

    print("Preparing features...")
    features = df.drop(columns=["name", "close_approach_km"])
    target = df["close_approach_km"]

    print("Splitting train/test...")
    X_train, X_test, y_train, y_test = train_test_split(
        features, target, test_size=0.2, random_state=42
    )

    print("Training RandomForestRegressor...")
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    print("Evaluating model...")
    y_pred = model.predict(X_test)
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    r2 = r2_score(y_test, y_pred)

    print(f"\nTraining complete!")
    print(f"RMSE: {rmse:.2f} km")
    print(f"R² Score: {r2:.4f}")

    print("Saving model...")
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print(f"Model saved to: {MODEL_PATH}")


if __name__ == "__main__":
    main()
