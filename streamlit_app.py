from io import BytesIO

import streamlit as st
import cv2
import numpy as np
from PIL import Image

def create_file(image_array):
    image_stream = BytesIO()
    img = Image.fromarray(image_array)
    if file_extension == "jpg":
        img.save(image_stream, format="JPEG", quality=95)
    elif file_extension == "png":
        img.save(image_stream, format="PNG")
    image_stream.seek(0)
    return image_stream.getvalue()

def distort_image(image_array, k=0):
    rows, cols = image_array.shape[:2]
    mapy, mapx = np.indices((rows, cols),dtype=np.float32)
    mapy, mapx, = 2*mapy/(rows-1)-1, 2*mapx/(cols-1)-1
    r, theta = cv2.cartToPolar(mapx, mapy)
    k1, k2, k3 = 0.5 * k / 255, 0.2 * k / 255, 0.0 * k / 255
    ru = r*(1 + k1*(r**2) + k2*(r**4) + k3*(r**6))
    mapx, mapy = cv2.polarToCart(ru, theta)
    mapx, mapy = ((mapx + 1)*cols-1)/2, ((mapy + 1)*rows-1)/2
    return cv2.remap(image_array, mapx, mapy, cv2.INTER_LINEAR)


st.set_page_config(
    page_title="Image Preprocessing For an Artist", 
    page_icon=":art:", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

st.title("Image Preprocessing For an Artist")
st.header("Upload your image and proceess it!")
uploaded_file = st.file_uploader("Upload your work!", type=["jpg", "png"])

if uploaded_file:
    file_name, file_extension = uploaded_file.name.rsplit(".", 1)

    with st.sidebar:
        step = st.selectbox("Select a filter", ["Distortion", "Perspective"])

    if step == "Distortion":
        image_array = np.array(Image.open(uploaded_file))
        k = st.slider("Distortion Efficient", 0, 255, 0)
        processed_image = distort_image(image_array, k)
        st.image(processed_image, caption="Distorted Image")

        st.download_button(
            label="Download", 
            data=create_file(processed_image), 
            file_name=f"{file_name}_processed.{file_extension}", 
            mime=f"image/{file_extension}")
        
    elif step == "Perspective":
        st.image(uploaded_file, caption="Original Image")