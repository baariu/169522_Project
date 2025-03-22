import joblib
import numpy as np

# Load the saved model
model = joblib.load("models/my_model.pkl")

def predict(features: list):
    """Make a prediction using the loaded model."""
    features_array = np.array(features).reshape(1, -1)
    prediction = model.predict(features_array)
    return prediction.tolist()

