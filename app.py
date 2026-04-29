import streamlit as st
from deep_translator import GoogleTranslator
import speech_recognition as sr
import tempfile

st.set_page_config(page_title="Voice + Text Translator", page_icon="🌍")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #1e1e2f;
        color: white;
    }

    h1, h2, h3, p, label {
        color: white !important;
    }

    .stTextArea textarea {
        background-color: #2b2b40;
        color: white;
    }

    .stSelectbox div {
        background-color: #2b2b40;
        color: white;
    }

    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        padding: 8px 20px;
    }

    .stButton button:hover {
        background-color: #45a049;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🌍 Voice + Text Translator")

languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Italian": "it",
    "Japanese": "ja"
}

target_language_name = st.selectbox("Translate to", list(languages.keys()))
target_lang = languages[target_language_name]

st.header("Text Translation")

text = st.text_area("Enter text")

if st.button("Translate Text"):
    if text.strip():
        try:
            translated = GoogleTranslator(source="auto", target=target_lang).translate(text)
            st.success(translated)
        except Exception as e:
            st.error(f"Translation error: {e}")
    else:
        st.warning("Please enter some text.")

st.header("Voice Translation")

audio_file = st.file_uploader("Upload audio file", type=["wav", "mp3", "m4a"])

if audio_file is not None:
    recognizer = sr.Recognizer()

    try:
        suffix = "." + audio_file.name.split(".")[-1]

        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp_file:
            tmp_file.write(audio_file.read())
            temp_path = tmp_file.name

        if suffix.lower() not in [".wav", ".aiff", ".flac"]:
            st.warning("For best results, upload a WAV file.")

        with sr.AudioFile(temp_path) as source:
            audio = recognizer.record(source)

        spoken_text = recognizer.recognize_google(audio)

        st.write("You said:", spoken_text)

        translated = GoogleTranslator(source="auto", target=target_lang).translate(spoken_text)

        st.success("Translated text:")
        st.success(translated)

    except Exception as e:
        st.error(f"Audio processing error: {e}")

    except Exception as e:
        st.error(f"Audio processing error: {e}")
