import streamlit as st
import pandas as pd

st.title("🛠 CRUD Operations - Matches")

# ---------------- LOAD DATA ----------------
try:
    df = pd.read_csv("matches.csv")
except:
    df = pd.DataFrame(columns=["team1", "team2", "venue", "city"])

st.subheader("Current Matches")
st.dataframe(df, use_container_width=True)

st.divider()

# ---------------- CREATE ----------------
st.subheader("➕ Add New Match")

team1 = st.text_input("Team 1")
team2 = st.text_input("Team 2")
venue = st.text_input("Venue")
city = st.text_input("City")

if st.button("Add Match"):
    if team1 and team2 and venue and city:

        new_row = pd.DataFrame([{
            "team1": team1,
            "team2": team2,
            "venue": venue,
            "city": city
        }])

        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv("matches.csv", index=False)

        st.success("Match added successfully")
        st.rerun()

    else:
        st.warning("Fill all fields")

st.divider()

# ---------------- UPDATE ----------------
st.subheader("✏ Update Match Venue")

if not df.empty:
    row_index = st.selectbox("Select Row Index", df.index)
    new_venue = st.text_input("New Venue")

    if st.button("Update Venue"):
        if new_venue:
            df.loc[row_index, "venue"] = new_venue
            df.to_csv("matches.csv", index=False)

            st.success("Updated successfully")
            st.rerun()
        else:
            st.warning("Enter new venue")

st.divider()

# ---------------- DELETE ----------------
st.subheader("🗑 Delete Match")

if not df.empty:
    delete_index = st.selectbox("Select Row to Delete", df.index, key="delete")

    if st.button("Delete Match"):
        df = df.drop(delete_index).reset_index(drop=True)
        df.to_csv("matches.csv", index=False)

        st.success("Deleted successfully")
        st.rerun()
