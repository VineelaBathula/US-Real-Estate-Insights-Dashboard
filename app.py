import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="US Real Estate Insights Dashboard", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("data/processed/us_city_affordability_flagged.csv")

df = load_data()

st.title("US Real Estate Insights Dashboard (City-Level)")
st.caption("Population (Wikipedia) + Median Home Value (Zillow ZHVI City) + Affordability Flags")

# Sidebar filters
st.sidebar.header("Filters")
states = ["All"] + sorted(df["state"].dropna().unique().tolist())
size_cats = ["All"] + sorted(df["city_size_category"].dropna().unique().tolist())
flags = ["All"] + sorted(df["affordability_flag"].dropna().unique().tolist())

state_sel = st.sidebar.selectbox("State", states)
size_sel = st.sidebar.selectbox("City size category", size_cats)
flag_sel = st.sidebar.selectbox("Affordability flag", flags)

filtered = df.copy()
if state_sel != "All":
    filtered = filtered[filtered["state"] == state_sel]
if size_sel != "All":
    filtered = filtered[filtered["city_size_category"] == size_sel]
if flag_sel != "All":
    filtered = filtered[filtered["affordability_flag"] == flag_sel]

# KPIs
col1, col2, col3 = st.columns(3)
col1.metric("Cities in view", f"{len(filtered):,}")
col2.metric("Median home value (median)", f"${filtered['median_home_value'].median():,.0f}")
col3.metric("Population (median)", f"{filtered['population_2024_estimate'].median():,.0f}")

st.divider()

# Scatter plot: population vs home value
st.subheader("Population vs Median Home Value")
fig = px.scatter(
    filtered,
    x="population_2024_estimate",
    y="median_home_value",
    color="affordability_flag",
    hover_data=["city", "state", "city_size_category"],
    log_x=True,
    log_y=True,
    title="City Population vs Median Home Value (log-log)"
)
st.plotly_chart(fig, use_container_width=True)

st.divider()

# Top tables
c1, c2 = st.columns(2)

with c1:
    st.subheader("Top 20 Affordable (Lowest Median Home Value)")
    st.dataframe(
        filtered.sort_values("median_home_value").loc[:, ["city", "state", "city_size_category", "median_home_value", "population_2024_estimate", "affordability_flag"]].head(20),
        use_container_width=True
    )

with c2:
    st.subheader("Top 20 Expensive (Highest Median Home Value)")
    st.dataframe(
        filtered.sort_values("median_home_value", ascending=False).loc[:, ["city", "state", "city_size_category", "median_home_value", "population_2024_estimate", "affordability_flag"]].head(20),
        use_container_width=True
    )
