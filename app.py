
import streamlit as st
from deep_translator import MyMemoryTranslator

st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 Language Translation Tool")
st.write("Translate text from one language to another easily.")


languages = {
    "English": "english",
    "Tamil": "tamil india",
    "Hindi": "hindi",
    "Telugu": "telugu",
    "Malayalam": "malayalam",
    "Kannada": "kannada",
    "French": "french",
    "German": "german",
    "Spanish": "spanish",
    "Japanese": "japanese"
}

col1, col2 = st.columns(2)

with col1:
    source_language = st.selectbox(
        "Translate from", list(languages.keys())
    )

with col2:
    target_language = st.selectbox(
        "Translate to", list(languages.keys()), index=1
    )

input_text = st.text_area(
    "Enter text to translate",
    placeholder="Type your text here...",
    height=150
)

if st.button("🌐 Translate", use_container_width=True):

    if not input_text.strip():
        st.warning("Please enter some text to translate.")

    elif source_language == target_language:
        st.warning("Please select two different languages.")

    else:
        try:
            translator = MyMemoryTranslator(
                source=languages[source_language],
                target=languages[target_language]
            )

            translated_text = translator.translate(text)

            st.subheader("Translated Text")

            st.text_area(
                "Translation result",
                value=translated_text,
                height=150
            )

            st.success("Translation completed successfully!")

        except Exception as error:
            st.error("Translation failed. Please try again later.")
            st.caption(f"Error details: {error}")