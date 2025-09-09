from langchain_community.vectorstores import FAISS

def store_embeddings(chunks, embeddings):
    return FAISS.from_texts(chunks, OpenAIEmbeddings())