from app.services.pdf_service import PDFService
from app.services.chunk_service import ChunkService

text = PDFService.extract_text_pdf("data/raw/banking.pdf")
chunks = ChunkService.create_chunks(text)

print(f"Total Chunks created: {len(chunks)}")

for i, chunk in enumerate(chunks[:10]):
    print(f"\nChunk {i+1}")
    print(f"-"* 20)

    print(chunk.page_content)
    print("\nMetadata:")
    print(chunk.metadata)
