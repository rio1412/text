import streamlit as st
from convert import process_text
import subprocess

# spaCyモデルの存在を確認し、なければダウンロードする関数
def download_spacy_model():
    try:
        # spaCyのja_core_news_smモデルが存在しない場合、ダウンロードする
        subprocess.run(['python', '-m', 'spacy', 'download', 'ja_core_news_sm'])
        return 'spaCy Model Downloaded Successfully!'
    except Exception as e:
        return f'Error: {str(e)}'

# spaCyモデルの存在を確認し、なければダウンロードを試みる
result = download_spacy_model()
st.write(result)


# Load the HTML template
html_template = open("index.html", "r", encoding="utf-8").read()

# Define Streamlit app
st.title("Japanese Text Conversion App")
text_input = st.text_input("Enter Japanese text:")
if st.button("Convert"):
    processed_text = process_text(text_input)
    st.markdown(html_template, unsafe_allow_html=True)
