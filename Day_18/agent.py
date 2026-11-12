
from tools import (
    search_company_documents,
    get_leave_information,
    get_working_hours
)


def run_agent(user_question, document_id):
    """
    AI Agent: Plans the task, selects a tool,
    observes the result, and generates a response.
    """

    question = user_question.lower()

    # STEP 1: Planning
    if "leave" in question or "holiday" in question:
        selected_tool = "leave_information"

    elif "working hours" in question or "office timing" in question:
        selected_tool = "working_hours"

    else:
        selected_tool = "document_search"

    # STEP 2: Action - Select and use a tool
    if selected_tool == "leave_information":
        observation = get_leave_information(document_id)

    elif selected_tool == "working_hours":
        observation = get_working_hours(document_id)

    else:
        observation = search_company_documents(
            user_question,
            document_id
        )

    # STEP 3: Observe the tool result
    answer = observation.get(
        "answer",
        "I could not find an answer in the documents."
    )

    # STEP 4: Return the final result
    return {
        "question": user_question,
        "plan": selected_tool,
        "tool_used": selected_tool,
        "observation": observation.get("sources", []),
        "answer": answer
    }
