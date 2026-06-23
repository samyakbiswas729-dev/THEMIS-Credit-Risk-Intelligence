import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="THEMIS Portfolio Analytics",
    page_icon="📊",
    layout="wide"
)

# =====================================
# LOAD CSS
# =====================================

with open("assets/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# =====================================
# HEADER
# =====================================

col1, col2 = st.columns([1,5])

with col1:
    st.image(
        "assets/themis_logo.png",
        width=120
    )

with col2:

    st.markdown("""
    <h1 style="
    color:#102f5e;
    font-family:'Times New Roman';
    font-size:54px;
    margin-bottom:0px;
    ">
    📊 THEMIS PORTFOLIO ANALYTICS
    </h1>
    """,
    unsafe_allow_html=True)

    st.markdown("""
    <h3 style="
    color:#c9a15d;
    font-family:'Times New Roman';
    ">
    Portfolio Intelligence Dashboard
    </h3>
    """,
    unsafe_allow_html=True)

st.markdown("""
<div style="
background:rgba(255,255,255,0.75);
padding:20px;
border-radius:15px;
border:2px solid #c9a15d;
margin-top:10px;
margin-bottom:20px;
">

<h3 style="color:#102f5e;">
Executive Overview
</h3>

This module provides a macro-level view of lending exposure,
customer demographics, credit concentration and portfolio
risk characteristics.

The dashboard enables analysts, risk managers and auditors
to identify emerging trends, unusual patterns and potential
risk concentrations across the credit portfolio.

</div>
""",
unsafe_allow_html=True)

st.divider()

# =====================================
# DATA
# =====================================

df = pd.read_csv(
    "data/german_credit_data.csv"
)

df["Risk Band"] = pd.cut(
    df["credit_amount"],
    bins=[0,2500,5000,100000],
    labels=[
        "Low Risk",
        "Medium Risk",
        "High Risk"
    ]
)

# =====================================
# KPI SECTION
# =====================================

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Applications",
    len(df)
)

c2.metric(
    "Average Loan",
    f"${int(df['credit_amount'].mean())}"
)

c3.metric(
    "Average Age",
    int(df["age"].mean())
)

c4.metric(
    "Maximum Loan",
    f"${int(df['credit_amount'].max())}"
)

st.divider()

# =====================================
# LOAN DISTRIBUTION
# =====================================

st.markdown("""
<h2 style="
text-align:center;
color:#102f5e;
font-family:'Times New Roman';
">
⚖️ Loan Amount Distribution
</h2>
""",
unsafe_allow_html=True)

fig1 = px.histogram(
    df,
    x="credit_amount",
    nbins=30,
    color_discrete_sequence=["#102f5e"]
)

fig1.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(255,255,255,0.75)"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# =====================================
# PURPOSE ANALYSIS
# =====================================

st.markdown("""
<h2 style="
text-align:center;
color:#102f5e;
font-family:'Times New Roman';
">
🏛️ Credit Purpose Distribution
</h2>
""",
unsafe_allow_html=True)

fig2 = px.pie(
    df,
    names="purpose",
    hole=0.4
)

fig2.update_layout(
    paper_bgcolor="rgba(0,0,0,0)"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# =====================================
# RISK CONCENTRATION
# =====================================

st.markdown("""
<h2 style="
text-align:center;
color:#102f5e;
font-family:'Times New Roman';
">
🛡️ Portfolio Risk Concentration
</h2>
""",
unsafe_allow_html=True)

risk_counts = (
    df["Risk Band"]
    .value_counts()
    .reset_index()
)

risk_counts.columns = [
    "Risk Band",
    "Count"
]

fig3 = px.bar(
    risk_counts,
    x="Risk Band",
    y="Count",
    color="Risk Band"
)

fig3.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(255,255,255,0.75)"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# =====================================
# AGE VS CREDIT
# =====================================

st.markdown("""
<h2 style="
text-align:center;
color:#102f5e;
font-family:'Times New Roman';
">
👥 Customer Demographic Analysis
</h2>
""",
unsafe_allow_html=True)

fig4 = px.scatter(
    df,
    x="age",
    y="credit_amount",
    color="target",
    size="month_duration"
)

fig4.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(255,255,255,0.75)"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

# =====================================
# ANALYTICS SUMMARY
# =====================================

st.divider()

st.markdown("""
<div style="
background:rgba(255,255,255,0.75);
padding:20px;
border-radius:15px;
border:2px solid #c9a15d;
">

<h2 style="color:#102f5e;">
📜 Portfolio Intelligence Summary
</h2>

<ul>
<li>The portfolio contains a diversified mix of lending purposes.</li>
<li>Most applicants fall within the low-to-medium credit exposure range.</li>
<li>Higher loan amounts contribute significantly to portfolio concentration risk.</li>
<li>Age and credit exposure demonstrate varying borrower behavior patterns.</li>
<li>The portfolio remains suitable for ongoing monitoring and risk segmentation.</li>
</ul>

</div>
""",
unsafe_allow_html=True)