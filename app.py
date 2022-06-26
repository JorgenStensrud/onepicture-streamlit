import streamlit as st


picture = st.camera_input("Camera Input")

if picture:
    st.download_button("Download", picture)

with open("flower.png", "rb") as file:
     btn = st.download_button(
             label="Download image",
             data=file,
             file_name="flower.jpeg",
             mime="image/jpeg"
           )