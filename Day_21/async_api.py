
from fastapi import (
    FastAPI,
    Request,
    BackgroundTasks,
    Depends,
    HTTPException
)
from pydantic import BaseModel, Field
import asyncio
import time

app = FastAPI(
    title="Day 21 - Advanced Asynchronous API",
    description="API demonstrating async programming and FastAPI features",
    version="1.0.0"
)


# 1. Middleware: Measure request processing time
@app.middleware("http")
async def timing_middleware(request: Request, call_next):
    start_time = time.perf_counter()

    response = await call_next(request)

    process_time = time.perf_counter() - start_time

    response.headers["X-Process-Time"] = str(
        round(process_time, 4)
    )

    print(
        f"{request.method} {request.url.path} "
        f"completed in {process_time:.4f} seconds"
    )

    return response


# 2. Dependency Injection
def get_app_info():
    return {
        "application": "Day 21 API",
        "version": "1.0.0"
    }


# 3. Background Task Function
def save_background_log(message: str):
    with open("background_tasks.log", "a") as file:
        file.write(message + "\n")


# 4. Request Validation
class UserRequest(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    age: int = Field(ge=18, le=100)


# 5. Home Endpoint
@app.get("/")
async def home(info: dict = Depends(get_app_info)):
    return {
        "message": "Asynchronous API is running",
        "application_info": info
    }


# 6. Async Processing Endpoint
@app.get("/process")
async def process_data():
    await asyncio.sleep(2)

    return {
        "message": "Task completed",
        "processing_time": "2 seconds",
        "mode": "asynchronous"
    }


# 7. Background Task Endpoint
@app.post("/background-task")
async def run_background_task(
    background_tasks: BackgroundTasks
):
    background_tasks.add_task(
        save_background_log,
        "Background task completed successfully"
    )

    return {
        "message": "Background task started"
    }


# 8. Validation Endpoint
@app.post("/validate")
async def validate_user(user: UserRequest):
    return {
        "message": "User data is valid",
        "user": user.model_dump()
    }


# 9. API Versioning - Version 1
@app.get("/api/v1/info")
async def api_v1():
    return {
        "version": "v1",
        "message": "Welcome to API Version 1"
    }


# 10. Dependency Injection Example
@app.get("/app-info")
async def application_info(
    info: dict = Depends(get_app_info)
):
    return info


# 11. Error Handling Example
@app.get("/error-example")
async def error_example():
    raise HTTPException(
        status_code=400,
        detail="This is an example error response"
    )
