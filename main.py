import streamlit as st
from style import load_css
import pandas as pd
import plotly.express as px

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Cricbuzz Analytics Dashboard",
    page_icon="🏏",
    layout="wide"
)

load_css()



# ---------------- KPI STYLE ----------------
st.markdown("""
<style>
.kpi-card{
background:linear-gradient(135deg,#1d3557,#457b9d);
padding:20px;
border-radius:12px;
text-align:center;
color:white;
box-shadow:0px 4px 12px rgba(0,0,0,0.4);
}
.kpi-title{font-size:18px;}
.kpi-value{font-size:36px;font-weight:bold;}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("🏏 Cricbuzz LiveStats Dashboard")

# ---------------- LOAD DATA ----------------
try:
    matches = pd.read_csv("matches.csv")
except:
    st.warning("No data found. Please go to Live Matches and click Refresh.")
    st.stop()

# ---------------- KPI CARDS ----------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="kpi-card">
    <div class="kpi-title">Total Matches</div>
    <div class="kpi-value">{len(matches)}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="kpi-card">
    <div class="kpi-title">Teams</div>
    <div class="kpi-value">{matches['team1'].nunique()}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="kpi-card">
    <div class="kpi-title">Venues</div>
    <div class="kpi-value">{matches['venue'].nunique()}</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ---------------- CHARTS ----------------
c1, c2 = st.columns(2)

with c1:
    venue_chart = matches["venue"].value_counts().reset_index()
    venue_chart.columns = ["venue","matches"]

    fig1 = px.bar(
        venue_chart,
        x="venue",
        y="matches",
        color="matches",
        title="Matches by Venue"
    )

    st.plotly_chart(fig1, use_container_width=True)

with c2:
    team_chart = matches["team1"].value_counts().reset_index()
    team_chart.columns = ["team","matches"]

    fig2 = px.bar(
        team_chart,
        x="team",
        y="matches",
        color="matches",
        title="Matches by Team"
    )

    st.plotly_chart(fig2, use_container_width=True)