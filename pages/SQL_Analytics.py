import streamlit as st
import pandas as pd

st.title("📊 SQL Analytics")

# ---------------- LOAD DATA ----------------
try:
    df = pd.read_csv("matches.csv")
except:
    st.warning("No data found. Please refresh Live Matches first.")
    st.stop()

# ---------------- SELECT LEVEL ----------------
level = st.selectbox("Select Query Level", ["Beginner", "Intermediate", "Advanced"])

# ---------------- QUERY OPTIONS ----------------
if level == "Beginner":
    query_options = [
        "Matches by Team",
        "Matches by Venue",
        "Matches by City"
    ]

elif level == "Intermediate":
    query_options = [
        "Top Cities Hosting Matches",
        "Venue Usage Analysis",
        "Team Participation Count"
    ]

else:
    query_options = [
        "Most Active Teams",
        "City vs Venue Distribution",
        "Frequent Match Locations"
    ]

# ---------------- SELECT QUERY ----------------
query_name = st.selectbox("Select Query", query_options)

# ---------------- RUN QUERY ----------------
if query_name == "Matches by Team":
    result = df.groupby("team1").size().reset_index(name="matches").sort_values(by="matches", ascending=False)

elif query_name == "Matches by Venue":
    result = df.groupby("venue").size().reset_index(name="matches").sort_values(by="matches", ascending=False)

elif query_name == "Matches by City":
    result = df.groupby("city").size().reset_index(name="matches").sort_values(by="matches", ascending=False)

elif query_name == "Top Cities Hosting Matches":
    result = df.groupby("city").size().reset_index(name="total_matches").sort_values(by="total_matches", ascending=False).head(5)

elif query_name == "Venue Usage Analysis":
    temp = df.groupby("venue").size().reset_index(name="matches_played")
    result = temp[temp["matches_played"] > 1].sort_values(by="matches_played", ascending=False)

elif query_name == "Team Participation Count":
    result = df.groupby("team1").size().reset_index(name="total_matches").sort_values(by="total_matches", ascending=False)

elif query_name == "Most Active Teams":
    result = df.groupby("team1").size().reset_index(name="matches").sort_values(by="matches", ascending=False).head(3)

elif query_name == "City vs Venue Distribution":
    result = df.groupby(["city", "venue"]).size().reset_index(name="matches").sort_values(by="matches", ascending=False)

elif query_name == "Frequent Match Locations":
    result = df.groupby("city")["venue"].nunique().reset_index(name="venues").sort_values(by="venues", ascending=False)

# ---------------- DISPLAY ----------------
st.subheader("Result")
st.dataframe(result, use_container_width=True)
