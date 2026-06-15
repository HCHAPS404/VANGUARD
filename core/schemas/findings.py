from enum import Enum
from pydantic import BaseModel, Field

class SeverityEnum(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"

class Finding(BaseModel):
    """
    A specific issue or insight discovered by a Phase A agent (LEXIS, SENTINEL, LEDGER).
    """
    id: str = Field(..., description="Unique identifier for the finding")
    agent_name: str = Field(..., description="Name of the agent that discovered the finding (e.g., LEXIS)")
    severity: SeverityEnum = Field(..., description="Risk severity level")
    claim: str = Field(..., description="The main assertion or identified risk")
    clause_ref: str = Field(..., description="Reference to the specific clause or section in the document")
    quote: str = Field(..., description="Exact quote from the document supporting the claim")
