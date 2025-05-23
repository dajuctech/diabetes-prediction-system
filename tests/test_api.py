import pytest
from fastapi.testclient import TestClient
from src.api.app import app

client = TestClient(app)

def test_predict_endpoint_valid():
    payload = {
        "Pregnancies": 2,
        "Glucose": 120,
        "BloodPressure": 70,
        "SkinThickness": 20,
        "Insulin": 85,
        "BMI": 28.5,
        "DiabetesPedigreeFunction": 0.627,
        "Age": 45
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "prediction" in response.json()

def test_predict_endpoint_invalid():
    payload = {"Glucose": 100}  # Missing fields
    response = client.post("/predict", json=payload)
    assert response.status_code == 422  # Unprocessable Entity
