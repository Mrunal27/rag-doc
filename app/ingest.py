from PyPDF2 import PdfReader

def load_pdf(path):
    reader = PdfReader(path)
    return "\n".join([page.extract_text() for page in reader.pages])

def chunk_text(text, chunk_size=500):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
