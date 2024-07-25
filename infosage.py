#final code
import streamlit as st
import wikipedia
import speech_recognition as sr
from googlesearch import search
from transformers import pipeline

# Initialize summarizer
summarizer = pipeline("summarization")

def get_wikipedia_summary(query, max_words=2000, lang='en'):
    """Fetches and summarizes Wikipedia content in the specified language"""
    try:
        wikipedia.set_lang(lang)  # Set the language for Wikipedia queries
        page_content = wikipedia.page(query).content
        summary = summarizer(page_content[:max_words], max_length=700, min_length=30, do_sample=False)
        return summary[0]['summary_text']
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Disambiguation error. Options: {e.options}"
    except wikipedia.exceptions.PageError:
        return "Page not found."
    except Exception as e:
        return f"An error occurred: {e}"

def get_google_links(query, num_links=5, filter_option="All"):
    """Fetches Google search links with filtering options"""
    links = []
    if filter_option == "News":
        query += " news"
    elif filter_option == "Images":
        query += " images"
    elif filter_option == "Videos":
        query += " videos"
    for url in search(query, num_results=num_links):
        links.append(url)
    return links

def main():
    st.title("InfoSage")

    # Application description
    st.write("""
    This application allows you to search for information on any specific topic and find related Google search results. 
    You can either enter a topic name manually or use your voice to provide the same.
    The application will display a summarized overview of the topic
    and will provide you with relevant Google search links for further exploration. You can fetch results in any of the below languages and can filter the search results.
    """)

    # Language selection
    language = st.selectbox("Select language:", ["en", "es", "fr", "de", "zh"])

    # Text input
    query_input = st.text_input("Enter your query:")

    # Speech input
    st.write("Or you can speak your query:")
    if st.button("Record"):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            st.write("Listening...")
            audio = recognizer.listen(source)
            st.write("Processing...")
            try:
                query_input = recognizer.recognize_google(audio)
                st.write(f"You said: {query_input}")
            except sr.UnknownValueError:
                st.error("Sorry, I did not understand the audio.")
            except sr.RequestError:
                st.error("Sorry, there was an error with the speech recognition service.")

    # Search filter
    filter_option = st.selectbox("Filter search results:", ["All", "News", "Images", "Videos"])

    if query_input:
        with st.spinner("Fetching results..."):
            st.subheader("Results:")
            summary = get_wikipedia_summary(query_input, lang=language)
            st.write(summary)

            st.subheader("You can learn more about this topic from the following sources:")
            links = get_google_links(query_input, filter_option=filter_option)
            if links:
                for link in links:
                    st.write(link)
            else:
                st.write("No search results found.")

if __name__ == "__main__":
    main()
