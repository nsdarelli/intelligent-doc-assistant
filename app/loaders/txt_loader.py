from app.loaders.base_loader import BaseLoader
from langchain_core.documents import Document

class TXTLoader(BaseLoader):

    def extract_text(self, file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        return [Document(
            page_content=text,
            metadata={"source": file_path}
        )]