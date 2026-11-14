
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

def execute_tool(
    tool_name,
    user_request,
    previous_results=None,
    parameters=None
):

    if previous_results is None:
        previous_results = {}

    if parameters is None:
        parameters = {}

    try:

        # 1. Calculator Tool
        if tool_name == "calculator":

            expression = input("Enter calculation: ")
            return calculator(expression)

        # 2. Database Tool
        elif tool_name == "database":

            employee_id = parameters.get("employee_id")

            if not employee_id:
                employee_id = input("Enter employee ID: ")

            return get_employee_details(employee_id)

        # 3. Weather Tool
        elif tool_name == "weather":

            city = parameters.get("city")

            if not city:
                city = input("Enter city: ")

            return get_weather(city)

        # 4. Web Search Tool
        elif tool_name == "web_search":

            query = input("Enter search query: ")
            return web_search(query)

        # 5. File Reader Tool
        elif tool_name == "file_reader":

            file_path = input("Enter file path: ")
            return read_file(file_path)

        # 6. Data Analyzer Tool
        elif tool_name == "data_analyzer":

            file_path = input("Enter CSV file path: ")
            return analyze_csv(file_path)

        # 7. Email Tool
        elif tool_name == "email":

            recipient = parameters.get("recipient")

            if not recipient:
                recipient = input("Enter recipient email: ")

            subject = input("Enter email subject: ")

            # Use previous Weather Tool result
            if "weather" in previous_results:

                weather_data = previous_results["weather"]

                if weather_data.get("error"):
                    return {
                        "error": "Weather information unavailable."
                    }

                message = (
                    f"Weather Update for {weather_data['city']}\n"
                    f"Temperature: {weather_data['temperature_c']}°C\n"
                    f"Weather: {weather_data['description']}\n"
                    f"Humidity: {weather_data['humidity']}%"
                )

                print("\nAutomatically generated email message:")
                print(message)

            else:
                message = input("Enter email message: ")

            return prepare_email(
                recipient,
                subject,
                message
            )

        # 8. Date Tool
        elif tool_name == "date":

            return get_current_date()

        # 9. Time Tool
        elif tool_name == "time":

            return get_current_time()

        # 10. Company HR Search Tool
        elif tool_name == "company_search":

            document_id = input("Enter Day 17 document ID: ")

            return company_search(
                user_request,
                document_id
            )

        else:

            return {
                "error": f"Unknown tool: {tool_name}"
            }

    except Exception as e:

        return {
            "error": str(e)
        }

def execute_tool_plan(
    tool_plan,
    user_request,
    parameters=None
):

    if parameters is None:
        parameters = {}

    results = {}

    print("\n===== Executing Tool Chain =====")

    for tool_name in tool_plan:

        print(f"\nExecuting Tool: {tool_name}")

        result = execute_tool(
            tool_name,
            user_request,
            previous_results=results,
            parameters=parameters
        )

        results[tool_name] = result

        print("Tool Result:", result)

        # Stop if a tool fails
        if isinstance(result, dict) and result.get("error"):

            print("\nTool chain stopped because of an error.")
            break

    return results