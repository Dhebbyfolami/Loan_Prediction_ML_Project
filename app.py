import streamlit as st
import pandas as pd
import pickle

# Load Model
model = pickle.load(open("models/trained_model.pkl", "rb"))

st.title("🏦 Loan Approval Prediction App")
st.write("Upload applicant details to predict loan approval.")

# User Inputs
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
employment = st.selectbox("Self Employed", ["Yes", "No"])
app_income = st.number_input("Applicant Income", min_value=0)
coapp_income = st.number_input("Coapplicant Income", min_value=0)
loan_amt = st.number_input("Loan Amount", min_value=0)
loan_term = st.number_input("Loan Term")
credit_hist = st.selectbox("Credit History", [1.0, 0.0])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# Convert to DataFrame
input_data = pd.DataFrame({
    "Gender": [gender],
    "Married": [married],
    "Dependents": [dependents],
    "Education": [education],
    "Self_Employed": [employment],
    "ApplicantIncome": [app_income],
    "CoapplicantIncome": [coapp_income],
    "LoanAmount": [loan_amt],
    "Loan_Amount_Term": [loan_term],
    "Credit_History": [credit_hist],
    "Property_Area": [property_area],
})

# Predict Button
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.success("Loan Approved ✔")
    else:
        st.error("Loan Not Approved ❌")

  streamlit run app.py
