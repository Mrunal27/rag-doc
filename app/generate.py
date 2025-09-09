from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

from langchain_community.llms import OpenAI

def generate_answer(context, query):
    prompt = f"Context:\n{context}\n\nQuestion:{query}"
    llm = OpenAI(openai_api_key=openai_api_key)
    return llm(prompt)