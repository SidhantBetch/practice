# Gender -> 1 Female, 0 Male
# Churn -> 1 Yes, 0 No
# Scaler is exported as scaler.pkl
# Model is exported as model.pkl
# Order of the x -> ['Age', 'Gender', 'Tenure', 'MonthlyCharges']

from pathlib import Path

import streamlit as st
import joblib
import numpy as np
import pandas as pd

BASE_DIR = Path(__file__).parent
scaler = joblib.load(BASE_DIR / "scaler.pkl")
model = joblib.load(BASE_DIR / "model.pkl")

st.title("Churn Prediction App")

st.divider()

st.write("Please enter the values and hit the predict button for getting a prediction.")

st.divider()

age = st.number_input("Enter age", min_value = 10, max_value = 100, value = 10)

tenure = st.number_input("Enter Tenure", min_value = 0, max_value = 130, value = 10)

monthlycharges = st.number_input("Enter Monthly Charges", min_value = 30, max_value = 150)

gender = st.selectbox("Enter the Gender", ["Male", "Female"])

st.divider()

predictbutton = st.button("Predict")

st.divider()

if predictbutton:
    gender_selected = 1 if gender == "Female" else 0

    x = pd.DataFrame(
        [[age, gender_selected, tenure, monthlycharges]],
        columns=["Age", "Gender", "Tenure", "MonthlyCharges"],
    )

    x_array = scaler.transform(x)

    prediction = model.predict(x_array)[0]

    predicted = "Yes" if prediction == 1 else "No"

    st.balloons()

    st.write(f"Predicted: {predicted}")

else:
    st.write("Please enter the values and use predict button")
