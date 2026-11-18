
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from graph_workflow import research_graph

app = FastAPI(
    title="Day 23 - LangGraph Multi-Agent Research Assistant",
    description="Company Research Assistant using LangGraph",
    version="1.0.0"
)


class ResearchRequest(BaseModel):
    question: str = Field(min_length=3)
    document_id: str


@app.get("/")
async def home():
    return {
        "message": "Day 23 LangGraph API is running"
    }


@app.post("/research")
def research(request: ResearchRequest):

    initial_state = {
        "question": request.question,
        "document_id": request.document_id,
        "research_findings": "",
        "analysis": "",
        "critic_feedback": "",
        "approved": False,
        "final_report": "",
        "sources": [],
        "error": ""
    }

    try:
        result = research_graph.invoke(initial_state)

        if result.get("error"):
            raise HTTPException(
                status_code=400,
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

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Workflow failed: {str(e)}"
        )
