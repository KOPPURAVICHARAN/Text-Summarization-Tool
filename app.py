
import streamlit as st
from summarizer import summarize_text
from docx import Document
import fitz 
import mimetypes

st.title("Text Summarization Tool")
uploaded_file = st.file_uploader("Upload any file containing text")
input_text = ""

def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    return "\n".join(page.get_text() for page in doc)
def extract_text_from_docx(file):
    doc = Document(file)
    return "\n".join([para.text for para in doc.paragraphs])
def try_decode_text(file):
    try:
        return file.read().decode("utf-8")
    except:
        file.seek(0)
        try:
            return file.read().decode("latin-1")
        except:
            return None
if uploaded_file is not None:
    try:
        file_ext = uploaded_file.name.split(".")[-1].lower()
        mime_type, _ = mimetypes.guess_type(uploaded_file.name)
        if file_ext == "pdf":
            input_text = extract_text_from_pdf(uploaded_file)
        elif file_ext == "docx":
            input_text = extract_text_from_docx(uploaded_file)
        else:
            input_text = try_decode_text(uploaded_file)
        if not input_text:
            st.error("⚠️ Could not extract text from this file.")
    except Exception as e:
        st.error(f"❌ Error reading file: {str(e)}")
else:
    input_text = st.text_area("Paste your text here")
if st.button("Summarize"):
    if input_text.strip():
        summary = summarize_text(input_text)
        st.subheader("Summary")
        st.text_area("Editable Summary", summary, height=300)
    else:
        st.warning("Please upload or paste some text.")
