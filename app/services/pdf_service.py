from pypdf import PdfReader

class PDFService:

    @staticmethod
    def extract_text_pdf(pdf_path: str) -> str:
        reader = PdfReader(pdf_path)
        if reader.is_encrypted:
            print(f"PDF {pdf_path} is encrypted. Skipping.")
            return ""
        
        text = ""

        for page in reader.pages:
            text_page = page.extract_text()

            if text_page:
                text += text_page + "\n"
                
        return text
