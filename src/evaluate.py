# src/evaluate.py

import pandas as pd
import matplotlib.pyplot as plt
import joblib
from sklearn.metrics import mean_squared_error, r2_score

MODEL_PATH = "models/approach_predictor.pkl"
DATA_PATH = "data/neo_preprocessed.csv"

def main():
    print("Loading model and data...")
    model = joblib.load(MODEL_PATH)
    df = pd.read_csv(DATA_PATH)

    X = df.drop(columns=["name", "close_approach_km"])
    y = df["close_approach_km"]
    y_pred = model.predict(X)

    # Print metrics
    rmse = mean_squared_error(y, y_pred, squared=False)
    r2 = r2_score(y, y_pred)
    print(f"\n Evaluation Results")
    print(f"RMSE: {rmse:.2f} km")
    print(f"R² Score: {r2:.4f}")

    # Actual vs. Predicted Scatter Plot
    plt.figure(figsize=(8, 6))
    plt.scatter(y, y_pred, alpha=0.6)
    plt.xlabel("Actual Close Approach (km)")
    plt.ylabel("Predicted Close Approach (km)")
    plt.title("Actual vs Predicted Close Approaches")
    plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')  # 45° line
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("models/predicted_vs_actual.png")
    print("Saved: models/predicted_vs_actual.png")

    # Feature Importance
    importances = model.feature_importances_
    features = X.columns
    importance_df = pd.DataFrame({
        "feature": features,
        "importance": importances
    }).sort_values("importance", ascending=True)

    plt.figure(figsize=(8, 6))
    plt.barh(importance_df["feature"], importance_df["importance"])
    plt.xlabel("Importance")
    plt.title("Feature Importance")
    plt.tight_layout()
    plt.savefig("models/feature_importance.png")
    print("Saved: models/feature_importance.png")

if __name__ == "__main__":
    main()
