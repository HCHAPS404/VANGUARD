import fitz
import hashlib
from typing import List

class DocumentExtractor:
    """
    Extracts text and metadata from PDF files using PyMuPDF.
    Handles chunking for RAG ingestion.
    """
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.doc = fitz.open(file_path)
        
    def extract_text(self) -> str:
        """Extracts full text from the PDF."""
        text = ""
        for page in self.doc:
            text += page.get_text()
        return text
        
    def get_hash(self) -> str:
        """Returns the SHA-256 hash of the document content."""
        text = self.extract_text()
        return hashlib.sha256(text.encode('utf-8')).hexdigest()
        
    def extract_chunks(self, chunk_size: int = 200) -> List[str]:
        """
        Splits the document text into chunks.
        MVP: Word-based simple chunking.
        """
        text = self.extract_text()
        words = text.split()
        chunks = []
        for i in range(0, len(words), chunk_size):
            chunks.append(" ".join(words[i:i + chunk_size]))
        return chunks
