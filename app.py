import streamlit as st


picture = st.camera_input("Camera Input")

if picture:
    st.download_button("Download", picture)
