import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

MODEL_PATH = Path(__file__).parent / "fraud_detection_pipeline.pkl"

st.title("Fraud Detection App")

try:
    model = joblib.load(MODEL_PATH)
except FileNotFoundError:
    st.error(f"Model file not found at {MODEL_PATH}")
    st.stop()

st.markdown("Please enter the transaction details and use the predict button")

st.divider()

transaction_type_map = {
    "Payment": "PAYMENT",
    "Transfer": "TRANSFER",
    "Cash In": "CASH_IN",
    "Cash Out": "CASH_OUT",
    "Debit": "DEBIT",
}
selected_transaction_type = st.selectbox("Transaction Type", list(transaction_type_map.keys()))
transaction_type = transaction_type_map[selected_transaction_type]
amount = st.number_input("Amount", min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, value=10000.0)
newbalanceOrg = st.number_input("New Balance (Sender)", min_value=0.0, value=9000.0)
oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=0.0)
newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, value=0.0)

if st.button("Predict"):
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        # map to the exact feature names expected by the trained pipeline
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrg,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest,
    }])
    try:
        prediction = model.predict(input_data)[0]
        st.subheader(f"prediction: '{int(prediction)}'")

        if int(prediction) == 1:
            st.error("This transaction is predicted to be fraudulent.")
        else:
            st.success("This transaction is predicted to be legitimate.")
    except ValueError as e:
        st.error(f"Prediction error: {e}")
        st.write("Input data sent to the model:")
        st.write(input_data)