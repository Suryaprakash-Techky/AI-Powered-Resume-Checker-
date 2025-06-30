import streamlit as st
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import Ollama
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
import shutil

st.set_page_config(page_title="AI Powered Resume Checker💼", layout="wide")
st.title("📄 AI Powered Resume Checker")


uploaded_file = st.file_uploader("Upload your Resume or Job Description (PDF)", type=["pdf"])

if uploaded_file:
   
    with open("uploaded.pdf", "wb") as f:
        f.write(uploaded_file.read())

   
    loader = PyPDFLoader("uploaded.pdf")
    pages = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(pages)

    
    st.write("🔄 Generating embeddings...")
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    if os.path.exists("faiss_store"):
        shutil.rmtree("faiss_store")
    vectorstore = FAISS.from_documents(chunks, embedding_model)
    vectorstore.save_local("faiss_store")

   
    retriever = vectorstore.as_retriever()
    llm = Ollama(model="mistral")

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

 
    st.subheader("🧠 Ask a Question:")
    query = st.text_input("Type your question here")

    if query:
        response = qa_chain.invoke({"query": query})
        st.write("💡 **Answer:**", response["result"])
