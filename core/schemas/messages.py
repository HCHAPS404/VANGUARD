from typing import Dict, Any, Optional
from pydantic import BaseModel, Field

class IngestMessage(BaseModel):
    """
    Message published by INTAKE agent after successfully ingesting a document.
    Signals Phase A agents to start their analysis.
    """
    document_id: str = Field(..., description="Unique identifier for the processed document")
    content_hash: str = Field(..., description="SHA-256 hash of the extracted document content")
    chunk_count: int = Field(..., description="Number of chunks the document was split into")
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Additional document metadata (e.g., filename, author)")
