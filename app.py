import streamlit as st


picture = st.camera_input("Camera Input")

if picture:
     btn = st.download_button(
             label="Download image",
             data=picture,
             file_name="flower.jpeg",
             mime="image/jpeg"
           )