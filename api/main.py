from fastapi import FastAPI, UploadFile
from app.ingest import load_pdf, chunk_text
from app.embed import get_embeddings
from app.store import store_embeddings
from app.retrieve import retrieve
from app.generate import generate_answer
from app.validate import validate_output

app = FastAPI()

@app.post("/query")
async def query_doc(file: UploadFile, question: str):
    text = load_pdf(file.file)
    chunks = chunk_text(text)
    embeddings = get_embeddings(chunks)
    store = store_embeddings(chunks, embeddings)
    context_chunks = retrieve(question, store)
    context = "\n".join([chunk.page_content for chunk in context_chunks])
    answer = generate_answer(context, question)
    validation = validate_output(answer, context)
    return {"answer": answer, "validation":validation}
