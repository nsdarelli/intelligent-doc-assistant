from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

class ChunkService:

    @staticmethod
    def create_chunks(pages, source_file):
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

        all_chunks = []

        chunk_counter = 1

        for page_data in pages:
            page_text = page_data["text"]
            page_number = page_data["page_number"]

            page_chunks = splitter.split_text(page_text)

            for chunk in page_chunks:
                all_chunks.append(
                    Document(
                        page_content=chunk,
                        metadata={
                            "source": str(source_file),
                            "page_number": int(str(page_number)),
                            "chunk_id": int(str(chunk_counter))
                        }
                    )
                )
                chunk_counter += 1
        print(f"Chunks: {all_chunks[:3]}")  # Print the first 3 chunks for verification
        return all_chunks