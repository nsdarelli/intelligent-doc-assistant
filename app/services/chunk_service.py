from langchain_text_splitters import RecursiveCharacterTextSplitter

class ChunkService:

    @staticmethod
    def create_chunks(text: str):
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

        chunks = splitter.create_documents([text], metadatas=[{"source": "banking.pdf"}])

        return chunks