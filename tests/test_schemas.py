import pytest
from pydantic import ValidationError
from core.schemas.messages import IngestMessage
from core.schemas.findings import Finding, SeverityEnum
from core.schemas.debate import RiskScore
from core.schemas.reporting import Remediation

def test_ingest_message_valid():
    msg = IngestMessage(
        document_id="doc-123",
        content_hash="abc123hash",
        chunk_count=5,
        metadata={"filename": "test.pdf"}
    )
    assert msg.document_id == "doc-123"
    assert msg.chunk_count == 5

def test_ingest_message_missing_fields():
    with pytest.raises(ValidationError):
        IngestMessage(document_id="doc-123")

def test_finding_valid():
    finding = Finding(
        id="f-001",
        agent_name="LEXIS",
        severity=SeverityEnum.HIGH,
        claim="Missing data protection clause",
        clause_ref="Section 3.2",
        quote="Data may be shared with partners."
    )
    assert finding.severity == SeverityEnum.HIGH
    assert finding.agent_name == "LEXIS"

def test_finding_invalid_severity():
    with pytest.raises(ValidationError):
        Finding(
            id="f-002",
            agent_name="SENTINEL",
            severity="NOT_A_SEVERITY", # Invalid
            claim="Test claim",
            clause_ref="Sec 1",
            quote="Quote"
        )

def test_risk_score_valid():
    score = RiskScore(score=85, critical_findings_count=2, summary="High risk detected")
    assert score.score == 85

def test_risk_score_out_of_bounds():
    with pytest.raises(ValidationError):
        RiskScore(score=105, critical_findings_count=1, summary="Too high")
    
    with pytest.raises(ValidationError):
        RiskScore(score=-5, critical_findings_count=1, summary="Too low")
