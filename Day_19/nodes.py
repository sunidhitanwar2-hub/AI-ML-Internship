from typing import TypedDict, Optional


class AgentState(TypedDict):
    question: str
    document_id: str
    answer: Optional[str]
    sources: list
    error: Optional[str]


def validate_question(state: AgentState):
    question = state.get("question", "").strip()

    if not question:
        return {"error": "Question cannot be empty."}

    return {"question": question}


def handle_error(state: AgentState):
    return {
        "answer": state.get("error", "Something went wrong."),
        "sources": []
    }
import requests

RAG_API_URL = "http://127.0.0.1:8001"


def retrieve_documents(state: AgentState):
    try:
        response = requests.post(
            f"{RAG_API_URL}/ask",
            json={
                "question": state["question"],
                "document_id": state["document_id"]
            },
            timeout=300
        )
        response.raise_for_status()

        data = response.json()

        return {
            "answer": data.get("answer", ""),
            "sources": data.get("sources", []),
            "error": None
        }

    except Exception as e:
        return {
            "error": f"Document retrieval failed: {str(e)}"
        }