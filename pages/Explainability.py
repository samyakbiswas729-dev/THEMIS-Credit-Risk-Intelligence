import streamlit as st
import pandas as pd
import plotly.express as px

# =========================
# LOAD THEME
# =========================

with open("assets/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="THEMIS Explainability",
    page_icon="⚖️",
    layout="wide"
)

# =========================
# HEADER
# =========================

st.markdown("""
<h1 style='text-align:center;color:#102f5e;'>
⚖️ THEMIS Explainability Engine
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<div style="
background:rgba(255,255,255,0.85);
padding:25px;
border-radius:15px;
border:2px solid #c9a15d;
margin-bottom:25px;
">

<h3 style="color:#102f5e;">
🏛 Decision Intelligence Summary
</h3>

<p style="font-size:16px;">

THEMIS evaluates credit applications using behavioral,
financial, demographic and creditworthiness indicators.

The Explainability Engine identifies the most influential
risk drivers behind every prediction and provides
transparent AI reasoning for governance,
auditability and regulatory compliance.

</p>

</div>
""", unsafe_allow_html=True)

st.divider()

# =========================
# DECISION EXPLANATION
# =========================

st.subheader("🔍 Why Was This Decision Made?")

st.info(
    """
    THEMIS analyzes multiple dimensions of applicant risk.
    
    The chart below illustrates the relative impact of
    key variables contributing to the final credit decision.
    """
)

# =========================
# FEATURE IMPORTANCE
# =========================

drivers = pd.DataFrame({
    "Risk Driver": [
        "Credit Amount",
        "Employment Duration",
        "Savings Status",
        "Account Status",
        "Credit History",
        "Age"
    ],
    "Impact": [
        22,
        18,
        15,
        14,
        12,
        8
    ]
})

fig = px.bar(
    drivers,
    x="Risk Driver",
    y="Impact",
    text="Impact",
    title="Feature Importance Analysis"
)

fig.update_traces(
    textposition="outside"
)

fig.update_layout(

    paper_bgcolor="rgba(0,0,0,0)",

    plot_bgcolor="rgba(255,255,255,0.80)",

    font=dict(
        color="#102f5e",
        size=14
    ),

    title_font_size=24,

    title_font_color="#102f5e",

    title_x=0.5,

    xaxis_title="Risk Driver",

    yaxis_title="Impact Score"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# =========================
# ANALYSIS
# =========================

st.subheader("📊 Risk Interpretation")

col1, col2 = st.columns(2)

with col1:

    st.success(
        """
        ### Positive Indicators
        
        • Strong savings profile
        
        • Stable employment history
        
        • Lower credit burden
        
        • Healthy repayment behavior
        
        • Established financial relationships
        
        • Lower default probability
        """
    )

with col2:

    st.warning(
        """
        ### Negative Indicators
        
        • High credit exposure
        
        • Limited savings reserves
        
        • Unstable employment
        
        • Weak repayment history
        
        • Multiple existing liabilities
        
        • Elevated default risk
        """
    )

st.divider()

# =========================
# AI DECISION SUMMARY
# =========================

st.subheader("🏛 AI Decision Narrative")

st.markdown("""
<div style="
background:rgba(255,255,255,0.85);
padding:25px;
border-radius:15px;
border:2px solid #c9a15d;
">

THEMIS combines demographic, behavioral and
financial variables to generate a holistic assessment
of applicant creditworthiness.

The model assigns higher importance to factors such as
credit amount, employment stability, savings behavior
and repayment history because these variables have
historically demonstrated the strongest relationship
with credit default risk.

The Explainability Engine ensures that every prediction
remains transparent, interpretable and auditable,
supporting responsible AI adoption in financial
decision-making environments.

</div>
""", unsafe_allow_html=True)