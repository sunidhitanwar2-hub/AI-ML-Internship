
from tools import (
    calculator,
    get_current_date,
    get_current_time,
    read_file,
    get_employee_details,
    web_search,
    get_weather,
    prepare_email,
    analyze_csv,
    company_search
)


# 1. SELECT THE APPROPRIATE TOOL
def select_tool(user_request):
    request = user_request.lower()

    if "weather" in request or "temperature" in request:
        return "weather"

    elif any(word in request for word in ["leave policy", "hr policy", "company policy",
                                           "working hours", "work from home", "holiday policy"]):
        return "company_search"

    elif any(word in request for word in ["calculate", "add", "subtract",
                                           "multiply", "divide", "percentage"]):
        return "calculator"

    elif "time" in request:
        return "time"

    elif "date" in request or "today" in request:
        return "date"

    elif any(word in request for word in ["search", "latest news", "online"]):
        return "web_search"

    elif "analyze" in request or "csv" in request:
            return "data_analyzer"

    elif any(word in request for word in ["read file", "read pdf", "read text"]):
        return "file_reader"

    elif "employee" in request or "employee id" in request:
     return "database"

    elif "email" in request:
        return "email"

    else:
        return "no_tool_found"


# 2. EXECUTE THE SELECTED TOOL
def run_tool(tool_name, **kwargs):

    tools = {
        "calculator": calculator,
        "date": get_current_date,
        "time": get_current_time,
        "weather": get_weather,
        "web_search": web_search,
        "database": get_employee_details,
        "file_reader": read_file,
        "data_analyzer": analyze_csv,
        "email": prepare_email,
        "company_search": company_search
    }

    if tool_name not in tools:
        return {"error": "Tool not found"}

    try:
        return tools[tool_name](**kwargs)

    except Exception as e:
        return {"error": str(e)}
