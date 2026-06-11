from app.services.pdf_service import PDFService
from app.services.chunk_service import ChunkService
from app.services.embedding_service import EmbeddingService
from app.services.vector_service import VectorService

pdf_text = PDFService.extract_text_pdf("data/raw/banking.pdf")

chunks = ChunkService.create_chunks(pdf_text)

texts = [chunk.page_content for chunk in chunks]

embedding_service = EmbeddingService()
embeddings = embedding_service.embed_documents(texts)

vector_service = VectorService()
vector_service.add_documents(ids=[str(i) for i in range(len(texts))], documents=texts, embeddings=embeddings)

print("Ingestion complete!")