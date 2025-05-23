from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib
import tensorflow as tf
from src.api.schemas import PredictionRequest
from sklearn.preprocessing import StandardScaler
import os

app = FastAPI()

# Load model once when server starts
MODEL_PATH = os.getenv("MODEL_PATH", "models/diabetes_model.h5")
model = tf.keras.models.load_model(MODEL_PATH)

# You may want to use the same scaler used during training
scaler = StandardScaler()

@app.get("/")
def root():
    return {"message": "Welcome to the Diabetes Prediction API!"}

@app.post("/predict")
def predict(data: PredictionRequest):
    features = [[
        data.Pregnancies, data.Glucose, data.BloodPressure,
        data.SkinThickness, data.Insulin, data.BMI,
        data.DiabetesPedigreeFunction, data.Age
    ]]

    # You should load the scaler fitted during training. This is just for structure.
    features_scaled = scaler.fit_transform(features)

    prediction = model.predict(features_scaled)
    result = int(prediction[0][0] > 0.5)

    return {
        "prediction": result,
        "probability": float(prediction[0][0])
    }
