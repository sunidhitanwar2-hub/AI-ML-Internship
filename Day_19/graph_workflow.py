from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver

from nodes import (
    AgentState,
    validate_question,
    retrieve_documents,
    handle_error
)


def build_graph():

    workflow = StateGraph(AgentState)

    workflow.add_node("validate", validate_question)
    workflow.add_node("retrieve", retrieve_documents)
    workflow.add_node("error", handle_error)

    workflow.add_edge(START, "validate")

    workflow.add_conditional_edges(
        "validate",
        lambda state: "error" if state.get("error") else "retrieve",
        {
            "error": "error",
            "retrieve": "retrieve"
        }
    )

    workflow.add_conditional_edges(
        "retrieve",
        lambda state: "error" if state.get("error") else END,
        {
            "error": "error",
            END: END
        }
    )

    workflow.add_edge("error", END)

    memory = MemorySaver()

    return workflow.compile(checkpointer=memory)


app_graph = build_graph()