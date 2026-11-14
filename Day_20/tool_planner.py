
import re


# =====================================
# 1. CREATE A TOOL PLAN
# =====================================

def create_tool_plan(user_request):

    request = user_request.lower()

    plan = []

    # Database Tool
    if any(word in request for word in [
        "employee details",
        "employee information",
        "employee salary"
    ]):
        plan.append("database")

    # Company HR Search Tool
    if any(word in request for word in [
        "leave policy",
        "hr policy",
        "working hours",
        "work from home",
        "company policy"
    ]):
        plan.append("company_search")

    # Calculator Tool
    if any(word in request for word in [
        "calculate",
        "percentage",
        "multiply",
        "divide",
        "addition",
        "subtract",
        "salary increase"
    ]):
        plan.append("calculator")

    # Web Search Tool
    if any(word in request for word in [
        "search online",
        "latest news",
        "web search"
    ]):
        plan.append("web_search")

    # File Reader Tool
    if any(word in request for word in [
        "read file",
        "read pdf",
        "read document"
    ]):
        plan.append("file_reader")

    # Weather Tool
    if any(word in request for word in [
        "weather",
        "temperature"
    ]):
        plan.append("weather")

    # Email Tool
    if any(word in request for word in [
        "prepare email",
        "prepare an email",
        "draft email",
        "draft an email",
        "send email",
        "send an email"
    ]):
        plan.append("email")

    # Date Tool
    if "date" in request or "today" in request:
        plan.append("date")

    # Time Tool
    if "current time" in request or "what time" in request:
        plan.append("time")

    # Data Analyzer Tool
    if any(word in request for word in [
        "analyze csv",
        "analyze data",
        "csv analysis"
    ]):
        plan.append("data_analyzer")

    # Remove duplicate tools
    plan = list(dict.fromkeys(plan))

    return plan


# =====================================
# 2. EXTRACT PARAMETERS FROM REQUEST
# =====================================

def extract_parameters(user_request):

    parameters = {}

    # Extract email address
    email_match = re.search(
        r'[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}',
        user_request
    )

    if email_match:
        parameters["recipient"] = email_match.group()

    # Extract city after "weather in"
    city_match = re.search(
        r'\bweather\s+in\s+([A-Za-z ]+?)(?=\s+and\b|[,?.]|$)',
        user_request,
        re.IGNORECASE
    )

    if city_match:
        parameters["city"] = city_match.group(1).strip()

    return parameters


# =====================================
# 3. TEST THE PLANNER
# =====================================

if __name__ == "__main__":

    request = input("Enter your request: ")

    selected_tools = create_tool_plan(request)

    extracted_parameters = extract_parameters(request)

    print("\nSelected Tools:")
    print(selected_tools)

    print("\nExtracted Parameters:")
    print(extracted_parameters)
