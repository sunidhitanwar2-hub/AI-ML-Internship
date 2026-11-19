
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Day 23 LangGraph API is running"

def test_research_empty_question():
    response = client.post(
        "/research",
        json={
            "question": "",
            "document_id": "DOC123"
        }
    )

    assert response.status_code == 422

def test_research_missing_document_id():
    response = client.post(
        "/research",
        json={
            "question": "What is the leave policy?"
        }
    )

    assert response.status_code == 422