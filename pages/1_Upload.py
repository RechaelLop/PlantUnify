import streamlit as st
import pandas as pd
import os
import base64

st.set_page_config(page_title="Upload", layout="centered")

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

st.title("📤 Upload & Select Plant Data")

# List standardized files
data_dir = "data/standardized"
plant_files = sorted([f for f in os.listdir(data_dir) if f.endswith(".csv")])
options = ["All Files"] + plant_files

selected_file = st.selectbox("Select a Plant File", options)

if selected_file == "All Files":
    dfs = [pd.read_csv(os.path.join(data_dir, f)) for f in plant_files]
    df = pd.concat(dfs, ignore_index=True)
else:
    df = pd.read_csv(os.path.join(data_dir, selected_file))

# --- Display Summary ---
st.subheader("📊 File Summary")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Bottles", f"{int(df['bottles_produced'].sum()):,}")
with col2:
    defect_rate = df['defect_count'].sum() / df['bottles_produced'].sum()
    st.metric("Defect Rate", f"{defect_rate:.2%}")
with col3:
    st.metric("Downtime (min)", f"{int(df['downtime_minutes'].sum()):,}")

st.dataframe(df.head())

# --- Generate Report ---
if st.button("📈 Generate Report"):
    st.session_state["selected_file"] = selected_file
    st.success("Selection saved! Go to the Dashboard page to view your report.")
