from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
import os 

pdf_path="sample.pdf"

loader=PyPDFLoader(pdf_path)
pages=loader.load()

print(f"Total pages loaded:{len(pages)}")

text_splitter=RecursiveCharacterTextSplitter(
  chunk_size=500,
  chunk_overlap=50
)

chunks = text_splitter.split_documents(pages)

print(f"Total chunks created:{len(pages)}")
print("\n First chunk:\n")
print(chunks[0].page_content)
print("Loading embedding model...")
embedding_model=HuggingFaceEmbeddings(model_name="all-all-MiniLM-L6-v2")
print("Creating vector store...")
vectorstore=FAISS.from_documents(chunks,embedding_model)
vectorstore.save_local("faiss_store")
print("Embeddings stored in 'faiss_Store'folder")