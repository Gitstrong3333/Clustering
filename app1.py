import streamlit as st
import joblib
import numpy as np

# Load model and scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("Credit Card Churn Prediction")

features = [
    "Customer_Age",
    "Gender",  # 0=F, 1=M
    "Income_Category",  # 0=High,1=Low,2=Medium
    "Credit_Limit",
    "Avg_Utilization_Ratio",
    "Total_Trans_Ct",
    "Months_on_book"
]

# User inputs
age = st.number_input("Customer Age", 18, 100, 30)
gender = st.selectbox("Gender", ["Female", "Male"])
income_map = {"High": 0, "Low": 1, "Medium": 2}
income = st.selectbox("Income Category", list(income_map.keys()))
credit_limit = st.number_input("Credit Limit", 0.0, 20000.0, 5000.0)
util_ratio = st.number_input("Avg Utilization Ratio", 0.0, 1.0, 0.5)
total_trans = st.number_input("Total Transaction Count", 0, 500, 50)
months = st.number_input("Months on Book", 0, 100, 12)

user_input = np.array([
    age,
    1 if gender == "Male" else 0,
    income_map[income],
    credit_limit,
    util_ratio,
    total_trans,
    months
]).reshape(1, -1)

if st.button("Predict Churn"):
    scaled_input = scaler.transform(user_input)
    pred = model.predict(scaled_input)[0]
    if pred == 1:
        st.error("Prediction: Customer WILL churn.")
    else:
        st.success("Prediction: Customer will NOT churn.")