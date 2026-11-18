
def critic_agent(state):
    """
    Reviews the analysis and checks its quality.
    """

    analysis = state.get("analysis", "")
    findings = state.get("research_findings", "")

    if not findings or not analysis:
        state["approved"] = False
        state["critic_feedback"] = (
            "Review failed: Research findings or analysis are missing."
        )
        return state

    if "No research information available" in analysis:
        state["approved"] = False
        state["critic_feedback"] = (
            "Please provide relevant research information."
        )
    else:
        state["approved"] = True
        state["critic_feedback"] = (
            "Approved: Analysis contains research findings and a summary."
        )

    return state
