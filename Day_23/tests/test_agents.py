
from graph_workflow import coordinator_node


def test_valid_request():
    state = {
        "question": "What is the leave policy?",
        "document_id": "DOC123"
    }

    result = coordinator_node(state)

    assert result["error"] == ""


def test_empty_question():
    state = {
        "question": "",
        "document_id": "DOC123"
    }

    result = coordinator_node(state)

    assert result["error"] == "Question cannot be empty."


def test_empty_document_id():
    state = {
        "question": "What is the leave policy?",
        "document_id": ""
    }

    result = coordinator_node(state)

    assert result["error"] == "Document ID cannot be empty."
