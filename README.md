# 🏏 Cricbuzz LiveStats: Real-Time Cricket Insights & SQL Analytics

Live Demo:- 
Deployed App Link:- 
https://cricbuzz-dashboard-hrmfitpwa3ffjcjlwdck7i.streamlit.app/

## 📌 Project Overview

Cricbuzz LiveStats is a multi-page Streamlit dashboard that integrates live cricket data from the Cricbuzz API with a MySQL database. The application enables users to view real-time match information, perform SQL-based analytics, and interact with cricket data through an intuitive interface.

---

## 🎯 Objectives

* Fetch live cricket match data using REST API
* Store and manage data in a SQL database
* Perform analytical queries using SQL
* Build an interactive dashboard using Streamlit

---

## 🛠️ Technologies Used

* Python
* Streamlit
* MySQL
* SQLAlchemy
* Pandas
* Requests (API integration)
* Plotly (visualization)

---

## 🏗️ Project Structure

```
PythonProject/
│
├── main.py                 # Main dashboard
├── api_fetch.py            # Fetch data from Cricbuzz API
├── db_connection.py        # Database connection
├── style.py                # UI styling
├── requirements.txt        # Dependencies
├── sql_queries.sql         # 25 SQL queries
│
└── pages/
    ├── 1_Live_Matches.py
    ├── 2_Player_Stats.py
    ├── 3_SQL_Analytics.py
    ├── 4_CRUD_Operations.py
```

---

## ⚙️ Setup Instructions

### 1. Clone or Download Project

Place the project folder on your system.

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Setup MySQL Database

Create a database:

```sql
CREATE DATABASE cricket_db;
```

### 4. Configure Database Connection

In `db_connection.py`:

```python
create_engine("mysql+pymysql://root:1234@localhost:3307/cricket_db")
```

### 5. Add API Key

In `api_fetch.py`, replace:

```python
"X-RapidAPI-Key": "YOUR_API_KEY"
```

with your actual API key.

---

## 🔄 Data Flow

```
Cricbuzz API → Python (requests) → MySQL → Streamlit Dashboard
```

---

## 📊 Dashboard Features

### 1. Home Page

* Project overview
* KPI cards
* Match analysis charts

### 2. Live Matches

* Displays live matches from API
* Refresh button to update data

### 3. Player / Team Stats

* Team-based analysis
* Venue and city statistics

### 4. SQL Analytics

* Beginner, Intermediate, Advanced SQL queries
* Interactive query selection

### 5. CRUD Operations

* Add new match
* Update match details
* Delete records

---

## 🧮 SQL Analytics

The project includes **25 SQL queries**:

* Beginner (1–8)
* Intermediate (9–16)
* Advanced (17–25)

These demonstrate:

* GROUP BY
* HAVING
* CASE
* Subqueries
* Window functions

---

## ▶️ Run the Application

```
streamlit run main.py
```

---

## 📦 Requirements

See `requirements.txt` for dependencies.

---

## 🎥 Demo

Record a short video showing:

* Dashboard navigation
* Live match refresh
* SQL analytics page
* CRUD operations

---

## 🔐 Notes

* API key must remain secure
* Database must be running before starting app
* API provides limited data (team-level, not full player stats)

---

## 🚀 Conclusion

This project demonstrates end-to-end integration of:

* API data fetching
* SQL database management
* Data analytics
* Interactive dashboard development

---

## 👨‍💻 Author

Krishna Vekariya
