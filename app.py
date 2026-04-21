import streamlit as st
from googletrans import Translator
import speech_recognition as sr

st.title("🌍 Voice + Text Translator")

translator = Translator()

# TEXT
st.header("Text Translation")

text = st.text_area("Enter text")

lang = st.selectbox(
    "Translate to",
    ["hi","en","fr","de","es","it","ja"]
)

if st.button("Translate Text"):
    translated = translator.translate(text, dest=lang)
    st.success(translated.text)


# VOICE
st.header("Voice Translation")

audio_file = st.file_uploader(
    "Upload audio file (.wav)", 
    type=["wav"]
)

if audio_file is not None:

    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio)

        st.write("You said:", text)

        translated = translator.translate(text, dest=lang)

        st.success("Translated:")
        st.success(translated.text)

    except:
        st.error("Could not understand audio")
