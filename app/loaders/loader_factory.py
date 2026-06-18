from app.loaders.pdf_loader import PDFLoader
from app.loaders.docx_loader import DOCXLoader
from app.loaders.txt_loader import TXTLoader
from app.core.exceptions import UnsupportedFileTypeException

from pathlib import Path

class LoaderFactory:
    loaders = {
        ".pdf" : PDFLoader(),
        ".docx": DOCXLoader(),
        ".txt": TXTLoader()
    }

    @classmethod
    def get_loader(cls, file_path: str):
        extension = Path(file_path).suffix.lower()
        loader = cls.loaders.get(extension)

        if not loader:
            raise UnsupportedFileTypeException(
                f"Unsupported file type: {extension}"
            )
        
        return loader