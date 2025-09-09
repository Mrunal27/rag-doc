from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
print(f"Loaded API key: {openai_api_key}")

from langchain_community.embeddings import OpenAIEmbeddings

def get_embeddings(chunks):
    embedder = OpenAIEmbeddings(openai_api_key=openai_api_key)
    return embedder.embed_documents(chunks)