import streamlit as st
import numpy as np


picture = st.camera_input("Camera Input")

def format_picture(picture):
    bytes_picture  = picture.getvalue()
    # cv2_img = cv2.imdecode(np.frombuffer(bytes_picture, np.uint8), cv2.IMREAD_COLOR)
    return bytes_picture

if picture:
    st.download_button(
        label = "Download",
        data = format_picture(picture),
        file_name = "image.jpeg",
        mime = "image/jpeg"
    )
