"""
Level 3 (Advanced) - Task 2: Interactive Dashboard (Streamlit)

A dashboard tool the assignment names (Power BI/Tableau) doesn't run on
Ubuntu, so this is a self-hosted interactive dashboard built with
Streamlit - same objective: import data, chart it, add filters, publish.

Run:
    cd codveda_local_setup && source venv/bin/activate
    streamlit run level3_advanced/level3_task2_dashboard.py

Uses the cleaned sentiment dataset (Level 1 Task 1 output).
Note: the raw 'Sentiment' column has 191 fine-grained emotion labels
(Joy, Excitement, ...). The dashboard computes the 3-class sentiment
(positive/negative/neutral) with VADER for the headline chart, and shows
top emotions as a separate view - honest about what the data is.
"""

import pandas as pd
import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer

st.set_page_config(page_title="Sentiment & Engagement Dashboard", layout="wide")
st.title("📊 Sentiment & Engagement Dashboard")
st.caption("Interactive dashboard — Codveda Level 3 Task 2 (Streamlit, Linux-friendly)")

# --- Load data -------------------------------------------------------------
@st.cache_data
def load():
    df = pd.read_csv("level1_basic/cleaned_sentiment_dataset.csv")
    df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce")
    return df

df = load()

# --- 3-class sentiment (VADER) - same approach as Level 3 Task 3 -----------
@st.cache_data
def sentiment_class(_df):
    sia = SentimentIntensityAnalyzer()
    compound = _df["Text"].astype(str).apply(lambda t: sia.polarity_scores(t)["compound"])
    def label(c):
        return "Positive" if c >= 0.05 else ("Negative" if c <= -0.05 else "Neutral")
    return compound.apply(label)

df["SentimentClass"] = sentiment_class(df)

# --- Sidebar filters (the "slicers") ---------------------------------------
st.sidebar.header("Filters")
sentiments = st.sidebar.multiselect(
    "Sentiment", options=["Positive", "Negative", "Neutral"],
    default=["Positive", "Negative", "Neutral"])
platforms = st.sidebar.multiselect(
    "Platform", options=sorted(df["Platform"].dropna().unique()),
    default=sorted(df["Platform"].dropna().unique()))
years = sorted(df["Timestamp"].dt.year.dropna().unique().astype(int))
year_range = st.sidebar.slider("Year", min_value=int(min(years)),
                               max_value=int(max(years)),
                               value=(int(min(years)), int(max(years))))

# Apply filters
mask = (
    df["SentimentClass"].isin(sentiments)
    & df["Platform"].isin(platforms)
    & df["Timestamp"].dt.year.between(year_range[0], year_range[1])
)
d = df[mask]

# --- Top metrics -----------------------------------------------------------
c1, c2, c3, c4 = st.columns(4)
c1.metric("Posts", len(d))
c2.metric("Total Likes", int(d["Likes"].sum()))
c3.metric("Total Retweets", int(d["Retweets"].sum()))
c4.metric("Avg Likes/Post", round(float(d["Likes"].mean()), 1))

# --- Charts -----------------------------------------------------------------
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Sentiment Distribution (3-class, VADER)")
    st.bar_chart(d["SentimentClass"].value_counts())

    st.subheader("Likes per Year")
    st.line_chart(d.groupby(d["Timestamp"].dt.year)["Likes"].sum())

with col_right:
    st.subheader("Top Emotions (raw labels)")
    st.bar_chart(d["Sentiment"].value_counts().head(15))

    st.subheader("Retweets vs Likes")
    st.scatter_chart(d[["Likes", "Retweets"]])

st.subheader("Engagement by Platform")
st.bar_chart(d.groupby("Platform")[["Likes", "Retweets"]].sum())

st.caption("Data: cleaned_sentiment_dataset.csv · interactive filters in the sidebar · "
           "served via Streamlit (self-hosted, no paid tier)")