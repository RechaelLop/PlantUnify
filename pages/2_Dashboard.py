import streamlit as st
import pandas as pd
import os
import plotly.express as px
import base64


st.set_page_config(page_title="Dashboard", layout="wide")

def image_to_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

logo_base64 = image_to_base64("assets/plantunify_logo.png")

st.markdown(
    f"""
    <style>
    .logo-container {{
        position: fixed;
        top: 5rem;
        right: 3rem;
        z-index: 100;
    }}
    .logo-container img {{
        width: 50px;
        border-radius: 5px;
        box-shadow: 0 0 10px #4CAF50;
    }}
    </style>
    <div class="logo-container">
        <img src="data:image/png;base64,{logo_base64}">
    </div>
    """,
    unsafe_allow_html=True
)

st.title("📊 PlantUnify – Dashboard")

if "selected_file" not in st.session_state:
    st.warning("No file selected. Please go to the Upload page first.")
    st.stop()

data_dir = "data/standardized"
selected = st.session_state["selected_file"]

if selected == "All Files":
    dfs = [pd.read_csv(os.path.join(data_dir, f)) for f in os.listdir(data_dir) if f.endswith(".csv")]
    df = pd.concat(dfs, ignore_index=True)
else:
    df = pd.read_csv(os.path.join(data_dir, selected))

# KPIs
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("🍼 Bottles Produced", f"{int(df['bottles_produced'].sum()):,}")
with col2:
    st.metric("❌ Defect Rate", f"{(df['defect_count'].sum() / df['bottles_produced'].sum()):.2%}")
with col3:
    st.metric("🕒 Downtime (min)", f"{int(df['downtime_minutes'].sum()):,}")

st.markdown("---")

# Charts
st.subheader("📈 Production by Shift")
fig1 = px.bar(df.groupby("shift")["bottles_produced"].sum().reset_index(),
              x="shift", y="bottles_produced", color="shift")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("📉 Defects Over Time")
fig2 = px.line(df, x="date", y="defect_count", markers=True)
st.plotly_chart(fig2, use_container_width=True)

st.subheader("🧾 Data Table")
st.dataframe(df)
