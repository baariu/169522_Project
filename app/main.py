from fastapi import FastAPI
from pydantic import BaseModel
from app.mymodel import predict

# Initialize FastAPI app
app = FastAPI(title="ML Model API", description="Deploying a Machine Learning Model with FastAPI")

# Define request schema
class InputData(BaseModel):
    features: list  # Example: [value1, value2, value3]

# Root endpoint
@app.get("/")
def home():
    return {"message": "Welcome to the ML Model API!"}

# Prediction endpoint
@app.post("/predict")
def get_prediction(data: InputData):
    prediction = predict(data.features)
    return {"prediction": prediction}
