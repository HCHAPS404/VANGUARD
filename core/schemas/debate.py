from typing import List
from pydantic import BaseModel, Field

class DebateMessage(BaseModel):
    """
    Initiated by ARBITER when a contradiction is detected among findings.
    Mentions specific agents to request clarification.
    """
    id: str = Field(..., description="Unique identifier for the debate")
    finding_id: str = Field(..., description="ID of the finding that triggered the debate")
    contradiction_summary: str = Field(..., description="Summary of the contradiction found")
    target_agents: List[str] = Field(..., description="List of agent names mentioned (e.g., ['@LEXIS', '@SENTINEL'])")

class DebateResponse(BaseModel):
    """
    Response from a Phase A agent defending or clarifying a finding during a debate.
    """
    id: str = Field(..., description="Unique identifier for the response")
    debate_id: str = Field(..., description="ID of the debate being responded to")
    agent_name: str = Field(..., description="Agent providing the response")
    argument: str = Field(..., description="The defense or clarification argument")
    source_quote: str = Field(..., description="Supporting quote from the document or external source")

class RiskScore(BaseModel):
    """
    Published by ARBITER summarizing the overall risk of the document.
    """
    score: int = Field(..., ge=0, le=100, description="Overall risk score from 0 to 100")
    critical_findings_count: int = Field(..., ge=0, description="Number of critical findings")
    summary: str = Field(..., description="Executive summary of the risk assessment")

class ValidationResult(BaseModel):
    """
    Published by TRUTHLOCK to validate or invalidate a claim based on ground truth.
    """
    finding_id: str = Field(..., description="ID of the finding being validated")
    is_valid: bool = Field(..., description="True if the claim is supported by the document, False otherwise")
    reason: str = Field(..., description="Explanation for the validation result")
