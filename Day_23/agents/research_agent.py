
import requests


def research_agent(state):
    """
    Retrieves information from the existing Day 17 RAG API.
    """

    question = state["question"]
    document_id = state["document_id"]

    url = "http://127.0.0.1:8001/ask"

    payload = {
        "question": question,
        "document_id": document_id
    }

    try:
        response = requests.post(
            url,
            json=payload,
            timeout=120
        )

        response.raise_for_status()
        result = response.json()

        state["research_findings"] = result.get("answer", "")
        state["sources"] = result.get("sources", [])
        state["error"] = ""

    except requests.RequestException as e:
        state["research_findings"] = ""
        state["sources"] = []
        state["error"] = f"Research failed: {str(e)}"

    return state
