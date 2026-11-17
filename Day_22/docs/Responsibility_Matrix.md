# Multi-Agent Responsibility Matrix

## Project: Company Research Assistant

The system uses five AI agents. Each agent has a specific responsibility and communicates with other agents through shared workflow state.

| Agent | Role | Input | Output |
|---|---|---|---|
| Coordinator | Plans and manages workflow | User question | Task plan |
| Research Agent | Retrieves company information | Task plan, documents | Research findings |
| Analyzer | Analyzes collected information | Research findings | Analysis report |
| Critic | Checks accuracy and quality | Research findings, analysis | Feedback |
| Writer | Creates final report | Approved analysis | Final research report |

## Agent Dependencies

1. Coordinator assigns tasks to the Research Agent.
2. Research Agent sends findings to the Analyzer.
3. Analyzer sends its analysis to the Critic.
4. Critic checks the information and provides feedback.
5. If corrections are needed, the workflow returns to the relevant agent.
6. Once approved, the Writer prepares the final report.
7. Coordinator delivers the final report to the user.

## Communication Flow

- Agents communicate through shared state.
- Each agent receives the required output from the previous agent.
- The Critic can request corrections.
- The Coordinator manages the complete workflow.

## Conclusion

The responsibility matrix defines each agent's role, inputs, outputs, dependencies, and communication flow. It helps organize the multi-agent research workflow.