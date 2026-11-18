
def writer_agent(state):
    """
    Creates the final research report.
    """

    question = state.get("question", "")
    analysis = state.get("analysis", "")
    feedback = state.get("critic_feedback", "")
    sources = state.get("sources", [])

    if not state.get("approved", False):
        state["final_report"] = (
            "Report not generated because the analysis was not approved.\n"
            + feedback
        )
        return state

    source_text = "\n".join(str(source) for source in sources)

    report = f"""
    COMPANY RESEARCH REPORT

    Research Question:
    {question}

    Analysis:
    {analysis}

    Critic Review:
    {feedback}

    Sources:
    {source_text if source_text else "No sources provided."}
    """

    state["final_report"] = report

    return state
