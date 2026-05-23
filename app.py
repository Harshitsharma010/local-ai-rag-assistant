import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

st.title("Chat with Webpage")
st.caption("This app allows you to chat with a webpage using a local Ollama model and RAG.")

webpage_url = st.text_input("Enter Webpage URL", type="default")

ollama_endpoint = "http://127.0.0.1:11434"
ollama_model = "qwen2.5:1.5b"
ollama = ChatOllama(model=ollama_model, base_url=ollama_endpoint)

if webpage_url:
    loader = WebBaseLoader(webpage_url)
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=10)
    splits = text_splitter.split_documents(docs)

    embeddings = OllamaEmbeddings(model="nomic-embed-text", base_url=ollama_endpoint)
    vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)
    retriever = vectorstore.as_retriever()

    def ollama_llm(question, context):
        """Generate an answer using the configured local Ollama model."""
        formatted_prompt = f"Question: {question}\n\nContext: {context}"
        response = ollama.invoke([("human", formatted_prompt)])
        return response.content.strip()

    def combine_docs(docs):
        """Combine retrieved document chunks into a single context string."""
        return "\n\n".join(doc.page_content for doc in docs)

    def rag_chain(question):
        """Retrieve relevant context and generate an answer."""
        retrieved_docs = retriever.invoke(question)
        formatted_context = combine_docs(retrieved_docs)
        return ollama_llm(question, formatted_context)

    st.success(f"Loaded {webpage_url} successfully.")

    prompt = st.text_input("Ask any question about the webpage")

    if prompt:
        result = rag_chain(prompt)
        st.write(result)
