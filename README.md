# Local AI Knowledge Assistant

Offline Retrieval-Augmented Generation (RAG) assistant built using LangChain and Ollama.

## Overview
A privacy-focused AI assistant that answers questions from user-provided data without internet dependency.

## Features
- Webpage ingestion
- Text chunking and embeddings
- Vector similarity search
- Local LLM integration via Ollama
- Streamlit-based user interface

## Tech Stack
- Python
- LangChain
- ChromaDB
- Ollama
- Streamlit

## How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
## Demo

Here’s how the assistant behaves:

1. User enters text or URL  
2. System chunks and embeds it  
3. Retriever finds context  
4. Local LLM answers the query
