
from agents.research_agent import research_agent
from agents.analyzer_agent import analyzer_agent
from agents.critic_agent import critic_agent
from agents.writer_agent import writer_agent


def run_research_workflow(question, document_id):
    """
    Coordinates all five agents.
    """

    state = {
        "question": question,
        "document_id": document_id,
        "research_findings": "",
        "analysis": "",
        "critic_feedback": "",
        "approved": False,
        "final_report": "",
        "sources": [],
        "error": ""
    }

    # Step 1: Research
    state = research_agent(state)

    if state["error"]:
        return state

    # Step 2: Analyze
    state = analyzer_agent(state)

    # Step 3: Critic review
    state = critic_agent(state)

    # Step 4: Writer
    state = writer_agent(state)

    return state
