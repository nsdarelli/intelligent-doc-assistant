from pathlib import Path

class DocumentService:
    def __init__(self, vector_service):
        self.vector_service = vector_service

    def list_documents(self):
        metadatas = self.vector_service.get_all_documents()

        documents = {}
        for metadata in metadatas:
            source = metadata["source"]
            documents[source] = documents.get(source, 0) + 1

        return [{
            "source": source,
            "chunk": count
        }
        for source, count in documents.items()
        ]
    
    def delete_document(self, source):
        self.vector_service.delete_doc(source)

        file_path = Path(f"data/raw/{source}")

        if file_path.exists():
            file_path.unlink()

        return {
            "status": "success",
            "source": source
        }