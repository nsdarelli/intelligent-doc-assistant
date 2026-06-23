import chromadb
from app.core.config import settings
from app.core.exceptions import DocNotFoundError

class VectorService:

    def __init__(self):
        self.client = chromadb.PersistentClient(path=settings.CHROMA_PATH)
        self.collection = self.client.get_or_create_collection(name=settings.COLLECTION_NAME) # Create or get the collection named "documents"
    
    # Add documents to the collection with their corresponding embeddings
    def add_documents(self, ids, chunks, document_hash, embeddings, file_path):
        metadatas = []

        for chunk in chunks:
            metadata = dict(chunk.metadata)

            metadata["document_hash"] = document_hash

            metadatas.append(metadata)
        
        documents = [chunk.page_content for chunk in chunks]

        self.collection.add(ids=ids, documents=documents, embeddings=embeddings, metadatas=metadatas)

    def search(self, query_embedding, top_k=3):
        return self.collection.query(query_embeddings=[query_embedding], n_results=top_k, include=["documents", "metadatas", "distances"])
    
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

    def get_all_documents(self):
        result = self.collection.get(include=["metadatas"])

        return result["metadatas"]

    def document_exists(self, document_hash: str) -> bool:
        result = self.collection.get(where={"document_hash": document_hash})

        return len(result["ids"])>0
    
    def delete_doc(self, source):
        results = self.collection.get(where={"source": source})
        ids = results.get("ids", [])
        if not ids:
            raise DocNotFoundError(f"Document {source} not found in vector store")
        self.collection.delete(ids=ids)