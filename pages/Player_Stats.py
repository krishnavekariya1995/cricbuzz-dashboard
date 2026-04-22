import streamlit as st
from style import load_css
import pandas as pd
import plotly.express as px

load_css()

st.title("📊 Team Statistics")

# ---------------- LOAD DATA ----------------
try:
    matches = pd.read_csv("matches.csv")
except:
    st.warning("No data found. Please refresh Live Matches first.")
    st.stop()

# ---------------- TEAM STATS ----------------
st.subheader("Matches Played by Team")

team_stats = matches["team1"].value_counts().reset_index()
team_stats.columns = ["team", "matches"]

st.dataframe(team_stats, use_container_width=True)

fig1 = px.bar(
    team_stats,
    x="team",
    y="matches",
    color="matches",
    title="Matches Played by Team"
)

st.plotly_chart(fig1, use_container_width=True)

st.divider()

# ---------------- VENUE STATS ----------------
st.subheader("Matches Played by Venue")

venue_stats = matches["venue"].value_counts().reset_index()
venue_stats.columns = ["venue", "matches"]

st.dataframe(venue_stats, use_container_width=True)

fig2 = px.bar(
    venue_stats,
    x="venue",
    y="matches",
    color="matches",
    title="Matches by Venue"
)

st.plotly_chart(fig2, use_container_width=True)

st.divider()

# ---------------- CITY STATS ----------------
st.subheader("Matches Played by City")

city_stats = matches["city"].value_counts().reset_index()
city_stats.columns = ["city", "matches"]

st.dataframe(city_stats, use_container_width=True)

fig3 = px.bar(
    city_stats,
    x="city",
    y="matches",
    color="matches",
    title="Matches by City"
)

st.plotly_chart(fig3, use_container_width=True)
