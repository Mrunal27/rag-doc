# 🧠 RAG Doc QA Pipeline

A modular Retrieval-Augmented Generation (RAG) system built with FastAPI, Docker, and LangChain. Upload a document, ask a question, and get validated answers powered by OpenAI.

---

## 🚀 Features

- 📄 PDF ingestion and chunking
- 🔍 Semantic search with FAISS
- 🤖 Answer generation via OpenAI LLM
- ✅ Output validation to detect hallucinations
- 🐳 Dockerized for reproducible deployment
- 🔧 Modular codebase for easy extension

---

## 🧱 Tech Stack

| Layer            | Tools Used                          |
|------------------|-------------------------------------|
| API              | FastAPI, Uvicorn                    |
| Embeddings       | LangChain + OpenAIEmbeddings        |
| Vector Store     | FAISS                               |
| Orchestration    | Docker                              |
| Validation       | Custom logic (length, context match)|
| PDF Parsing      | PyPDF2                              |

---

## 📦 Setup Instructions

1. Clone the Repo
```bash
git clone https://github.com/Mrunal27/rag-doc.git
cd rag-doc

2. Create .env File
```bash
touch .env
### Add your OPENAI API KEY
```bash
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

3. Build and Run with Docker
```bash
docker build -t rag-doc .
docker run -p 8000:8000 rag-doc

4. Test via Swagger UI
Visit
```bash
http://localhost:8000/docs

Upload a PDF and ask a question.

