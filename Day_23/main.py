
import os
import logging

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from dotenv import load_dotenv
from logging_config import logger
from graph_workflow import research_graph

# Load environment variables
load_dotenv()

# Create FastAPI application
app = FastAPI(
    title=os.getenv(
        "APP_NAME",
        "Day 23 Multi-Agent Research Assistant"
    ),
    version=os.getenv("APP_VERSION", "1.0.0"),
    description="Company Research Assistant using LangGraph"
)

# Request model
class ResearchRequest(BaseModel):
    question: str = Field(min_length=3)
    document_id: str

# Home endpoint
@app.get("/")
async def home():
    logger.info("Home endpoint accessed")

    return {
        "message": "Day 23 LangGraph API is running"
    }

# Research endpoint
@app.post("/research")
def research(request: ResearchRequest):

    logger.info("Research request received")

    initial_state = {
        "question": request.question,
        "document_id": request.document_id,
        "research_findings": "",
        "analysis": "",
        "critic_feedback": "",
        "approved": False,
        "final_report": "",
        "sources": [],
        "error": ""
    }

    try:
        logger.info("Starting LangGraph workflow")

        result = research_graph.invoke(initial_state)

        if result.get("error"):
            logger.error(
                "Research workflow failed: %s",
                result["error"]
            )

            raise HTTPException(
                status_code=400,
                detail=result["error"]
            )

        logger.info("Research workflow completed successfully")

        return {
            "question": result["question"],
            "research_findings": result["research_findings"],
            "analysis": result["analysis"],
            "critic_feedback": result["critic_feedback"],
            "approved": result["approved"],
            "final_report": result["final_report"],
            "sources": result["sources"]
        }

    except HTTPException:
        raise

    except Exception:
        logger.exception("Unexpected error during research workflow")

        raise HTTPException(
            status_code=500,
            detail="Internal server error during research workflow"
        )