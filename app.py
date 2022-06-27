import streamlit as st
import numpy as np
import cv2



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

def detect_face(img):
    bytes_picture  = picture.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_picture, np.uint8), cv2.IMREAD_COLOR)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    return faces


def detect_smile(picture):
    bytes_picture  = picture.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_picture, np.uint8), cv2.IMREAD_COLOR)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
    gray = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = cv2_img[y:y+h, x:x+w]
        smile = smile_cascade.detectMultiScale(roi_gray, 1.8, 22)
        # for (sx,sy,sw,sh) in smile:
        #     cv2.rectangle(roi_color, (sx,sy), (sx+sw, sy+sh), (0,255,0), 2)
    return smile

if picture:
    bytes_picture  = picture.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_picture, np.uint8), cv2.IMREAD_COLOR)
    # faces = detect_face(picture)
    smile = detect_smile(picture)
    st.write("Found {} faces!".format(len(smile)))
    for (x,y,w,h) in smile:
        cv2.rectangle(cv2_img, (x,y), (x+w, y+h), (255,0,0), 2)
    st.image(cv2_img)