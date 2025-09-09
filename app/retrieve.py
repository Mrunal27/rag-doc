def retrieve(query, vector_store):
    return vector_store.similarity_search(query, k=3)