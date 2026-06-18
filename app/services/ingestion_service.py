from pathlib import Path
import uuid
from app.services.hash_service import HashService

class IngestionService:

    def __init__(self, pdf_service, chunk_service, embedding_service, vector_service):
        self.pdf_service = pdf_service
        self.chunk_service = chunk_service
        self.embedding_service = embedding_service
        self.vector_service = vector_service

    def ingest_pdf(self, file_path):
        file_name = Path(file_path).name
        pages = self.pdf_service.extract_text_pdf(file_path)
        chunks = self.chunk_service.create_chunks(pages, source_file=file_name)
        document_hash = HashService.calculate_file_hash(file_path=file_path)
        if self.vector_service.document_exists(document_hash):
            print("DUPLICATE DOCUMENT FOUND")
            return {
                "status": "skipped",
                "file_name": file_name,
                "message": "Document already exists"
            }
        texts = [chunk.page_content for chunk in chunks]
        embeddings = self.embedding_service.embed_documents(texts)
        ids = [str(uuid.uuid4()) for _ in range(len(texts))]
        self.vector_service.add_documents(ids=ids, documents=texts, document_hash=document_hash, embeddings=embeddings, file_path=file_path)
        print(f"processing: {file_name}")
        print(f"Pages: {len(pages)}")
        print(f"Chunks: {len(chunks)}")

        return {
            "status": "success",
            "file_name": file_name,
            "pages": len(pages),
            "chunks": len(chunks)
        }

