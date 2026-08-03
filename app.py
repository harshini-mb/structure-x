import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("structurex_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🏗 StructureX - Infrastructure Risk Predictor")

st.header("Enter Structural Parameters")

age = st.number_input("Age of Structure (years)", 1, 150)
crack = st.number_input("Crack Width (mm)", 0.0, 50.0)
vibration = st.number_input("Vibration Level (Hz)", 0.0, 100.0)
load = st.number_input("Load Stress (%)", 0.0, 150.0)
weather = st.slider("Weather Impact (1-10)", 1, 10)
maintenance = st.slider("Maintenance Score (1-10)", 1, 10)

if st.button("Predict Risk"):
    input_data = np.array([[age, crack, vibration, load, weather, maintenance]])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.write(f"Risk Probability: {probability * 100:.2f}%")

    if prediction == 1:
        st.error("🔴 HIGH RISK of Structural Failure")
    else:
        st.success("🟢 LOW RISK - Structure is Stable")