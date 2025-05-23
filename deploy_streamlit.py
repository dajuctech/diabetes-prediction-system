import streamlit as st
import requests

st.title("🧠 Diabetes Prediction App")

# Input form
form = {
    "Pregnancies": st.number_input("Pregnancies", min_value=0),
    "Glucose": st.number_input("Glucose", min_value=0),
    "BloodPressure": st.number_input("Blood Pressure", min_value=0),
    "SkinThickness": st.number_input("Skin Thickness", min_value=0),
    "Insulin": st.number_input("Insulin", min_value=0),
    "BMI": st.number_input("BMI", min_value=0.0),
    "DiabetesPedigreeFunction": st.number_input("Diabetes Pedigree Function", min_value=0.0),
    "Age": st.number_input("Age", min_value=0),
}

if st.button("Predict"):
    res = requests.post("http://localhost:8000/predict", json=form)
    if res.ok:
        data = res.json()
        prediction = "Positive" if data["prediction"] else "Negative"
        st.success(f"Prediction: {prediction} ({data['probability']:.2%})")
    else:
        st.error("Prediction failed.")
