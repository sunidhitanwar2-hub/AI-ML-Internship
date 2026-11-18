
# Day 23 - LangGraph Multi-Agent System Explanation

## 1. Introduction

The Day 23 project integrates LangGraph with the multi-agent research assistant developed in Day 22.

The system helps employees find information from company documents using multiple specialized agents.

LangGraph manages the workflow, agent communication, shared state, and conditional routing.

## 2. System Architecture

The system contains the following components:

1. **FastAPI:** Provides the API endpoint for user requests.
2. **LangGraph:** Controls the execution and communication flow between agents.
3. **Coordinator Agent:** Validates requests and starts the workflow.
4. **Research Agent:** Retrieves information from the Day 17 RAG API.
5. **Analyzer Agent:** Organizes research findings and identifies key observations.
6. **Critic Agent:** Reviews the analysis and provides approval feedback.
7. **Writer Agent:** Generates the final research report.
8. **Shared State:** Stores information exchanged between agents.

## 3. LangGraph Integration

LangGraph is used to create a workflow consisting of nodes and edges.

Each agent is connected as a node in the graph.

The workflow follows this order:

User Request → Coordinator → Research Agent → Analyzer Agent → Critic Agent → Writer Agent → Final Response

The graph uses conditional routing to handle errors and approval decisions.

## 4. Shared State Management

All agents communicate through a shared state.

The shared state contains:

- question
- document_id
- research_findings
- analysis
- critic_feedback
- approved
- final_report
- sources
- error

Each agent reads the required information and updates the shared state with its output.

This allows information to move between agents without directly connecting every agent to every other agent.

## 5. Agent Communication

The agents communicate through the LangGraph workflow.

- Coordinator validates the request.
- Research Agent retrieves information from the RAG API.
- Analyzer Agent organizes the findings.
- Critic Agent reviews the analysis.
- Writer Agent creates the final report.

LangGraph passes the updated state between these nodes.

## 6. Conditional Routing and Error Handling

The system uses conditional routing to decide the next step.

Examples:

- If the question is empty, the workflow moves to the Error Node.
- If the document ID is missing, the workflow moves to the Error Node.
- If the Research Agent encounters an API error, the workflow moves to the Error Node.
- If the Critic Agent approves the analysis, the workflow moves to the Writer Agent.
- If the Critic Agent rejects the analysis, the workflow moves to the Error Node.

This prevents the system from generating a final report when the analysis is not approved.

## 7. Integration with Day 17 RAG API

The Research Agent communicates with the existing Day 17 RAG API.

The RAG API searches the uploaded company documents and generates relevant answers.

The Research Agent receives the findings and source information and passes them to the other agents through shared state.

## 8. Practical Testing

The system was tested using the question:

"What is the company's leave policy?"

The system successfully returned information about:

- Work-from-home policy.
- Casual and sick leaves.
- Working hours.
- Attendance rules.
- Official holiday calendar.

The Critic Agent approved the analysis, and the Writer Agent generated the final company research report.

## 9. Technologies Used

- Python
- LangGraph
- LangChain Core
- FastAPI
- Uvicorn
- Requests
- Pydantic
- Existing Day 17 RAG API

## 10. Conclusion

The Day 23 project successfully integrates LangGraph into the existing multi-agent research assistant.

It demonstrates agent coordination, shared state management, conditional routing, API integration, and error handling.

The system provides a structured way to process company-related questions and generate research reports using multiple specialized agents.
