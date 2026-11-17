# Multi-Agent Architecture Notes

## Project: Company Research Assistant

### 1. Architecture Overview
The Company Research Assistant uses five specialized AI agents to complete research tasks through a coordinated workflow.

### 2. Main Components

- **Coordinator Agent:** Receives the user query, plans tasks, and manages the workflow.
- **Research Agent:** Retrieves relevant information from company documents using the existing RAG API.
- **Analyzer Agent:** Examines the collected information and identifies important points.
- **Critic Agent:** Reviews the analysis for accuracy, relevance, and missing information.
- **Writer Agent:** Creates a clear and structured final report.

### 3. Shared State
Shared State stores the user question, research findings, analysis, critic feedback, approval status, and final report.

### 4. Communication
Agents exchange information through the shared state. The Coordinator manages task execution and passes the required information between agents.

### 5. Workflow Planning
1. Receive the user's research question.
2. Create a research plan.
3. Retrieve relevant company information.
4. Analyze the findings.
5. Review the analysis.
6. Request corrections if necessary.
7. Generate the final report.

### 6. Error Handling
If research information is unavailable, the system should report that no relevant information was found. If the Critic identifies issues, the workflow should return the information for correction.

### 7. Conclusion
This architecture divides research responsibilities among specialized agents. It improves workflow organization, communication, and report preparation.