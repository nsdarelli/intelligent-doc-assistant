from pathlib import Path
import uuid
from app.services.hash_service import HashService
from app.loaders.loader_factory import LoaderFactory
from app.core.logger import logger
from app.core.exceptions import DuplicateDocumentException

class IngestionService:

    def __init__(self, chunk_service, embedding_service, vector_service):
        self.chunk_service = chunk_service
        self.embedding_service = embedding_service
        self.vector_service = vector_service

    def ingest_document(self, file_path):
        file_name = Path(file_path).name
        logger.info(f"Staring ingestion for {file_name}")
        loader = LoaderFactory.get_loader(file_path)
        pages = loader.extract_text(file_path)
        chunks = self.chunk_service.create_chunks(pages, source_file=file_name)
        logger.info(f"Created {len(chunks)} chunks")
        document_hash = HashService.calculate_file_hash(file_path=file_path)
        if self.vector_service.document_exists(document_hash):
            logger.info(f"DUPLICATE DOCUMENT FOUND {file_name}")
            raise DuplicateDocumentException(
                f"{file_name} already exists"
            )
        texts = [chunk.page_content for chunk in chunks]
        embeddings = self.embedding_service.embed_documents(texts)
        logger.info(f"Generated {len(embeddings)}")
        ids = [str(uuid.uuid4()) for _ in range(len(texts))]
        self.vector_service.add_documents(ids=ids, chunks=chunks, document_hash=document_hash, embeddings=embeddings, file_path=file_path)
        print(f"processing: {file_name}")
        print(f"Pages: {len(pages)}")
        print(f"Chunks: {len(chunks)}")

        return {
            "status": "success",
            "file_name": file_name,
            "pages": len(pages),
            "chunks": len(chunks)
        }

