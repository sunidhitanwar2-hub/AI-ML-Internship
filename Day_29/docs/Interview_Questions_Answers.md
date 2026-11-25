# Day 29 – Technical Interview Questions & Answers

## Project: AI Research Assistant – Multi-Agent System

### 1. What is the purpose of your project?
My project is an AI Research Assistant that answers questions based on uploaded company documents. It uses a multi-agent workflow to research information, analyze it, check the result, and generate a final report.

### 2. What is the architecture of your project?
The system uses FastAPI for the API, LangGraph for workflow orchestration, multiple specialized agent nodes, and a RAG API for document retrieval and answer generation.

The workflow is:
User → Coordinator → Research Agent → Analyzer → Critic → Writer → Final Response.

### 3. Why did you use LangGraph?
I used LangGraph to organize the workflow into nodes and manage the flow between them. It allows me to define shared state, conditional routing, and workflow execution.

### 4. What is shared state?
Shared state is information passed between workflow nodes. In my project, it stores the question, document ID, research findings, analysis, critic feedback, approval status, final report, sources, and errors.

### 5. What are the different agents in your project?
- Coordinator: validates the request and manages the workflow.
- Research Agent: retrieves information through the RAG API.
- Analyzer: organizes and analyzes the research findings.
- Critic: checks whether the research and analysis are available.
- Writer: prepares the final report.

### 6. How does the Research Agent work?
The Research Agent sends the user's question and document ID to the Day 17 RAG API using an HTTP POST request. It receives the answer and source information and stores them in the shared state.

### 7. How does your system handle errors?
The workflow checks for errors during execution and routes the request to an error-handling node when necessary. The API also validates user input and logs exceptions.

### 8. What is RAG, and why did you use it?
RAG stands for Retrieval-Augmented Generation. It retrieves relevant information from documents and uses that information to generate an answer. I used RAG so that answers are based on company documents rather than only the model's general knowledge.

### 9. How did you test and deploy your project?
I used Pytest for unit and API testing. I created six tests, and all six passed. I also added logging, environment variables, and Docker configuration. I successfully built and ran the project in a Docker container.

### 10. What challenges did you face, and what improvements would you make?
One challenge was connecting the Day 23 application running inside Docker with the RAG API running on my computer. I solved this using `host.docker.internal` and environment variables.

Future improvements include adding authentication, rate limiting, better monitoring, persistent storage, and more advanced AI-based agents.
