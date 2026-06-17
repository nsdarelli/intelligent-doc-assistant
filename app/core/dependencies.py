from app.services.embedding_service import EmbeddingService
from app.services.vector_service import VectorService
from app.services.llm_service import LLMService
from app.services.pdf_service import PDFService
from app.services.chunk_service import ChunkService

from app.services.ingestion_service import IngestionService

pdf_service = PDFService()

chunk_service = ChunkService()

embedding_service = EmbeddingService()

vector_service = VectorService()

llm_service = LLMService()

ingestion_service = IngestionService(pdf_service=pdf_service, chunk_service=chunk_service, embedding_service=embedding_service, vector_service=vector_service)
