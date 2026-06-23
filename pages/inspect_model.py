import streamlit as st
import joblib

with open("assets/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.title("🔍 THEMIS Model Inspector")

feature_columns = joblib.load(
    "models/feature_columns.pkl"
)

encoders = joblib.load(
    "models/encoders.pkl"
)

model = joblib.load(
    "models/themis_model.pkl"
)

st.subheader("Model Information")

st.write(
    f"Model Type: {type(model).__name__}"
)

st.write(
    f"Number of Features: {len(feature_columns)}"
)

st.subheader("Feature Columns")

st.dataframe(feature_columns)

st.subheader("Available Encoders")

st.dataframe(
    list(encoders.keys())
)

st.markdown("""
<div style="
background:rgba(255,255,255,0.8);
padding:20px;
border-radius:15px;
border:2px solid #c9a15d;
">

<h3>🏛 Model Governance</h3>

THEMIS uses a Random Forest architecture trained on
German Credit Risk data.

The system evaluates 22 risk variables including:

• Credit History

• Savings Status

• Employment Duration

• Account Status

• Housing

• Applicant Demographics

These variables are transformed using categorical
encoders before model inference.

</div>
""", unsafe_allow_html=True)
