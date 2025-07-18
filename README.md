# 🧠 AI-Powered Plagiarism Checker

This is a **Streamlit-based web app** that compares two documents and detects sentence-level plagiarism using **Sentence Transformers (MiniLM model)**. It's a lightweight, intelligent plagiarism checker built for internship evaluation and practical use.

---

## 🚀 Features

✅ Upload `.txt`, `.pdf`, or `.docx` files  
🧠 AI model: `paraphrase-MiniLM-L6-v2`  
🔍 Sentence-level similarity detection  
📊 Adjustable similarity threshold (0.5 to 0.95)  
📈 Plagiarism percentage estimation  
📥 CSV download of detected matches  
⚡ Fast and lightweight, perfect for local or cloud use  

---

## 📂 File Structure

plagiarism-checker-ai/
│
├── pc.py # Main Streamlit app code
├── requirements.txt # Required Python libraries
├── README.md # This file
└── similarity_results.csv # (Generated) CSV output of results

yaml
Copy
Edit

---

## ⚙️ Installation & Running

### 📌 Step 1: Clone the repository

git clone https://github.com/DhivyadharshiniCoder/plagiarism-checker-ai.git
cd plagiarism-checker-ai

shell
Copy
Edit

### 📌 Step 2: Install dependencies

pip install -r requirements.txt

shell
Copy
Edit

### 📌 Step 3: Run the app

streamlit run pc.py

yaml
Copy
Edit

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🧾 Requirements

- Python 3.7 or higher  
- `sentence-transformers`  
- `streamlit`  
- `PyPDF2`  
- `python-docx`  
- `pandas`  

✔️ All dependencies are listed in `requirements.txt`

---

## 📊 Output

- Matching sentence pairs displayed in a table  
- Similarity score (0 to 1) shown for each match  
- Plagiarism percentage calculated based on sentence overlap  
- Downloadable CSV includes:
  - `Sentence_File1`
  - `Sentence_File2`
  - `Similarity_Score`

---

## 🛠️ Credits

- **Model**: `paraphrase-MiniLM-L6-v2`  
- **UI**: Streamlit  
- **Author**: [DhivyadharshiniCoder](https://github.com/DhivyadharshiniCoder)

---

## 📬 Contact

📧 Email: dhivyadharshan0505@gmail.com  
👤 GitHub: [DhivyadharshiniCoder](https://github.com/DhivyadharshiniCoder)
