import streamlit as st
import nltk


def main():
    st.set_page_config(
        page_title="NLTK example in Streamlit · edsaac.me",
        page_icon=":speech_balloon:",
        menu_items={
            "About": "https://edsaac.me",
            "Report a Bug": "https://github.com/edsaac/st-nltk/issues",
        },
    )

    _default_text = """Punkt knows that the periods in Mr. Smith and Johann S. 
    Bach do not mark sentence boundaries.  And sometimes sentences can start with 
    non-capitalized words.  i is a good variable name."""

    st.title("NLTK in Streamlit")
    "Example from https://www.nltk.org/api/nltk.tokenize.punkt.html"

    with st.expander("Make sure to download NLTK packages", expanded=True):
        with st.echo():
            try:
                sent_detector = nltk.tokenize.PunktTokenizer()

            except LookupError:
                nltk.download("punkt_tab")
                st.rerun()

    st.divider()
    text = st.text_area("Insert text to tokenize", value=_default_text)
    processed = sent_detector.tokenize(text.strip())

    "**Tokens:**"
    for i, line in enumerate(processed, 1):
        st.write(f"**{i})** {line}")


if __name__ == "__main__":
    main()
