
from fastapi import FastAPI
import time

app = FastAPI(title="Day 21 Synchronous API")


@app.get("/")
def home():
    return {"message": "Synchronous API is running"}


@app.get("/process")
def process_data():
    # Simulate a task that takes 2 seconds
    time.sleep(2)

    return {
        "message": "Task completed",
        "processing_time": "2 seconds",
        "mode": "synchronous"
    }
