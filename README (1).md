
# 🤖 AI-Powered Resume Checker

A cutting-edge Generative AI project that allows users to upload a **resume or job description** PDF and ask natural language questions about its content. It leverages **LangChain**, **FAISS**, and a **local LLM (Mistral via Ollama)** using the **RAG (Retrieval-Augmented Generation)** approach. The project includes a user-friendly **Streamlit** frontend for seamless interaction.

---

## 📌 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Architecture](#-architecture)
- [Installation](#-installation)
- [Usage](#-usage)
- [Example Questions](#-example-questions)
- [Screenshots](#-screenshots)
- [Folder Structure](#-folder-structure)
- [Future Improvements](#-future-improvements)
- [Author](#-author)


---

## 🚀 Features

- 📄 Upload resume or job description in PDF format
- 🧠 Ask questions like “What skills does the candidate have?” or “Is this suitable for a data analyst role?”
- 💬 Answers generated using **local LLM** (Mistral) via **Ollama**
- 🔍 Uses **FAISS vector store** for semantic chunk retrieval
- 📚 Supports **RAG pipeline** with LangChain
- 🖥️ Streamlit interface for real-time interaction
- 🛡️ Fully local — **no OpenAI key required**
- ⚙️ Modular code structure (chunking, embedding, querying, app)

---

## 🧠 Tech Stack

- **LangChain** – for chaining LLMs with retrievers
- **LangChain Community Modules** – loaders like `PyPDFLoader`, Ollama, FAISS
- **FAISS** – fast vector similarity search
- **HuggingFace Sentence Transformers** – to embed documents
- **Streamlit** – frontend UI
- **Ollama** – to run Mistral LLM locally
- **Python** – primary language

---

## 🏗️ Architecture

```text
PDF Upload
   │
   ▼
Chunking (LangChain Splitters)
   │
   ▼
Embedding (Sentence Transformers)
   │
   ▼
Store in FAISS Vector DB
   │
   ▼
User Query ─► Retriever ─► Mistral (via Ollama)
                   │
                   ▼
              Final Answer
```

---

## ⚙️ Installation

### 1. Clone this repository
```bash
git clone https://github.com/Suryaprakash-Techky/ai-powered-resume-checker.git
cd ai-powered-resume-checker
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate 

```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Install and run Ollama
Download from: https://ollama.com  
Then run:
ollama run mistral
```

---

## ▶️ Usage

Run the app using:

```bash
streamlit run app.py
```

Then upload your PDF, enter a question, and get instant answers!

---

## ❓ Example Questions

- What skills are mentioned?
- Is the candidate suitable for a data scientist role?
- What experience does the person have?
- Does the resume match a data analyst JD?

---

## 📁 Folder Structure

```text
ai-powered-resume-checker/
│
├── app.py                    # Streamlit app
├── embed_chunks.py          # Converts PDF chunks to embeddings
├── load_and_chunk.py        # Loads and splits PDF
├── rag_qa_local_llm.py      # CLI interface for QA
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
├── .gitignore
└── faiss_store/             # Vector DB files (auto generated)
```

---

## 🌱 Future Improvements

- Upload multiple PDFs at once
- Add login + user history
- Score resume match to job description
- Add support for other LLMs (like LLaMA3, Phi-3)
- Currenlty Building an app 

---

## 👨‍💻 Author

**Suryaprakash A**  
📧 [suryaprakash_193@yahoo.com](mailto:suryaprakash_193@yahoo.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/suryaprakash-anandbabu-b9a0b1266/)

---


