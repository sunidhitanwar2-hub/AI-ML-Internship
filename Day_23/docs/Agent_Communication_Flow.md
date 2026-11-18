
# Agent Communication Flow

## 1. Introduction
This document explains how the different agents communicate and share information in the Day 23 LangGraph Multi-Agent Research Assistant.

The system uses LangGraph to coordinate multiple agents and manage their workflow through shared state.

## 2. User Request

Example user question:

"What is the company's leave policy?"

The user also provides a document ID uploaded through the Day 17 RAG API.

## 3. Agent Communication Process

### Step 1: User
- Sends a research question.
- Provides the document ID.

### Step 2: Coordinator Agent
- Receives the user's request.
- Checks whether the question and document ID are provided.
- Routes valid requests to the Research Agent.
- Routes invalid requests to the Error Node.

### Step 3: Research Agent
- Receives the question and document ID.
- Communicates with the Day 17 RAG API.
- Retrieves relevant company information.
- Stores research findings and sources in shared state.

### Step 4: Analyzer Agent
- Receives the research findings.
- Organizes the information.
- Identifies important observations.
- Stores the analysis in shared state.

### Step 5: Critic Agent
- Reviews the analysis.
- Checks whether research findings and a summary are available.
- Approves or rejects the analysis.
- Stores feedback and approval status.

### Step 6: Writer Agent
- Receives the approved analysis.
- Prepares the final company research report.
- Adds source information.
- Stores the final report in shared state.

### Step 7: Final Response
- The API returns the final report to the user.
- The response includes research findings, analysis, critic feedback, and sources.

## 4. Shared State Communication

The agents communicate through a shared state containing:

- question
- document_id
- research_findings
- analysis
- critic_feedback
- approved
- final_report
- sources
- error

Each agent reads the information it needs and updates its output in the shared state.

## 5. Error Handling

The workflow handles these situations:

- Empty question: Coordinator sends the workflow to the Error Node.
- Missing document ID: Coordinator sends the workflow to the Error Node.
- Research API failure: Research Agent records an error, and the workflow routes to the Error Node.
- Critic rejection: The workflow routes to the Error Node instead of generating an unapproved report.

## 6. Practical Test Result

Test Question: What is the company's leave policy?

The system successfully retrieved the following information:

- Employees can work from home up to 2 days per week with manager approval.
- Employees receive 12 casual leaves and 12 sick leaves per year.
- Standard working hours are 9 AM to 6 PM, Monday to Friday.
- Employees must inform their manager if they cannot attend work.
- The company follows the official holiday calendar.

The Critic Agent approved the analysis, and the Writer Agent generated the final report.

## 7. Conclusion

The Day 23 system successfully integrates LangGraph with the multi-agent workflow developed in Day 22.

LangGraph manages agent execution, shared state, communication flow, and conditional routing. The system connects the Research Agent with the existing Day 17 RAG API to answer company-related questions.
