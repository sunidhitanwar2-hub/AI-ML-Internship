# Day 20 – Workflow Notes

## 1. Project Overview

The Company AI Tool Assistant is a Python-based application that selects and executes tools according to user requests.

## 2. Workflow

1. User enters a request in the terminal.
2. `main.py` receives the request.
3. `tool_planner.py` identifies the required tools.
4. The planner extracts supported parameters, such as city and email address.
5. `tool_executor.py` executes the selected tools.
6. Results are collected and displayed to the user.

## 3. Tool Execution Example

User request:

"Check the weather in Ambala and prepare an email for test@example.com."

Execution flow:

- Weather tool retrieves weather information.
- Email tool receives the weather result.
- Email tool prepares an email draft.
- The final result is displayed.

## 4. Error Handling

The project uses try-except blocks to handle tool execution errors.

If a tool returns an error, the tool chain stops instead of continuing with potentially invalid results.

## 5. Integration with Previous Projects

- Day 17: Company Search Tool connects to the RAG API.
- Day 18: The HR research agent demonstrates tool-based company document search.
- Day 20: The tool assistant combines multiple tools and supports selected tool chains.

## 6. Limitations

- Tool selection is keyword-based.
- Parameter extraction supports selected patterns.
- Tool chaining is implemented for specific workflows.
- Employee database and uploaded document data are stored locally or in memory.
- Email functionality creates drafts but does not send them.

## 7. Conclusion

The project demonstrates tool creation, function calling, tool selection, tool chaining, and basic error handling using Python.