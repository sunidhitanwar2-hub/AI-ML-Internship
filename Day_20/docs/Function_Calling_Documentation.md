# Day 20 – Function Calling Documentation

## 1. Introduction

Function calling allows an AI application to select and execute specific functions or tools based on a user's request.

In this project, the Company AI Tool Assistant uses Python functions to perform different tasks.

## 2. Tools Created

| Tool | Function | Purpose |
|---|---|---|
| Calculator | `calculator()` | Performs mathematical calculations. |
| Date | `get_current_date()` | Retrieves today's date. |
| Time | `get_current_time()` | Retrieves the current time. |
| File Reader | `read_file()` | Reads PDF and TXT files. |
| Database | `get_employee_details()` | Retrieves employee details from SQLite. |
| Web Search | `web_search()` | Searches for online information. |
| Weather | `get_weather()` | Retrieves weather information. |
| Email | `prepare_email()` | Creates an email draft. |
| Data Analyzer | `analyze_csv()` | Analyzes CSV files using pandas. |
| Company Search | `company_search()` | Connects to the Day 17 RAG API to search company documents. |

## 3. Function Calling Workflow

1. The user enters a request.
2. The tool planner analyzes the request.
3. The planner selects the appropriate tool or tools.
4. Parameters are extracted from the request where supported.
5. The tool executor calls the selected functions.
6. Tool results are collected and displayed.
7. If a tool returns an error, the execution can stop.

## 4. Tool Chaining

Tool chaining means executing multiple tools in sequence.

Example:

User Request:
"Check the weather in Ambala and prepare an email for test@example.com."

Execution:

1. Weather tool retrieves the weather information.
2. The weather result is passed to the email tool.
3. The email tool creates an email draft using the weather details.
4. The final result is displayed.

## 5. Error Handling

The project uses basic error handling through Python try-except blocks.

- Invalid calculations return an error.
- Missing or invalid files return an error.
- Database errors are handled.
- If a tool returns an error during a chain, the remaining tools are not executed.

## 6. Practical Implementation

The Company AI Tool Assistant demonstrates function calling through:

- `tools.py` – contains the tool functions.
- `tool_selector.py` – selects a tool using keywords.
- `tool_planner.py` – creates a tool execution plan and extracts supported parameters.
- `tool_executor.py` – executes the selected tools.
- `main.py` – provides the main user interface.

## 7. Limitations

- Tool selection uses keyword-based rules, not an LLM.
- Parameter extraction supports only selected details.
- Tool chaining is implemented for specific workflows, such as Weather → Email.
- The email tool creates a draft; it does not send emails.
- Web search results may be limited.

## 8. Conclusion

This project demonstrates tool creation, function calling, tool planning, tool execution, tool chaining, and basic error handling using Python.