import PyPDF2
import os

class PDFReader:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.text = ""
        self.page_count = 0
    
    def extract_text(self):
        if not os.path.exists(self.pdf_path):
            return False, "File not found"
        
        try:
            with open(self.pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                self.page_count = len(pdf_reader.pages)
                
                for page_num in range(self.page_count):
                    page = pdf_reader.pages[page_num]
                    self.text += page.extract_text() + "\n"
                
                if len(self.text.strip()) == 0:
                    return False, "No text found in PDF"
                
                return True, self.text[:5000]
        
        except Exception as e:
            return False, f"Error reading PDF: {str(e)}"
    
    def get_text_preview(self, max_chars=1000):
        if len(self.text) > max_chars:
            return self.text[:max_chars] + "..."
        return self.text