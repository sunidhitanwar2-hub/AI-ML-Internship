
import requests

RAG_API_URL = "http://127.0.0.1:8001"


def search_company_documents(question, document_id):
    """
    Tool 1: Search company documents using the Day 17 RAG API.
    """

    response = requests.post(
        f"{RAG_API_URL}/ask",
        json={
            "question": question,
            "document_id": document_id
        },
        timeout=120
    )

    response.raise_for_status()

    return response.json()


def get_leave_information(document_id):
    """
    Tool 2: Search for company leave policy information.
    """

    return search_company_documents(
        "What is the company's leave policy and leave eligibility?",
        document_id
    )


def get_working_hours(document_id):
    """
    Tool 3: Search for company working hours.
    """

    return search_company_documents(
        "What are the company's working hours?",
        document_id
    )
