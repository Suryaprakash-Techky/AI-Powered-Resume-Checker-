from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import Ollama


print("⏳ Loading vector store...")
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = FAISS.load_local("faiss_store", embedding_model, allow_dangerous_deserialization=True)

retriever = vectorstore.as_retriever()


print("⏳ Loading Mistral model from Ollama...")
llm = Ollama(model="mistral")


qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)

print("🤖 You can now ask questions from your PDF!")
while True:
    query = input("📝 Ask a question (or type 'exit'): ")
    if query.lower() == "exit":
        break
    response = qa_chain({"query": query})
    print("\n💡 Answer:\n", response["result"])
