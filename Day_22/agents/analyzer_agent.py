
def analyzer_agent(state):
    """
    Analyzes the research findings.
    """

    findings = state.get("research_findings", "")

    if not findings:
        state["analysis"] = "No research information available."
        return state

    analysis = f"""
    RESEARCH ANALYSIS

    Original Findings:
    {findings}

    Key Observations:
    - The information was retrieved from company documents.
    - The findings are relevant to the user's research question.
    - The information should be checked for accuracy and completeness.

    Summary:
    {findings}
    """

    state["analysis"] = analysis

    return state
