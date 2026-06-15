from typing import List
from pydantic import BaseModel, Field

class Remediation(BaseModel):
    """
    Mitigation strategies proposed by FORGE for specific findings.
    """
    finding_id: str = Field(..., description="ID of the finding to remediate")
    recommendation: str = Field(..., description="Actionable recommendation to mitigate the risk")
    effort: str = Field(..., description="Estimated effort or complexity (e.g., Low, Medium, High)")

class ExecutiveSummary(BaseModel):
    """
    Final consolidated report payload composed by HERALD.
    """
    overall_score: int = Field(..., ge=0, le=100, description="Overall risk score")
    key_risks: List[str] = Field(..., description="List of the most critical risks identified")
    remediations: List[Remediation] = Field(..., description="Proposed remediations")
    band_room_url: str = Field(..., description="URL to the Band Room for full traceability")
