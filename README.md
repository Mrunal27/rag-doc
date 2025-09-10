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

⚙️ Setup Instructions
1. Clone the Repository
git clone https://github.com/Mrunal27/rag-doc.git
cd rag-doc


2. Create Environment File
Create a .env file to securely store your OpenAI API key:
touch .env


Add the following line to .env:
OPENAI_API_KEY="API_KEY"

3. Build and Run the Docker Container
docker build -t rag-doc .
docker run -p 8000:8000 rag-doc

4. Access the Swagger UI
Visit http://localhost:8000/docs to interact with the API.

5. Test the RAG Pipeline
- Upload a PDF document via the Swagger interface
- Ask a question based on the document content
- Receive a context-aware response powered by OpenAI

---
_#RetrievalAugmentedGeneration #GenerativeAI #BackendEngineering #MLPlatform #CareerPivot #OpenToWork_
