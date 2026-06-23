import streamlit as st
import pandas as pd
import joblib
from utils.pdf_report import generate_report
import base64

def add_bg():

    with open(
        "assets/greek_texture.jpg",
        "rb"
    ) as image_file:

        encoded = base64.b64encode(
            image_file.read()
        ).decode()

    st.markdown(
        f"""
        <style>

        .stApp {{

            background:
            linear-gradient(
                rgba(248,241,228,0.82),
                rgba(248,241,228,0.82)
            ),
            url("data:image/jpg;base64,{encoded}");

            background-size: cover;
            background-position: center;
            background-attachment: fixed;

        }}

        </style>
        """,
        unsafe_allow_html=True
    )

add_bg()

def load_css():

    with open(
        "assets/style.css"
    ) as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()
st.markdown(
"""
<style>

.block-container {

border: 4px solid #c9a15d;

border-radius: 20px;

margin-top: 15px;

background: rgba(
255,
255,
255,
0.55
);

backdrop-filter: blur(10px);
}

</style>
""",
unsafe_allow_html=True
)

st.set_page_config(
    page_title="THEMIS",
    page_icon="assets/themis_logo.png",
    layout="wide"
)

model = joblib.load("models/themis_model.pkl")
feature_columns = joblib.load("models/feature_columns.pkl")
encoders = joblib.load("models/encoders.pkl")
target_encoder = joblib.load("models/target_encoder.pkl")

col1, col2 = st.columns([1,5])

with col1:

    st.image(
        "assets/themis_logo.png",
        width=130
    )

with col2:

    st.markdown(
        """
        <h1 style="
        margin-bottom:0px;
        color:#102a4d;">
        THEMIS
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <h3 style="
        color:#7c5b20;">
        AI-Powered Credit Risk Intelligence Platform
        </h3>
        """,
        unsafe_allow_html=True
    )

st.divider()

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "🏛 Applications",
    "1000"
)

c2.metric(
    "🎯 Accuracy",
    "75.5%"
)

c3.metric(
    "🏆 Features",
    "22"
)

c4.metric(
    "🌳 Model",
    "Random Forest"
)

st.divider()

st.markdown(
"""
<h1 style='
text-align:center;
color:#102a4d;
font-family:Georgia;
'>
⚜ Applicant Information ⚜
</h1>
""",
unsafe_allow_html=True
)

col1, col2 = st.columns(2)

# LEFT SIDE

age = col1.number_input(
    "Age",
    18,
    100,
    35
)

credit_amount = col1.number_input(
    "Credit Amount",
    100,
    50000,
    5000
)

month_duration = col1.number_input(
    "Loan Duration (Months)",
    1,
    120,
    24
)

payment_ratio = col1.selectbox(
    "Payment To Income Ratio",
    [1,2,3,4]
)

status_account = col1.selectbox(
    "Account Status",
    [
        "< 0 DM",
        "0 to < 200 DM",
        ">= 200 DM",
        "no checking account"
    ]
)

credit_history = col1.selectbox(
    "Credit History",
    [
        "critical account/ other credits existing (not at this bank)",
        "existing credits paid back duly till now",
        "delay in paying off in the past",
        "no credits taken/ all credits paid back duly",
        "all credits at this bank paid back duly"
    ]
)

purpose = col1.selectbox(
    "Purpose",
    [
        "car (new)",
        "car (used)",
        "radio/television",
        "education",
        "business",
        "furniture/equipment",
        "repairs",
        "others",
        "retraining",
        "domestic appliances"
    ]
)

status_and_sex = col1.selectbox(
    "Applicant Status",
    [
        "male : single",
        "female : divorced/separated/married",
        "male : divorced/separated",
        "male : married/widowed"
    ]
)

secondary_obligor = col1.selectbox(
    "Secondary Obligor",
    [
        "none",
        "guarantor",
        "co-applicant"
    ]
)

collateral = col1.selectbox(
    "Collateral",
    [
        "none",
        "car",
        "savings agreement/life insurance",
        "real estate"
    ]
)

other_installment_plans = col1.selectbox(
    "Other Installment Plans",
    [
        "none",
        "bank",
        "stores"
    ]
)

telephone = col1.selectbox(
    "Telephone",
    [
        "yes, registered under the customers name",
        "none"
    ]
)

is_foreign_worker = col1.selectbox(
    "Foreign Worker",
    [
        "yes",
        "no"
    ]
)

