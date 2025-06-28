import streamlit as st
import pandas as pd
import os
import glob
import plotly.express as px

# --- Load Cleaned Data ---
def load_cleaned_data():
    all_files = glob.glob("data/standardized/*.csv")
    dfs = []
    for file in all_files:
        df = pd.read_csv(file)
        df["plant_id"] = os.path.basename(file).split("_")[0]
        dfs.append(df)
    return pd.concat(dfs, ignore_index=True)

# --- Load Data ---
df = load_cleaned_data()

st.set_page_config(page_title="PlantUnify Dashboard", layout="wide")
st.title("🏭 PlantUnify – Unified Manufacturing Dashboard")

# --- KPIs ---
col1, col2, col3 = st.columns(3)

with col1:
    total_bottles = int(df["bottles_produced"].sum())
    st.metric("🍼 Total Bottles Produced", f"{total_bottles:,}")

with col2:
    total_defects = int(df["defect_count"].sum())
    defect_rate = total_defects / total_bottles if total_bottles > 0 else 0
    st.metric("❌ Defect Rate", f"{defect_rate:.2%}")

with col3:
    downtime = int(df["downtime_minutes"].sum())
    st.metric("🕒 Total Downtime (min)", f"{downtime:,}")

st.markdown("---")

# --- Filters ---
plant_options = sorted(df["plant_id"].unique())
selected_plant = st.selectbox("Filter by Plant", options=["All"] + plant_options)

if selected_plant != "All":
    df = df[df["plant_id"] == selected_plant]

# --- Visuals ---
st.subheader("📊 Production by Shift")
fig1 = px.bar(df.groupby("shift")["bottles_produced"].sum().reset_index(),
              x="shift", y="bottles_produced", color="shift",
              labels={"bottles_produced": "Bottles Produced"})
st.plotly_chart(fig1, use_container_width=True)

st.subheader("📉 Defects Over Time")
fig2 = px.line(df, x="date", y="defect_count", color="plant_id", markers=True)
st.plotly_chart(fig2, use_container_width=True)

st.subheader("🧮 Raw Data Preview")
st.dataframe(df)

