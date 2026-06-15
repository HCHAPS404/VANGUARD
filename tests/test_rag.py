import os
import pytest
from core.rag.extractor import DocumentExtractor
from core.rag.embeddings import ChromaManager

def test_document_extractor():
    pdf_path = "tests/documents/aws_privacy_policy.pdf"
    assert os.path.exists(pdf_path), "Sample PDF must exist"
    
    extractor = DocumentExtractor(pdf_path)
    text = extractor.extract_text()
    
    assert "AWS Privacy Policy" in text
    
    doc_hash = extractor.get_hash()
    assert len(doc_hash) == 64  # SHA256 length
    
    chunks = extractor.extract_chunks(chunk_size=10)
    assert len(chunks) > 1

def test_chroma_manager():
    # Use memory client for tests
    manager = ChromaManager(persist_dir=":memory:", collection_name="test_col")
    
    doc_id = "test-doc-1"
    chunks = ["Data is collected.", "Data is used for services.", "Data is secure."]
    
    manager.add_chunks(doc_id, chunks)
    
    results = manager.query("Is data safe?", n_results=1)
    assert len(results) == 1
    assert "secure" in results[0].lower()
