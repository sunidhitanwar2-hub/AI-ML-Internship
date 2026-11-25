"""Student Management System with AI Features – API entry point.

Run:  python -m uvicorn main:app --reload --port 8005
Docs: http://127.0.0.1:8005/docs
"""

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from config import get_log_level
from database import init_db
from routers import students

logging.basicConfig(
    level=get_log_level(),
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    logger.info("Database ready")
    yield


app = FastAPI(
    title="Student Management System",
    description="Student registration and profile management (Sprint 2 feature).",
    version="0.2.0",
    lifespan=lifespan,
)
app.include_router(students.router)


@app.get("/health", tags=["Health"])
def health() -> dict[str, str]:
    """Simple check that the API is running."""
    return {"status": "ok"}
