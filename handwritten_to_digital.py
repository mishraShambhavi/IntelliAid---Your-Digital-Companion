import streamlit as st
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
import cv2

# Path to the tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_image(image):
    """
    Preprocess the image to improve OCR accuracy.
    :param image: PIL Image object
    :return: Preprocessed PIL Image object
    """
    # Convert image to grayscale
    image = image.convert('L')

    # Apply thresholding
    image = image.point(lambda p: p > 128 and 255)

    # Convert to OpenCV format
    open_cv_image = np.array(image)

    # Apply median blur to remove noise
    open_cv_image = cv2.medianBlur(open_cv_image, 3)

    # Apply adaptive thresholding
    open_cv_image = cv2.adaptiveThreshold(open_cv_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # Convert back to PIL Image format
    preprocessed_image = Image.fromarray(open_cv_image)

    return preprocessed_image

def convert_image_to_text(image):
    """
    Converts handwritten text in an image to a string.
    :param image: PIL Image object
    :return: Extracted text as a string
    """
    try:
        # Preprocess the image
        preprocessed_image = preprocess_image(image)

        # Use pytesseract to do OCR on the image
        text = pytesseract.image_to_string(preprocessed_image)
        return text
    except Exception as e:
        st.error(f"Error: {e}")
        return ""

def handwritten_to_digital_app():
    st.markdown('<div class="main-header">Handwritten Text to Digital Text Converter</div>', unsafe_allow_html=True)
    st.write("Upload an image of handwritten text, and this app will convert it to digital text.")

    uploaded_file = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        # Open the image file
        image = Image.open(uploaded_file)

        # Display the uploaded image
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Convert the image to text
        extracted_text = convert_image_to_text(image)

        # Display the extracted text
        st.subheader("Extracted Text:")
        st.text(extracted_text)
