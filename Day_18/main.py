
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from agent import run_agent


app = FastAPI(
    title="Company HR Research Agent",
    description="An AI Agent that answers employee questions using company documents."
)


class AgentRequest(BaseModel):
    question: str
    document_id: str


@app.get("/")
def home():
    return {
        "message": "Welcome to the Company HR Research Agent!",
        "docs": "/docs"
    }


@app.post("/ask-agent")
def ask_agent(request: AgentRequest):

    if not request.question.strip():
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )

    try:
        result = run_agent(
            request.question,
            request.document_id
        )

        return result

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )
