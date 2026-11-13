from fastapi import FastAPI
from pydantic import BaseModel
from graph_workflow import app_graph

app = FastAPI(title="Day 19 - LangGraph HR Assistant")


class AgentRequest(BaseModel):
    question: str
    document_id: str
    thread_id: str = "hr-user-1"


@app.get("/")
def home():
    return {"message": "LangGraph HR Assistant is running"}


@app.post("/ask")
def ask_question(request: AgentRequest):
    initial_state = {
        "question": request.question,
        "document_id": request.document_id,
        "answer": None,
        "sources": [],
        "error": None
    }

    config = {
        "configurable": {
            "thread_id": request.thread_id
        }
    }

    result = app_graph.invoke(initial_state, config=config)

    return {
        "question": request.question,
        "answer": result.get("answer"),
        "sources": result.get("sources", []),
        "error": result.get("error")
    }