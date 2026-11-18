
from typing import TypedDict, List

class ResearchState(TypedDict):
    question: str
    document_id: str

    research_findings: str
    analysis: str
    critic_feedback: str

    approved: bool
    final_report: str

    sources: List[str]
    error: str