import streamlit as st
from sentence_transformers import SentenceTransformer, util
import pandas as pd
import re
import io
from PyPDF2 import PdfReader
import docx

# Load model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Function to extract text from uploaded file
def extract_text(uploaded_file):
    if uploaded_file.type == "text/plain":
        return str(uploaded_file.read(), "utf-8")
    elif uploaded_file.type == "application/pdf":
        pdf = PdfReader(uploaded_file)
        return " ".join(page.extract_text() for page in pdf.pages if page.extract_text())
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = docx.Document(uploaded_file)
        return " ".join(paragraph.text for paragraph in doc.paragraphs)
    else:
        return ""

# Function to split text into sentences
def get_sentences(text):
    sentences = re.split(r'(?<=[.!?]) +', text.strip())
    return [s for s in sentences if len(s.strip()) > 0]

# Compute similarity between two texts
def compute_similarity(text1, text2, threshold):
    sent1 = get_sentences(text1)
    sent2 = get_sentences(text2)
    emb1 = model.encode(sent1, convert_to_tensor=True)
    emb2 = model.encode(sent2, convert_to_tensor=True)
    cosine_scores = util.pytorch_cos_sim(emb1, emb2)
    matches = []
    for i in range(len(sent1)):
        for j in range(len(sent2)):
            score = cosine_scores[i][j].item()
            if score >= threshold:
                matches.append((sent1[i], sent2[j], round(score, 3)))
    return matches

# Streamlit App
st.set_page_config(page_title="Plagiarism Checker AI", layout="centered")
st.title("🧠 AI-Powered Plagiarism Checker")
st.markdown("Upload two documents and detect similarities using sentence embeddings.")

file1 = st.file_uploader("📄 Upload File 1", type=["txt", "pdf", "docx"])
file2 = st.file_uploader("📄 Upload File 2", type=["txt", "pdf", "docx"])

threshold = st.slider("🔍 Similarity Threshold", min_value=0.5, max_value=0.95, step=0.05, value=0.75)

if st.button("🚀 Run Checker") and file1 and file2:
    with st.spinner("Comparing documents..."):
        text1 = extract_text(file1)
        text2 = extract_text(file2)
        matches = compute_similarity(text1, text2, threshold)

    if matches:
        st.success(f"Found {len(matches)} matching sentence pairs.")
        df = pd.DataFrame(matches, columns=["Sentence_File1", "Sentence_File2", "Similarity_Score"])
        st.dataframe(df)

        # Plagiarism percentage
        plag_percent = (len(matches) / max(len(get_sentences(text1)), 1)) * 100
        st.markdown(f"### 📊 Estimated Plagiarism: `{plag_percent:.2f}%`")

        # Download CSV
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Results CSV", csv, "similarity_results.csv", "text/csv")
    else:
        st.success("✅ No significant plagiarism detected.")

st.markdown("---")
st.caption("Developed for Internship Plagiarism Checker Project | Model: MiniLM-L6-v2")
