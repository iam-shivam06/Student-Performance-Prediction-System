import os
import joblib
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Create project folders if they do not exist
os.makedirs("dataset", exist_ok=True)
os.makedirs("model", exist_ok=True)

# Generate a reproducible synthetic dataset for this educational demo
np.random.seed(42)
n = 1000

study_hours = np.random.uniform(0, 10, n)
attendance = np.random.uniform(40, 100, n)
previous_score = np.random.uniform(20, 100, n)
assignment_score = np.random.uniform(20, 100, n)
sleep_hours = np.random.uniform(4, 10, n)
noise = np.random.normal(0, 5, n)

final_score = (
    2.5 * study_hours
    + 0.20 * attendance
    + 0.30 * previous_score
    + 0.20 * assignment_score
    + 1.0 * sleep_hours
    + noise
)
final_score = np.clip(final_score, 0, 100)

df = pd.DataFrame({
    "study_hours": study_hours,
    "attendance": attendance,
    "previous_score": previous_score,
    "assignment_score": assignment_score,
    "sleep_hours": sleep_hours,
    "final_score": final_score
})

dataset_path = "dataset/student_data.csv"
df.to_csv(dataset_path, index=False)

X = df.drop(columns=["final_score"])
y = df["final_score"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

joblib.dump(model, "model/student_model.pkl")

print("\nModel training completed successfully!")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"R2 Score: {r2:.3f}")
print(f"Dataset saved to: {dataset_path}")
print("Trained model saved to: model/student_model.pkl")
