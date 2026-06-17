from pathlib import Path
import uuid

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
        texts = [chunk.page_content for chunk in chunks]
        metadatas = [chunk.metadata for chunk in chunks]
        embeddings = self.embedding_service.embed_documents(texts)
        ids = [str(uuid.uuid4()) for _ in range(len(texts))]
        self.vector_service.add_documents(ids=ids, documents=texts, metadatas=metadatas, embeddings=embeddings)
        print(f"processing: {file_name}")
        print(f"Pages: {len(pages)}")
        print(f"Chunks: {len(chunks)}")

        return {
            "status": "success",
            "file_name": file_name,
            "pages": len(pages),
            "chunks": len(chunks)
        }

