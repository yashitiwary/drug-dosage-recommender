# train_model.py
import pickle
from sklearn.linear_model import LinearRegression
import numpy as np

# Dummy training data (age, weight, condition) → dosage
X = np.array([
    [25, 60, 1],
    [40, 70, 2],
    [30, 80, 3],
    [50, 65, 1],
    [45, 75, 2],
    [35, 85, 3],
    [60, 90, 4],
    [28, 55, 5],
])
y = np.array([200, 250, 300, 220, 270, 320, 400, 180])  # Dosages in mg

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model to app/model.pkl
with open("app/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved to app/model.pkl")
