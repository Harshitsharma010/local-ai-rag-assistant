# Local AI RAG Assistant

**Privacy-first local webpage question-answering assistant using LangChain, ChromaDB, Ollama, embeddings, semantic search, and Streamlit.**

Local AI RAG Assistant demonstrates a practical Retrieval-Augmented Generation (RAG) workflow that runs against a local LLM through Ollama. The app loads webpage content, splits it into chunks, embeds the text, stores it in a Chroma vector store, retrieves relevant context, and generates context-aware answers through a Streamlit interface.

> **Project status**  
> This is a portfolio GenAI/RAG project focused on local-first question answering. The current implementation supports webpage ingestion. Document upload, persistent vector storage, authentication, and cloud deployment are planned improvements.

## Why This Project Matters

Many AI assistants depend on external cloud APIs, which can be a problem for private notes, internal documentation, research material, or sensitive learning resources. This project shows how a local RAG pipeline can answer questions from provided content while keeping the LLM runtime on the user's machine.

The project is relevant for AI Engineer, GenAI Engineer, Python Developer, Full Stack Developer, and Cloud Engineer internship roles because it connects:

- Retrieval-Augmented Generation
- LangChain orchestration
- ChromaDB vector search
- Ollama local LLM inference
- Embeddings and semantic search
- Streamlit application UI
- Python-based AI application development

## Key Features

| Feature | Description |
| --- | --- |
| Webpage ingestion | Loads webpage content from a user-provided URL |
| Text chunking | Splits content into smaller retrieval-friendly chunks |
| Embeddings | Creates local embeddings using Ollama embeddings |
| Vector search | Stores chunks in ChromaDB and retrieves relevant context |
| Local LLM response | Uses an Ollama-hosted model to generate answers |
| Streamlit UI | Provides a simple browser-based interface for querying content |
| Privacy-first workflow | Keeps LLM inference local instead of relying fully on external cloud APIs |

## Tech Stack

| Layer | Technology |
| --- | --- |
| Application | Python, Streamlit |
| RAG Framework | LangChain |
| Document Loader | LangChain `WebBaseLoader` |
| Text Splitting | `RecursiveCharacterTextSplitter` |
| Vector Store | ChromaDB |
| Embeddings | Ollama embeddings with `nomic-embed-text` |
| Local LLM | Ollama chat model, currently configured as `qwen2.5:1.5b` |

## RAG Architecture

```text
User enters webpage URL
  |
  v
Streamlit UI
  |
  v
LangChain WebBaseLoader
  |
  v
Raw webpage documents
  |
  v
RecursiveCharacterTextSplitter
  |
  v
Text chunks
  |
  v
Ollama Embeddings
  |
  v
ChromaDB Vector Store
  |
  v
Retriever
  |
  v
Relevant context
  |
  v
Ollama Local LLM
  |
  v
Context-aware answer
```

## How the RAG Pipeline Works

1. **Input:** The user enters a webpage URL in the Streamlit app.
2. **Loading:** `WebBaseLoader` loads the webpage content.
3. **Chunking:** `RecursiveCharacterTextSplitter` splits content into chunks of `500` characters with `10` characters overlap.
4. **Embedding:** Ollama embeddings convert each chunk into vector representations.
5. **Indexing:** ChromaDB stores the chunk vectors for semantic search.
6. **Retrieval:** The retriever finds chunks most relevant to the user's question.
7. **Prompting:** Retrieved context is combined with the user question.
8. **Generation:** The local Ollama model generates an answer from the retrieved context.

## Local Development Setup

### Prerequisites

- Python 3.10+
- Ollama installed and running locally
- Internet access for webpage loading

### 1. Clone the repository

```bash
git clone https://github.com/Harshitsharma010/local-ai-rag-assistant.git
cd local-ai-rag-assistant
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit app

```bash
streamlit run app.py
```

Streamlit will open the app in your browser.

## Ollama Setup

The current app expects Ollama to be available at:

```text
http://127.0.0.1:11434
```

Pull the local chat model:

```bash
ollama pull qwen2.5:1.5b
```

Pull the embedding model:

```bash
ollama pull nomic-embed-text
```

Confirm Ollama is running:

```bash
ollama list
```

## ChromaDB Vector Store

The app uses ChromaDB through LangChain:

```python
vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)
retriever = vectorstore.as_retriever()
```

In the current implementation, the vector store is created during the app session after a webpage is loaded. Persistent storage can be added later by configuring a Chroma persist directory.

## Environment Variables

No environment variables are required in the current version. The Ollama endpoint and model names are configured in `app.py`:

```python
ollama_endpoint = "http://127.0.0.1:11434"
ollama_model = "qwen2.5:1.5b"
```

Recommended future environment variables:

| Variable | Purpose |
| --- | --- |
| `OLLAMA_BASE_URL` | Configure local or remote Ollama endpoint |
| `OLLAMA_CHAT_MODEL` | Configure the chat model |
| `OLLAMA_EMBED_MODEL` | Configure the embedding model |
| `CHROMA_PERSIST_DIR` | Configure persistent vector storage |

## Project Structure

```text
local-ai-rag-assistant/
|-- app.py
|-- requirements.txt
`-- README.md
```

## Sample Usage

1. Start Ollama.
2. Run the Streamlit app.
3. Enter a webpage URL, for example:

```text
https://example.com/article
```

4. Wait for the page to load and embed.
5. Ask a question such as:

```text
What are the main ideas from this page?
```

6. The app retrieves relevant chunks and generates an answer using the local LLM.

Add a real sample after capturing output:

```text
[Add Sample Input]
[Add Sample Output]
```

## Screenshots / Demo Proof

Add proof here after capturing the working app.

| Proof | Status |
| --- | --- |
| Streamlit home screen | `[Add Screenshot]` |
| Webpage loaded successfully | `[Add Screenshot]` |
| Example question and answer | `[Add Screenshot]` |
| Ollama models installed | `[Add Screenshot]` |
| Short demo video | `[Add Demo Video]` |

Suggested file paths:

```text
docs/screenshots/home.png
docs/screenshots/webpage-loaded.png
docs/screenshots/question-answer.png
docs/screenshots/ollama-models.png
```

## Limitations

This project is intentionally scoped as a local RAG learning and portfolio project. The core workflow is implemented, but the following improvements would make it stronger:

- Current ingestion focuses on webpages, not uploaded PDFs or local files.
- Vector storage is session-based and not yet persisted between runs.
- Retrieval quality has not yet been measured with an evaluation set.
- The app does not yet show source citations for retrieved chunks.
- The UI does not include authentication or multi-user session handling.
- Cloud deployment requires additional planning because Ollama/local LLM inference depends on runtime resources.

## Future Improvements

| Area | Improvement |
| --- | --- |
| Retrieval | Add configurable `k`, chunk size, chunk overlap, and retrieval strategy |
| Evaluation | Add sample questions, expected answers, and retrieval quality checks |
| Citations | Show source chunks used for each answer |
| Persistence | Add persistent ChromaDB storage |
| Documents | Add PDF, TXT, Markdown, and DOCX upload support |
| API Layer | Add FastAPI backend for programmatic access |
| Auth | Add basic authentication for private deployments |
| Docker | Add Dockerfile and Docker Compose setup |
| Cloud | Explore deployment with a hosted app plus separately managed LLM runtime |
| Observability | Add logs for ingestion time, retrieval count, and response latency |

## License

This project is intended for educational, portfolio, and GenAI learning purposes.
