
import os
import requests


def research_agent(state):
    """
    Research Agent:
    Connects to the Day 17 RAG API and retrieves
    company information.
    """

    rag_api_url = os.getenv(
        "RAG_API_URL",
        "http://127.0.0.1:8001/ask"
    )

    question = state.get("question", "")
    document_id = state.get("document_id", "")

    try:
        response = requests.post(
            rag_api_url,
            json={
                "question": question,
                "document_id": document_id
            },
            timeout=120
        )

        response.raise_for_status()
        result = response.json()

        return {
            "research_findings": result.get("answer", ""),
            "sources": result.get("sources", []),
            "error": ""
        }

    except requests.exceptions.RequestException as e:
        return {
            "research_findings": "",
            "sources": [],
            "error": f"RAG API connection failed: {str(e)}"
        }

    except Exception as e:
        return {
            "research_findings": "",
            "sources": [],
            "error": f"Research Agent failed: {str(e)}"
        }
