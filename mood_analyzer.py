import streamlit as st
from textblob import TextBlob
import pandas as pd
import datetime
import plotly.express as px

def analyze_mood(text):
    """Analyze mood based on the input text."""
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        mood = "Positive", "😊"
    elif sentiment < 0:
        mood = "Negative", "😢"
    else:
        mood = "Neutral", "😐"
    return mood, sentiment

def update_history(text, mood, score):
    """Update mood history with the latest analysis."""
    new_entry = pd.DataFrame([[datetime.datetime.now(), text, mood, score]],
                             columns=["Timestamp", "Text", "Mood", "Score"])
    st.session_state.history = pd.concat([st.session_state.history, new_entry], ignore_index=True)

def plot_mood_graph(history):
    """Plot mood graph using Plotly."""
    history['Timestamp'] = pd.to_datetime(history['Timestamp'])
    fig = px.line(history, x='Timestamp', y='Score', title='Mood Trend Over Time',
                  labels={'Timestamp': 'Time', 'Score': 'Sentiment Score'})
    st.plotly_chart(fig)

def get_recommendations(mood):
    """Provide recommendations based on the detected mood."""
    recommendations = {
        "Positive": "Keep up the great work! Consider sharing your positivity with others.",
        "Negative": "Take a deep breath and try a relaxing activity. Remember, it's okay to seek support.",
        "Neutral": "Stay balanced. Engage in activities that you enjoy and find fulfilling."
    }
    return recommendations.get(mood, "No recommendations available.")

def mood_analyzer_app():
    if 'history' not in st.session_state:
        st.session_state.history = pd.DataFrame(columns=["Timestamp", "Text", "Mood", "Score"])

    st.markdown('<div class="main-header">Mood Analyzer</div>', unsafe_allow_html=True)
    st.markdown("Enter your text below to analyze the mood:")

    user_input = st.text_area("Text Input")

    if st.button("Analyze"):
        if user_input:
            mood, score = analyze_mood(user_input)
            st.markdown(f'<p class="text-black">Mood: {mood[0]} {mood[1]}</p>', unsafe_allow_html=True)
            st.markdown(f'<p class="text-black">Recommendation: {get_recommendations(mood[0])}</p>', unsafe_allow_html=True)
            update_history(user_input, mood[0], score)
        else:
            st.markdown('<p class="text-black">Please enter some text to analyze.</p>', unsafe_allow_html=True)

    if not st.session_state.history.empty:
        st.markdown('<p class="text-black">Mood History:</p>', unsafe_allow_html=True)
        st.dataframe(st.session_state.history)
        st.write("Mood Trend Graph:")
        plot_mood_graph(st.session_state.history)
