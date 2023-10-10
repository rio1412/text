import streamlit as st
from convert import process_text

# Load the HTML template
html_template = open("index.html", "r", encoding="utf-8").read()

# Define Streamlit app
st.title("Japanese Text Conversion App")
text_input = st.text_input("Enter Japanese text:")
if st.button("Convert"):
    processed_text = process_text(text_input)
    st.markdown(html_template, unsafe_allow_html=True)
