# Day 28 – Pull Requests and Code Review: Student Profiles Feature

## Project Overview
One assigned feature of the company project **Student Management System with AI Features** (planned on Day 27): student registration and profile management, built with FastAPI and SQLite. The feature was developed on a branch, reviewed through a pull request, improved based on the code review, and merged into `main`.

## Features
- Register, list, view, update (partial) and delete students
- REST API with correct status codes (201, 204, 404, 409, 422)
- Input validation with Pydantic (age, email format, name and course length)
- Unique email per student
- Safe SQL with placeholders (protected against SQL injection)
- Modular structure: config, database, schemas, CRUD and routers
- Logging and environment variable configuration
- 10 API tests using a temporary database

## Project Structure
- `main.py` – FastAPI application and startup
- `config.py` – Settings from environment variables
- `database.py` – SQLite connection and table creation
- `schemas.py` – Request and response models
- `crud.py` – Database operations
- `routers/students.py` – Student API endpoints
- `tests/` – API tests
- `docs/` – Code Review Report
- `.env.example` – Example environment settings

## API Endpoints
| Method | Endpoint | Description |
|---|---|---|
| POST | `/students` | Register a student |
| GET | `/students?skip=0&limit=50` | List students |
| GET | `/students/{id}` | Get one student |
| PATCH | `/students/{id}` | Update some fields |
| DELETE | `/students/{id}` | Delete a student |
| GET | `/health` | Health check |

## Run Locally
```bash
pip install -r requirements.txt
python -m uvicorn main:app --reload --port 8005
```

Swagger UI: http://127.0.0.1:8005/docs

## Run Tests
```bash
python -m pytest tests -v
```

## Git Workflow
1. Created branch `feature/student-profiles`
2. Committed the first version and opened a pull request
3. Reviewed the code (see `docs/Code_Review_Report.md`)
4. Committed the improved version to the same pull request
5. Merged the pull request into `main`

## Documentation
- Code Review Report (`docs/Code_Review_Report.md` and `.docx`)

## Technologies
Python, FastAPI, Pydantic, SQLite, Pytest, Python Logging and Git / GitHub Pull Requests.
