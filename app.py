import streamlit as st
import nltk

_default_text = """Punkt knows that the periods in Mr. Smith and Johann S. 
Bach do not mark sentence boundaries.  And sometimes sentences can start with 
non-capitalized words.  i is a good variable name."""

st.title("NLTK example")
"Example from https://www.nltk.org/api/nltk.tokenize.punkt.html"

text = st.text_area("Insert text to tokenize", value=_default_text)

try:
    sent_detector = nltk.tokenize.PunktTokenizer()

except LookupError:
    nltk.download("punkt_tab")
    st.rerun()

processed = sent_detector.tokenize(text.strip())

st.header("Tokens:")
for i, line in enumerate(processed, 1):
    st.subheader(i, divider="blue")
    st.write(line)
