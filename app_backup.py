import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="THEMIS",
    page_icon="🏛️",
    layout="wide"
)

model = joblib.load("models/themis_model.pkl")
feature_columns = joblib.load("models/feature_columns.pkl")

st.title("🏛️ THEMIS")
st.subheader("AI-Powered Credit Risk Intelligence Platform")

st.divider()

c1, c2, c3, c4 = st.columns(4)

c1.metric("Applications", "1000")
c2.metric("Accuracy", "75.5%")
c3.metric("Features", len(feature_columns))
c4.metric("Model", "Random Forest")

st.divider()

st.header("Applicant Information")

col1, col2 = st.columns(2)

age = col1.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=35
)

credit_amount = col1.number_input(
    "Credit Amount",
    min_value=100,
    value=5000
)

month_duration = col1.number_input(
    "Loan Duration (Months)",
    min_value=1,
    value=24
)

payment_ratio = col1.selectbox(
    "Payment To Income Ratio",
    [1, 2, 3, 4]
)

n_credits = col2.number_input(
    "Number of Existing Credits",
    min_value=1,
    value=1
)

residence_since = col2.number_input(
    "Years at Residence",
    min_value=1,
    value=2
)

n_guarantors = col2.number_input(
    "Number of Guarantors",
    min_value=1,
    value=1
)

if st.button("Evaluate Applicant"):

    input_data = {}

    for feature in feature_columns:
        input_data[feature] = 0

    input_data["age"] = age
    input_data["credit_amount"] = credit_amount
    input_data["month_duration"] = month_duration
    input_data["payment_to_income_ratio"] = payment_ratio
    input_data["n_credits"] = n_credits
    input_data["residence_since"] = residence_since
    input_data["n_guarantors"] = n_guarantors

    input_data["credit_per_month"] = (
        credit_amount / month_duration
    )

    input_data["high_credit_flag"] = int(
        credit_amount > 5000
    )

    input_df = pd.DataFrame([input_data])

    input_df = input_df[feature_columns]

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0][1]

    credit_score = int(probability * 1000)

    st.divider()

    st.header("Risk Assessment")

    a, b, c = st.columns(3)

    a.metric(
        "Credit Score",
        credit_score
    )

    b.metric(
        "Probability of Good Credit",
        f"{probability:.2%}"
    )

    c.metric(
        "Prediction",
        "Good Credit" if prediction == 1 else "Bad Credit"
    )

    if probability >= 0.75:
        st.success("SAFE, 🟢 LOW RISK - APPROVE")

    elif probability >= 0.55:
        st.warning("MONITOR...🟡 MEDIUM RISK - MANUAL REVIEW")

    else:
        st.error("WARNING!!!, 🔴 HIGH RISK - REJECT")