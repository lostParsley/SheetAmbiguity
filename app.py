import math

import pandas as pd
import streamlit as st

st.set_page_config(page_title="A4 Sheet Prediction", page_icon="📄", layout="wide")
st.markdown("""
<style>
.stock-card {
    padding: 2.5rem;
    border: 1px solid rgba(52, 211, 153, 0.35);
    border-radius: 20px;
    background: linear-gradient(120deg, #064e3b, #065f46 55%, #047857);
    box-shadow: 0 12px 35px rgba(4, 120, 87, 0.25);
    text-align: center;
    color: #ecfdf5;
}
.stock-label {font-size: 1.15rem; font-weight: 600; letter-spacing: 0.04em;}
.stock-number {font-size: clamp(4rem, 10vw, 7rem); font-weight: 800; line-height: 1.1; color: #6ee7b7;}
.stock-unit {font-size: 1.1rem; color: #d1fae5;}
</style>
""", unsafe_allow_html=True)

st.title("📄 A4 Sheet Prediction")
st.caption("Turn observation data into a confident stock plan for tomorrow.")

st.sidebar.header("Stock planning")
operating_hours = st.sidebar.slider("Operating Hours", 4, 12, 8)
buffer_percent = st.sidebar.slider("Safety Buffer %", 0, 50, 20)
st.sidebar.caption("Adjust the sliders to explore tomorrow's stock needs.")

try:
    data = pd.read_csv("data.csv")
except (OSError, pd.errors.EmptyDataError, pd.errors.ParserError, UnicodeError) as error:
    st.error(f"Could not read data.csv: {error}")
    st.stop()

required_columns = [
    "Time", "Sheets requested", "Sheets sold", "Students served",
    "Students turned away", "Stock remaining",
]
missing_columns = [column for column in required_columns if column not in data.columns]
if missing_columns:
    st.error(f"Missing required columns: {', '.join(missing_columns)}")
    st.stop()

for column in ["Sheets requested", "Sheets sold"]:
    data[column] = pd.to_numeric(data[column], errors="coerce")
    data.loc[~data[column].map(math.isfinite), column] = float("nan")
data = data.dropna(subset=["Sheets requested", "Sheets sold"]).copy()
if data.empty:
    st.warning("No valid records with numeric sheets requested and sold were found.")
    st.stop()

data["Students turned away"] = pd.to_numeric(data["Students turned away"], errors="coerce")
if data["Students turned away"].isna().any():
    st.warning("Missing or invalid students turned away values were excluded from that total.")

total_requested = data["Sheets requested"].sum()
total_sold = data["Sheets sold"].sum()
total_turned_away = data["Students turned away"].sum()
observed_hours = len(data) * 5 / 60
hourly_demand = total_requested / observed_hours
recommendation = math.ceil(hourly_demand * operating_hours * (1 + buffer_percent / 100))

st.divider()
st.subheader("At a glance")
metrics = st.columns(5)
metrics[0].metric("Valid records", f"{len(data):,}")
metrics[1].metric("Total requested", f"{total_requested:,.0f}")
metrics[2].metric("Total sold", f"{total_sold:,.0f}")
metrics[3].metric("Missed sales", f"{total_requested - total_sold:,.0f}")
metrics[4].metric("Students turned away", f"{total_turned_away:,.0f}")

st.divider()
st.subheader("Demand over time")
st.caption("Compare requested and sold sheets across your observations.")
st.line_chart(data.set_index("Time")[["Sheets requested", "Sheets sold"]])

st.divider()
st.subheader("Tomorrow's stock plan")
details = st.columns(3)
details[0].metric("Observed hours", f"{observed_hours:,.2f}")
details[1].metric("Hourly demand", f"{hourly_demand:,.2f} sheets")
details[2].metric("Safety buffer", f"{buffer_percent}%")
st.markdown(f"""
<div class="stock-card">
    <div class="stock-label">Tomorrow's Recommended Stock</div>
    <div class="stock-number">{recommendation:,}</div>
    <div class="stock-unit">A4 sheets</div>
</div>
""", unsafe_allow_html=True)
