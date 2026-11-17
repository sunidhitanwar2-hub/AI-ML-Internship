
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from agents.coordinator import run_research_workflow

app = FastAPI(
    title="Day 22 - Multi-Agent Research Assistant",
    description="Company Research Assistant using five specialized agents",
    version="1.0.0"
)


class ResearchRequest(BaseModel):
    question: str = Field(min_length=3)
    document_id: str


@app.get("/")
async def home():
    return {
        "message": "Multi-Agent Research Assistant is running"
    }


@app.post("/research")
def research(request: ResearchRequest):

    result = run_research_workflow(
        request.question,
        request.document_id
    )

    if result["error"]:
        raise HTTPException(
            status_code=502,
            detail=result["error"]
        )

    return {
        "question": result["question"],
        "research_findings": result["research_findings"],
        "analysis": result["analysis"],
        "critic_feedback": result["critic_feedback"],
        "approved": result["approved"],
        "final_report": result["final_report"],
        "sources": result["sources"]
    }
