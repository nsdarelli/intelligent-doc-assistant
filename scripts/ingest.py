import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))


from app.services.chunk_service import ChunkService
from app.services.embedding_service import EmbeddingService
from app.services.vector_service import VectorService
import os

source_file = os.path.basename("data/raw/banking.pdf")

pages = PDFService.extract_text_pdf("data/raw/banking.pdf")

chunks = ChunkService.create_chunks(pages, source_file=source_file)

texts = [chunk.page_content for chunk in chunks]
metadatas = [chunk.metadata for chunk in chunks]
print(f"length of texts: {len(texts)}")
print(f"length of metadatas: {len(metadatas)}")
print(f"Sample metadata: {metadatas[:5]}")  # Print the first metadata for verification

embedding_service = EmbeddingService()
embeddings = embedding_service.embed_documents(texts)

vector_service = VectorService()
vector_service.add_documents(ids=[str(i) for i in range(len(texts))], chunks=chunks, embeddings=embeddings, metadatas=metadatas)

sample = vector_service.collection.get()

if sample is None or not sample.get("documents"):
    print("Warning: No documents found in collection")
else:
    print("Documents:", len(sample["documents"]))
    print("Metadatas:", len(sample["metadatas"]))
    print(sample["metadatas"][:5])
    print("Ingestion complete!")

print("Ingestion complete!")