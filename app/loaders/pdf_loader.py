from langchain_community.document_loaders import PyPDFLoader
from app.loaders.base_loader import BaseLoader

class PDFLoader(BaseLoader):

    def extract_text(self, file_path):
        loader = PyPDFLoader(file_path)

        return loader.load()