# RIGHT SIDE

housing = col2.selectbox(
    "Housing",
    ["own", "rent", "for free"]
)

employment = col2.selectbox(
    "Employment Duration",
    [
        "< 1 year",
        "1 to < 4 years",
        "4 to < 7 years",
        ">= 7 years",
        "unemployed"
    ]
)

savings = col2.selectbox(
    "Savings Status",
    [
        "< 100 DM",
        "100 to < 500 DM",
        "500 to < 1000 DM",
        ">= 1000 DM",
        "unknown/ no savings account"
    ]
)

job = col2.selectbox(
    "Job Type",
    [
        "unskilled - resident",
        "skilled employee/ official",
        "management/ self-employed/highly qualified employee",
        "unemployed/ unskilled - non-resident"
    ]
)

n_credits = col2.number_input(
    "Number of Existing Credits",
    1,
    4,
    1
)

residence_since = col2.number_input(
    "Years at Residence",
    1,
    4,
    2
)

n_guarantors = col2.number_input(
    "Number of Guarantors",
    1,
    2,
    1
)

if st.button("Evaluate Applicant"):

    input_data = {
        "status_account": status_account,
        "month_duration": month_duration,
        "credit_history": credit_history,
        "purpose": purpose,
        "credit_amount": credit_amount,
        "status_savings": savings,
        "years_employment": employment,
        "payment_to_income_ratio": payment_ratio,
        "status_and_sex": status_and_sex,
        "secondary_obligor": secondary_obligor,
        "residence_since": residence_since,
        "collateral": collateral,
        "age": age,
        "other_installment_plans": other_installment_plans,
        "housing": housing,
        "n_credits": n_credits,
        "job": job,
        "n_guarantors": n_guarantors,
        "telephone": telephone,
        "is_foreign_worker": is_foreign_worker,
        "credit_per_month": credit_amount / month_duration,
        "high_credit_flag": int(credit_amount > 5000)
    }

    input_df = pd.DataFrame([input_data])

    categorical_cols = [
        "status_account",
        "credit_history",
        "purpose",
        "status_savings",
        "years_employment",
        "status_and_sex",
        "secondary_obligor",
        "collateral",
        "other_installment_plans",
        "housing",
        "job",
        "telephone",
        "is_foreign_worker"
    ]

    try:

        for col in categorical_cols:
            input_df[col] = encoders[col].transform(
                input_df[col]
            )

        input_df = input_df[feature_columns]

        prediction = model.predict(
            input_df
        )[0]

        probability = model.predict_proba(
            input_df
        )[0][1]

        credit_score = int(
            300 + probability * 550
        )

        prediction_text = (
            "Good Credit"
            if prediction == 1
            else "Bad Credit"
        )

        st.divider()

        st.header("Risk Assessment")

        a, b, c = st.columns(3)

        a.metric(
            "Credit Score",
            credit_score
        )

        b.metric(
            "Approval Probability",
            f"{probability:.2%}"
        )

        c.metric(
            "Prediction",
            prediction_text
        )

        if probability >= 0.80:

            st.markdown(
"""
<div style="
background:#0f5132;
padding:20px;
border-radius:15px;
font-size:24px;
font-weight:bold;
color:white;
text-align:center;
">
🟢 LOW RISK – APPROVE
</div>
""",
unsafe_allow_html=True
)

        elif probability >= 0.60:

            st.markdown(
"""
<div style="
background:#856404;
padding:20px;
border-radius:15px;
font-size:24px;
font-weight:bold;
color:white;
text-align:center;
">
🟡 MEDIUM RISK – REVIEW
</div>
""",
unsafe_allow_html=True
)

        else:

            st.markdown(
"""
<div style="
background:#842029;
padding:20px;
border-radius:15px;
font-size:24px;
font-weight:bold;
color:white;
text-align:center;
">
🔴 HIGH RISK – REJECT
</div>
""",
unsafe_allow_html=True
)
        

        report_file = generate_report(
            age,
            credit_amount,
            month_duration,
            probability,
            credit_score,
            prediction_text
        )

        with open(report_file, "rb") as pdf_file:

            st.download_button(
                label="📄 Download Credit Risk Report",
                data=pdf_file,
                file_name=report_file,
                mime="application/pdf"
            )

    except Exception as e:

        st.error(
            f"Prediction Error: {e}"
        )