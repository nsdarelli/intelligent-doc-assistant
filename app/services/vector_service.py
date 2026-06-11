import chromadb

class VectorService:

    def __init__(self):
        self.client = chromadb.PersistentClient(path="storage/chroma")
        self.collection = self.client.get_or_create_collection(name="documents") # Create or get the collection named "documents"
    
    # Add documents to the collection with their corresponding embeddings
    def add_documents(self, ids, documents, embeddings):
        self.collection.add(ids=ids, documents=documents, embeddings=embeddings.tolist())

    def search(self, query_embedding, top_k=3):
        return self.collection.query(query_embeddings=[query_embedding.tolist()], n_results=top_k)

    