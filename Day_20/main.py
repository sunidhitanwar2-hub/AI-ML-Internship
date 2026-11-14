
from tool_selector import select_tool, run_tool
from tool_planner import create_tool_plan, extract_parameters
from tool_executor import execute_tool_plan


def main():

    print("\n===== Company AI Tool Assistant =====")

    # Get user request
    user_request = input("\nEnter your request: ")

    # Step 1: Select required tools
    tool_plan = create_tool_plan(user_request)

    # Step 2: Extract parameters
    parameters = extract_parameters(user_request)

    # Step 3: Execute the selected tools
    if tool_plan:

        print("\n===== Tool Planning =====")
        print("User Request:", user_request)

        print("\nSelected Tools:", tool_plan)

        print("\nExtracted Parameters:", parameters)

        results = execute_tool_plan(
            tool_plan,
            user_request,
            parameters
        )

        # Step 4: Display final results
        print("\n===== Final Tool Results =====")

        for tool_name, result in results.items():

            print(f"\n{tool_name}:")
            print(result)

        print("\n===== Execution Completed =====")

        return

    # Fallback: Original single-tool selector
    selected_tool = select_tool(user_request)

    print("\nSelected Tool:", selected_tool)

    if selected_tool == "calculator":

        expression = input("Enter calculation: ")
        result = run_tool("calculator", expression=expression)

    elif selected_tool == "date":

        result = run_tool("date")

    elif selected_tool == "time":

        result = run_tool("time")

    elif selected_tool == "weather":

        city = input("Enter city: ")
        result = run_tool("weather", city=city)

    elif selected_tool == "web_search":

        query = input("Enter search query: ")
        result = run_tool("web_search", query=query)

    elif selected_tool == "database":

        employee_id = input("Enter employee ID: ")
        result = run_tool("database", employee_id=employee_id)

    elif selected_tool == "file_reader":

        file_path = input("Enter file path: ")
        result = run_tool("file_reader", file_path=file_path)

    elif selected_tool == "data_analyzer":

        file_path = input("Enter CSV file path: ")
        result = run_tool("data_analyzer", file_path=file_path)

    elif selected_tool == "email":

        recipient = input("Enter recipient email: ")
        subject = input("Enter email subject: ")
        message = input("Enter email message: ")

        result = run_tool(
            "email",
            recipient=recipient,
            subject=subject,
            message=message
        )

    elif selected_tool == "company_search":

        document_id = input("Enter Day 17 document ID: ")

        result = run_tool(
            "company_search",
            question=user_request,
            document_id=document_id
        )

    else:

        result = {"error": "No suitable tool found"}

    print("\n===== Result =====")
    print(result)


if __name__ == "__main__":
    main()
