# Day 29 – Presentation Notes

## Project: AI Research Assistant – Multi-Agent System

### 1. Introduction (1 minute)
- Introduce the AI Research Assistant project.
- Explain that it answers questions using company documents.
- Mention that the project combines RAG, LangGraph, FastAPI, and multiple agent nodes.

### 2. Project Architecture (2 minutes)
Explain the main components:
- FastAPI – provides the API endpoint.
- LangGraph – manages workflow execution.
- Coordinator – validates and directs the workflow.
- Research Agent – retrieves information from documents.
- Analyzer – organizes research findings.
- Critic – checks the workflow output.
- Writer – generates the final report.

### 3. Demonstrate the Workflow (3 minutes)
Show the workflow:

User Question → Coordinator → Research → Analyzer → Critic → Writer → Final Answer

Explain how information is passed through shared state.

### 4. Live Demo (3 minutes)
Demonstrate:
1. Open Swagger UI.
2. Show the `/research` endpoint.
3. Enter a question about the company HR policy.
4. Enter the uploaded document ID.
5. Execute the request.
6. Show the final report and sources.

### 5. Testing and Deployment (2 minutes)
Explain:
- Six tests passed using Pytest.
- Logging was implemented.
- Environment variables are used for configuration.
- Docker was used to containerize the application.
- The application was successfully tested inside Docker.

### 6. Challenges and Improvements (2 minutes)
Challenges:
- Connecting the Docker container to the RAG API.
- Managing workflow state.
- Handling errors and API communication.

Future improvements:
- Add authentication and rate limiting.
- Add better monitoring.
- Use persistent storage.
- Improve agents using LLM-based reasoning.
- Add more document formats and features.

### 7. Conclusion (1 minute)
Conclude by explaining that the project helped me understand multi-agent workflows, LangGraph, API integration, testing, logging, and Docker deployment.
