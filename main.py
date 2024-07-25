import streamlit as st
from mood_analyzer import mood_analyzer_app
from healthcare_guide import healthcare_guide_app
from infosage import infosage_app
from handwritten_to_digital import handwritten_to_digital_app

# Custom CSS for styling
st.markdown("""
    <style>
    .stApp {
        background-color: #f0f4f8;
    }
    .main-header {
        font-size: 2.5em;
        font-weight: bold;
        color: #2e3b4e;
        text-align: center;
    }
    .stTextInput input, .stTextArea textarea {
        border-radius: 5px;
        border: 1px solid #ccc;
        padding: 10px;
        font-size: 16px;
    }
    .stButton button {
        background-color: #007bff;
        color: white;
        font-size: 16px;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        cursor: pointer;
    }
    .stButton button:hover {
        background-color: #0056b3;
    }
    .info-box {
        border-radius: 10px;
        border: 1px solid #ddd;
        background-color: #fff;
        padding: 15px;
        margin: 10px 0;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        color: #000;
    }
    .info-box h4 {
        color: #000;
        font-size: 1.5em;
        margin-bottom: 10px;
    }
    .stMarkdown {
        font-size: 1.2em;
        color: #000;
    }
    .footer {
        text-align: center;
        font-size: 0.9em;
        color: #888;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Main application title and description
st.markdown('<div class="main-header">IntelliAid - Your Digital Companion</div>', unsafe_allow_html=True)
st.markdown("""
    **Welcome to IntelliAid**, your digital companion. This application can assist you in various ways:
    - **Human Health Assistant**: Analyze your mood or get a healthcare guide based on your symptoms.
    - **InfoSage**: Search for information on any specific topic and get relevant Google search results.
    - **Handwritten to Digital Text Converter**: Convert images of handwritten text into digital text.

    Please select one of the options below to get started:
""")

# Main menu
app_mode = st.selectbox("Choose a feature", ["Human Health Assistant - Mood Analyzer", "Human Health Assistant - Healthcare Guide", "InfoSage", "Handwritten to Digital Text Converter"])

if app_mode == "Human Health Assistant - Mood Analyzer":
    mood_analyzer_app()
elif app_mode == "Human Health Assistant - Healthcare Guide":
    healthcare_guide_app()
elif app_mode == "InfoSage":
    infosage_app()
elif app_mode == "Handwritten to Digital Text Converter":
    handwritten_to_digital_app()

st.markdown("<div class='footer'>IntelliAid © 2024</div>", unsafe_allow_html=True)
