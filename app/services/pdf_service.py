from pypdf import PdfReader

class PDFService:

    @staticmethod
    def extract_text_pdf(pdf_path: str) -> str:
        reader = PdfReader(pdf_path)
        if reader.is_encrypted:
            print(f"PDF {pdf_path} is encrypted. Skipping.")
            return ""
        
        pages = []

        for page_num, page in enumerate(reader.pages):
            pages.append({
                "text": page.extract_text(),
                "page_number": page_num + 1
            })

        return pages