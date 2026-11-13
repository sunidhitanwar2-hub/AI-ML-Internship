# Day 19 – Error Handling Notes

## 1. Empty Question
- **Problem:** User submits an empty question.
- **Detection:** Validation node checks the question.
- **Solution:** Conditional routing sends the request to the error handler.
- **Result:** "Question cannot be empty."

## 2. RAG API Failure
- **Problem:** Day 17 RAG API is unavailable or returns an error.
- **Detection:** Python exception handling catches the failure.
- **Solution:** The workflow routes to the error handler.
- **Result:** An error message is returned without crashing the workflow.

## 3. Memory Limitation
- MemorySaver stores checkpoints in memory.
- Checkpoints are not permanent and may be lost when the application restarts.

## 4. Conclusion
LangGraph conditional routing and exception handling help manage invalid questions and API failures. These mechanisms make the HR Assistant more reliable.