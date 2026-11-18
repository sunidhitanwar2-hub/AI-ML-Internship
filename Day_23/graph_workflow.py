
from langgraph.graph import StateGraph, START, END

from shared_state import ResearchState
from agents.research_agent import research_agent
from agents.analyzer_agent import analyzer_agent
from agents.critic_agent import critic_agent
from agents.writer_agent import writer_agent


def coordinator_node(state):
    """Checks the user's request before starting research."""
    if not state["question"].strip():
        return {"error": "Question cannot be empty."}

    if not state["document_id"].strip():
        return {"error": "Document ID cannot be empty."}

    return {"error": ""}


def research_node(state):
    return research_agent(dict(state))


def analyzer_node(state):
    return analyzer_agent(dict(state))


def critic_node(state):
    return critic_agent(dict(state))


def writer_node(state):
    return writer_agent(dict(state))


def error_node(state):
    return {
        "approved": False,
        "final_report": "Workflow failed: " + state.get(
            "error", "Unknown error"
        )
    }


def route_after_coordinator(state):
    if state.get("error"):
        return "error"
    return "research"


def route_after_research(state):
    if state.get("error"):
        return "error"
    return "analyzer"


def route_after_critic(state):
    if state.get("approved"):
        return "writer"
    return "error"


workflow = StateGraph(ResearchState)

workflow.add_node("coordinator", coordinator_node)
workflow.add_node("research", research_node)
workflow.add_node("analyzer", analyzer_node)
workflow.add_node("critic", critic_node)
workflow.add_node("writer", writer_node)
workflow.add_node("error", error_node)

workflow.add_edge(START, "coordinator")

workflow.add_conditional_edges(
    "coordinator",
    route_after_coordinator
)

workflow.add_conditional_edges(
    "research",
    route_after_research
)

workflow.add_edge("analyzer", "critic")

workflow.add_conditional_edges(
    "critic",
    route_after_critic
)

workflow.add_edge("writer", END)
workflow.add_edge("error", END)

research_graph = workflow.compile()
