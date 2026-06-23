import streamlit as st
import pandas as pd
import plotly.express as px

with open("assets/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.set_page_config(
    page_title="Model Performance",
    page_icon="📈",
    layout="wide"
)

st.title("📈 THEMIS Model Performance")

st.divider()

# KPI Cards

c1, c2, c3, c4 = st.columns(4)

c1.metric("Accuracy", "75.5%")
c2.metric("Precision", "77%")
c3.metric("Recall", "94%")
c4.metric("F1 Score", "84%")

st.divider()

# Confusion Matrix

st.subheader("Confusion Matrix")

cm = pd.DataFrame(
    [
        [20, 40],
        [8, 132]
    ],
    columns=["Predicted Bad", "Predicted Good"],
    index=["Actual Bad", "Actual Good"]
)

fig = px.imshow(
    cm,
    text_auto=True,
    aspect="auto"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# Feature Importance

st.subheader("Top Risk Factors")

feature_df = pd.DataFrame({
    "Feature": [
        "Credit Amount",
        "Account Status",
        "Employment Duration",
        "Age",
        "Credit History",
        "Savings Status",
        "Housing",
        "Loan Duration",
        "Guarantors",
        "Job Type"
    ],
    "Importance": [
        0.22,
        0.18,
        0.14,
        0.12,
        0.09,
        0.08,
        0.06,
        0.05,
        0.03,
        0.03
    ]
})

fig2 = px.bar(
    feature_df,
    x="Importance",
    y="Feature",
    orientation="h"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.markdown("""
### 🏛 Model Evaluation Summary

THEMIS demonstrates strong predictive performance
with high recall and F1-score.

The model is optimized to identify creditworthy
applicants while minimizing default risk.

Risk intelligence models prioritize recall because
missing a high-risk applicant can result in significant
financial losses.

""")

fig.update_layout(

    paper_bgcolor="rgba(0,0,0,0)",

    plot_bgcolor="rgba(255,255,255,0.8)",

    font=dict(
        color="#102f5e"
    )
)