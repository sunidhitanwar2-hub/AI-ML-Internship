
import os
import sqlite3
import ast
import operator
import requests
import pandas as pd

from datetime import datetime


# 1. CALCULATOR TOOL
def calculator(expression):
    try:
        operations = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.Pow: operator.pow,
            ast.Mod: operator.mod,
        }

        def calculate(node):
            if isinstance(node, ast.Expression):
                return calculate(node.body)
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
                return node.value
            if isinstance(node, ast.BinOp) and type(node.op) in operations:
                return operations[type(node.op)](
                    calculate(node.left), calculate(node.right)
                )
            if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
                value = calculate(node.operand)
                return value if isinstance(node.op, ast.UAdd) else -value
            raise ValueError("Unsupported mathematical expression")

        result = calculate(ast.parse(expression, mode="eval"))
        return {"result": result, "error": None}

    except Exception as e:
        return {"result": None, "error": str(e)}


# 2. DATE TOOL
def get_current_date():
    return datetime.now().strftime("%d-%m-%Y")


def get_current_time():
    return datetime.now().strftime("%I:%M:%S %p")


# 3. FILE READER TOOL (TXT AND PDF)
def read_file(file_path):
    try:
        if not os.path.isfile(file_path):
            return {"content": None, "error": "File not found"}

        if file_path.lower().endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

        elif file_path.lower().endswith(".pdf"):
            from pypdf import PdfReader
            reader = PdfReader(file_path)
            content = "\n".join(page.extract_text() or "" for page in reader.pages)

        else:
            return {"content": None, "error": "Only TXT and PDF files are supported"}

        return {"content": content, "error": None}

    except Exception as e:
        return {"content": None, "error": str(e)}


# 4. DATABASE TOOL
def get_employee_details(employee_id):
    try:
        connection = sqlite3.connect("employee.db")
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM employees WHERE employee_id = ?",
            (employee_id,)
        )

        employee = cursor.fetchone()
        connection.close()

        if employee is None:
            return {"employee": None, "error": "Employee not found"}

        return {"employee": employee, "error": None}

    except Exception as e:
        return {"employee": None, "error": str(e)}


# 5. WEB SEARCH TOOL
def web_search(query):
    try:
        response = requests.get(
            "https://api.duckduckgo.com/",
            params={"q": query, "format": "json"},
            timeout=15
        )
        response.raise_for_status()
        data = response.json()

        results = []
        if data.get("AbstractText"):
            results.append(data["AbstractText"])

        for item in data.get("RelatedTopics", []):
            if isinstance(item, dict) and item.get("Text"):
                results.append(item["Text"])

        return {"results": results[:5], "error": None}

    except Exception as e:
        return {"results": [], "error": str(e)}


# 6. WEATHER TOOL
def get_weather(city):
    try:
        response = requests.get(
            f"https://wttr.in/{city}",
            params={"format": "j1"},
            timeout=15
        )
        response.raise_for_status()
        data = response.json()

        current = data["current_condition"][0]

        return {
            "city": city,
            "temperature_c": current["temp_C"],
            "description": current["weatherDesc"][0]["value"],
            "humidity": current["humidity"],
            "error": None
        }

    except Exception as e:
        return {"city": city, "error": str(e)}


# 7. EMAIL TOOL
# This prepares an email draft; it does not send an email.
def prepare_email(recipient, subject, message):
    if not recipient or "@" not in recipient:
        return {"status": "failed", "error": "Invalid email address"}

    return {
        "status": "draft_created",
        "recipient": recipient,
        "subject": subject,
        "message": message
    }


# 8. DATA ANALYZER TOOL
def analyze_csv(file_path):
    try:
        if not os.path.isfile(file_path):
            return {"analysis": None, "error": "CSV file not found"}

        df = pd.read_csv(file_path)

        analysis = {
            "rows": len(df),
            "columns": list(df.columns),
            "summary": df.describe(include="all").fillna("").to_dict()
        }

        return {"analysis": analysis, "error": None}

    except Exception as e:
        return {"analysis": None, "error": str(e)}
# 9. COMPANY HR SEARCH TOOL (DAY 17 RAG API)

RAG_API_URL = "http://127.0.0.1:8001"

def company_search(question, document_id):
    try:
        response = requests.post(
            f"{RAG_API_URL}/ask",
            json={
                "question": question,
                "document_id": document_id
            },
            timeout=300
        )

        response.raise_for_status()
        data = response.json()

        return {
            "answer": data.get("answer"),
            "sources": data.get("sources", []),
            "error": None
        }

    except Exception as e:
        return {
            "answer": None,
            "sources": [],
            "error": str(e)
        }
def create_employee_database():
    try:
        connection = sqlite3.connect("employee.db")
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                employee_id TEXT PRIMARY KEY,
                name TEXT,
                department TEXT,
                salary INTEGER
            )
        """)

        cursor.execute("""
            INSERT OR IGNORE INTO employees
            VALUES ('EMP001', 'Rahul', 'IT', 45000)
        """)

        connection.commit()
        connection.close()

        return "Employee database created successfully"

    except Exception as e:
        return str(e)   
