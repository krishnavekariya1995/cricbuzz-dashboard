import streamlit as st

def load_css():
    st.markdown("""
    <style>

    .main {
        background-color:#0E1117;
    }

    .kpi-card {
        background: linear-gradient(135deg,#1D3557,#457B9D);
        padding:20px;
        border-radius:12px;
        text-align:center;
        color:white;
        box-shadow:0px 4px 15px rgba(0,0,0,0.4);
        height:150px;
        display:flex;
        flex-direction:column;
        justify-content:center;
        align-items:center;
    }

    .kpi-card h3{
        margin:0;
        font-size:18px;
    }

    .kpi-card h1{
        margin-top:10px;
        font-size:36px;
    }

    .section-card {
        background-color:#1C1F26;
        padding:20px;
        border-radius:10px;
        margin-top:20px;
        box-shadow:0px 3px 10px rgba(0,0,0,0.3);
    }

    h1,h2,h3 {
        color:#E63946;
    }

    </style>
    """, unsafe_allow_html=True)