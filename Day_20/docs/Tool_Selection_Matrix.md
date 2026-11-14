# Day 20 – Tool Selection Matrix

## Purpose
This matrix explains how the Company AI Tool Assistant selects the appropriate tool based on a user's request.

| No. | User Request | Selected Tool | Reason |
|---|---|---|---|
| 1 | Calculate 25 multiplied by 4 | Calculator | Performs mathematical calculations. |
| 2 | What is today's date? | Date Tool | Retrieves the current date. |
| 3 | What is the current time? | Time Tool | Retrieves the current time. |
| 4 | What is the weather in Ambala? | Weather Tool | Retrieves weather information for a city. |
| 5 | Search online for Python tutorials | Web Search Tool | Searches for online information. |
| 6 | Read a PDF document | File Reader Tool | Extracts text from PDF files. |
| 7 | Find employee details for EMP001 | Database Tool | Retrieves employee information from SQLite. |
| 8 | Analyze employee CSV data | Data Analyzer Tool | Analyzes CSV data using pandas. |
| 9 | Prepare an email for an employee | Email Tool | Creates an email draft. |
| 10 | What is the company leave policy? | Company Search Tool | Retrieves relevant HR policy information using the Day 17 RAG API. |
| 11 | Check the weather in Ambala and prepare an email | Weather + Email Tools | Gets weather information and uses it to prepare an email draft. |
| 12 | Calculate a 10% salary increase | Calculator Tool | Calculates the salary increase. |

## Conclusion

The Tool Selection Matrix demonstrates how different user requests are mapped to suitable tools. The assistant can also chain multiple tools together, passing the output of one tool to another.