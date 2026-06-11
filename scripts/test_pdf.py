from app.services.pdf_service import PDFService

text = PDFService.extract_text_pdf("data/raw/banking.pdf")

print(text[:500])  # Print the first 500 characters of the extracted text