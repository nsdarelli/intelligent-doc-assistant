from app.services.embedding_service import EmbeddingService
from app.services.vector_service import VectorService
from app.services.llm_service import LLMService
from app.services.chunk_service import ChunkService

from app.services.ingestion_service import IngestionService
from app.services.document_service import DocumentService


chunk_service = ChunkService()

embedding_service = EmbeddingService()

vector_service = VectorService()

llm_service = LLMService()

ingestion_service = IngestionService(chunk_service=chunk_service, embedding_service=embedding_service, vector_service=vector_service)
document_service = DocumentService(vector_service=vector_service)
