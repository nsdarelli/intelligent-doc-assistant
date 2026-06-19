from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from app.core.config import settings


class ChunkService:

    @staticmethod
    def create_chunks(documents, source_file):

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.CHUNK_SIZE,
            chunk_overlap=settings.CHUNK_OVERLAP
        )

        all_chunks = []
        chunk_counter = 1

        for doc in documents:

            page_text = doc.page_content

            page_number = doc.metadata.get(
                "page",
                0
            )

            page_chunks = splitter.split_text(
                page_text
            )

            for chunk in page_chunks:

                all_chunks.append(
                    Document(
                        page_content=chunk,
                        metadata={
                            "source": source_file,
                            "page_number": page_number,
                            "chunk_id": chunk_counter
                        }
                    )
                )

                chunk_counter += 1
        print(f"All Chunks: {all_chunks}")
        return all_chunks