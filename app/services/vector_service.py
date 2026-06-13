import chromadb

class VectorService:

    def __init__(self):
        self.client = chromadb.PersistentClient(path="storage/chroma")
        self.collection = self.client.get_or_create_collection(name="documents") # Create or get the collection named "documents"
    
    # Add documents to the collection with their corresponding embeddings
    def add_documents(self, ids, documents, embeddings, metadatas=None):
        self.collection.add(ids=ids, documents=documents, embeddings=embeddings.tolist(), metadatas=metadatas)

    def search(self, query_embedding, top_k=3):
        return self.collection.query(query_embeddings=[query_embedding.tolist()], n_results=top_k, include=["documents", "metadatas", "distances"])
    
    def retrieve_context(self, query_embedding, top_k=3):
        results = self.search(query_embedding, top_k)
        docs = results['documents'][0]  # Get the retrieved documents
        print(f"Retrieved {len(docs)} documents for the query. {"\n".join(docs)}")  # Print the retrieved documents
        print(f"distances: {results['distances'][0]}")  # Print the distances of the retrieved documents
        return {
            "documents": "\n\n".join(docs),
            "sources": results['metadatas'][0],  # Get the metadata of the retrieved documents
            "distances": results['distances'][0]  # Get the distances of the retrieved documents
        }
