import os

import streamlit as st
import cv2
import numpy as np
from PIL import Image


st.set_page_config(
    page_title="Image Preprocessing For an Artist", 
    page_icon=":art:", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

st.title("Image Preprocessing For an Artist")
st.header("Upload your image and let the AI do the rest!")
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png"])

step1, step2 = None, None
checked = False

with st.sidebar:
    step1 = st.selectbox("Step 1: Select a filter", [None, "Distortion", "Perspective"])
    checked = st.checkbox("Done. To the next step!")
    if step1 == "Distortion":
        k = st.slider("Distortion Efficient", 0, 255, 125, disabled=checked)
    if step1 == "Perspective":
        st.write("Click 4 edges of the image to select the point.")
    step2 = st.selectbox("Step 2: Select a filter", [None, "Distortion", "Perspective"], disabled=not checked)


# Distortion


tab1, tab2 = st.tabs([f"STEP1: {step1}", f"STEP2: {step2}"])

with tab1:
    if uploaded_file:
        if step1 == "Distortion":
            file_name, file_extension = os.path.splitext(uploaded_file.name)
            file_extension = file_extension.replace(".", "")
            original_image = np.array(Image.open(uploaded_file))
            rows, cols = original_image.shape[:2]
            mapy, mapx = np.indices((rows, cols),dtype=np.float32)
            mapx = 2*mapx/(cols-1)-1
            mapy = 2*mapy/(rows-1)-1
            r, theta = cv2.cartToPolar(mapx, mapy)
            k1 = 0.5 * k / 255
            k2 = 0.2 * k / 255
            k3 = 0.0 * k / 255
            ru = r*(1 + k1*(r**2) + k2*(r**4) + k3*(r**6))
            mapx, mapy = cv2.polarToCart(ru, theta)
            mapx = ((mapx + 1)*cols-1)/2
            mapy = ((mapy + 1)*rows-1)/2
            distored_image = cv2.remap(original_image, mapx, mapy, cv2.INTER_LINEAR)
            col1, col2 = st.columns(2)
            col1.image(original_image, caption="Original")
            col2.image(distored_image, caption="Canny")
            col2.download_button("Download", distored_image.tobytes(), f"canny_{file_name}.{file_extension}", "image/{file_extension}")
        if step1 == "Perspective":
            st.image(uploaded_file)
            st.write("Click 4 edges of the image to select the point.")
        st.button("Next Step")
