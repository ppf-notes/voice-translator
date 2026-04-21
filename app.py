import streamlit as st
from googletrans import Translator
import speech_recognition as sr

st.title("Voice + Text Translator")

translator = Translator()

# TEXT TRANSLATION
st.header("Text Translation")

text = st.text_area("Enter text")

target_lang = st.selectbox(
    "Translate to",
    ["hi","en","fr","de","es","it","ja"]
)

if st.button("Translate Text"):
    translated = translator.translate(text, dest=target_lang)
    st.success(translated.text)

# VOICE TRANSLATION
st.header("Voice Translation")

if st.button("Start Voice Input"):
    r = sr.Recognizer()

    with sr.Microphone() as source:
        st.write("Speak now...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        st.write("You said:", text)

        translated = translator.translate(text, dest=target_lang)

        st.success("Translated:")
        st.success(translated.text)

    except:
        st.error("Could not understand audio")