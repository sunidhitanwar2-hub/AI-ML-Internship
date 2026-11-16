# Day 21 – Updated API Documentation

## 1. Project Overview

This project demonstrates asynchronous programming and advanced FastAPI features, including middleware, background tasks, validation, dependency injection, and API versioning.

**Base URL:** `http://127.0.0.1:8002`

## 2. Available Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Home endpoint |
| GET | `/process` | Simulates asynchronous processing |
| POST | `/background-task` | Starts a background task |
| POST | `/validate` | Validates user input |
| GET | `/api/v1/info` | Returns API version information |
| GET | `/app-info` | Demonstrates dependency injection |
| GET | `/error-example` | Demonstrates HTTP error handling |

## 3. Endpoint Details

### GET /

Returns a welcome message and application information.

### GET /process

Simulates a two-second asynchronous operation using `asyncio.sleep()`.

### POST /background-task

Starts a background task that writes a completion message to `background_tasks.log`.

### POST /validate

Validates user information using Pydantic.

Example request:

```json
{
  "name": "Rahul",
  "age": 22
}
```

Validation rules:
- Name must contain 2–50 characters.
- Age must be between 18 and 100.

### GET /api/v1/info

Returns information about API version 1.

### GET /app-info

Returns application information using FastAPI dependency injection.

### GET /error-example

Demonstrates HTTP error handling by returning a 400 Bad Request response.

## 4. Middleware

The application uses HTTP middleware to measure request processing time.

It adds the `X-Process-Time` response header and prints the request duration in the terminal.

## 5. API Documentation Interface

FastAPI provides interactive Swagger documentation.

Open:

`http://127.0.0.1:8002/docs`

Users can test the available endpoints directly through the browser.

## 6. Technologies Used

- Python
- FastAPI
- Uvicorn
- Pydantic
- Asyncio
- HTTPX

## 7. Conclusion

The updated API demonstrates asynchronous endpoints, background processing, middleware, request validation, dependency injection, API versioning, and error handling.