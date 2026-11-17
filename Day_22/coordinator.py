
from agents.research_agent import research_agent
from agents.analyzer_agent import analyzer_agent
from agents.critic_agent import critic_agent
from agents.writer_agent import writer_agent


def run_research_workflow(question, document_id):

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

    # Step 2: Analyze and review
    max_attempts = 2

    for attempt in range(max_attempts):

        state = analyzer_agent(state)
        state = critic_agent(state)

        if state["approved"]:
            break

        # Send critic feedback back to the analyzer
        state["research_findings"] += (
            "\nCritic feedback: " + state["critic_feedback"]
        )

    # Step 3: Generate final report
    state = writer_agent(state)

    return state
