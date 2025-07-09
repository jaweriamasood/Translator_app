import streamlit as st
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import os

translator = Translator()

st.title("🌐 Language Translation Tool")

text_to_translate = st.text_area("Enter text to translate")

lang_list = list(LANGUAGES.values())
lang_dict = {v: k for k, v in LANGUAGES.items()}

source_lang = st.selectbox("Source Language", lang_list, index=lang_list.index("english"))
target_lang = st.selectbox("Target Language", lang_list, index=lang_list.index("urdu"))

if st.button("Translate"):
    if text_to_translate:
        translated = translator.translate(text_to_translate, src=lang_dict[source_lang], dest=lang_dict[target_lang])
        st.success("Translated Text:")
        st.write(translated.text)

        # Text-to-Speech
        tts = gTTS(text=translated.text, lang=lang_dict[target_lang])
        tts.save("translated_audio.mp3")
        st.audio("translated_audio.mp3", format="audio/mp3")

        # Show copyable text
        st.code(translated.text)
    else:
        st.warning("Please enter some text to translate.")
