import io
from PyPDF2 import PdfReader
import docx

def extract_text_from_file(filename, content_bytes):
    ext = filename.split('.')[-1].lower()

    if ext == "pdf":
        text = ""
        reader = PdfReader(io.BytesIO(content_bytes))
        for page in reader.pages:
            text += page.extract_text()
        return text

    elif ext == "docx":
        doc = docx.Document(io.BytesIO(content_bytes))
        return "\n".join([para.text for para in doc.paragraphs])

    elif ext == "txt":
        return content_bytes.decode("utf-8")

    else:
        return "Format de fișier neacceptat."
