import streamlit as st
from style import load_css
import pandas as pd
from api_fetch import update_matches

load_css()

st.title("🏏 Live Match Center")

# ---------------- REFRESH BUTTON ----------------
if st.button("🔄 Refresh Live Matches"):
    update_matches()
    st.success("Live matches updated successfully")

# ---------------- LOAD DATA ----------------
try:
    matches = pd.read_csv("matches.csv").head(6)
except:
    st.warning("No data found. Please click Refresh first.")
    st.stop()

st.subheader("Match Scoreboard")

# ---------------- DISPLAY MATCH CARDS ----------------
for _, row in matches.iterrows():
    st.markdown(
        f"""
        <div style="
            background:linear-gradient(135deg,#1d3557,#457b9d);
            padding:20px;
            border-radius:14px;
            margin-bottom:20px;
            color:white;
            box-shadow:0px 6px 16px rgba(0,0,0,0.35);
        ">

        <div style="display:flex;justify-content:space-between;align-items:center;">

        <div style="font-size:20px;font-weight:bold;">
        {row['team1']}
        </div>

        <div style="
            font-size:22px;
            font-weight:bold;
            background:#e63946;
            padding:6px 14px;
            border-radius:8px;
        ">
        VS
        </div>

        <div style="font-size:20px;font-weight:bold;">
        {row['team2']}
        </div>

        </div>

        <hr style="border:1px solid rgba(255,255,255,0.2);margin-top:15px;margin-bottom:10px">

        <div style="display:flex;justify-content:space-between;font-size:14px;">

        <div>
        📍 <b>Venue</b><br>
        {row['venue']}
        </div>

        <div>
        🌆 <b>City</b><br>
        {row['city']}
        </div>

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )