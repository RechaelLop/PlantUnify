import streamlit as st
from PIL import Image

st.set_page_config(page_title="PlantUnify", layout="centered")

# Load logo
logo = Image.open("assets/plantunify_logo.png")

# Centered layout using columns
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.write("")  # Empty left spacer

with col2:
    st.markdown("<div style='margin-top: 80px;'></div>", unsafe_allow_html=True)  # Adds vertical space
    st.image(logo, width=500)

    st.markdown(
        "<h1 style='text-align: center; margin-top: 20px;'>PlantUnify</h1>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='text-align: center; font-size: 16px;'>A Unified Manufacturing Dashboard</p>",
        unsafe_allow_html=True
    )

with col3:
    st.write("")  # Empty right spacer
