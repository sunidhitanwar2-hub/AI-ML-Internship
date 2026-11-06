
from pathlib import Path
import shutil
import uuid

from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel

from document_processor import extract_text, split_into_chunks
from rag_pipeline import (
    create_embeddings,
    retrieve_chunks,
    generate_answer
)


app = FastAPI(
    title="Company Documents RAG API",
    description="Upload documents and ask questions using AI.",
    version="1.0"
)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

# Store uploaded document information
document_store = {}


class QuestionRequest(BaseModel):
    question: str
    document_id: str


@app.get("/")
def home():
    return {
        "message": "Welcome to the Company Documents RAG API!",
        "docs": "/docs"
    }


@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    extension = Path(file.filename or "").suffix.lower()

    if extension not in [".pdf", ".txt"]:
        raise HTTPException(
            status_code=400,
            detail="Unsupported format. Please upload a PDF or TXT file."
        )

    document_id = str(uuid.uuid4())
    file_path = UPLOAD_DIR / f"{document_id}{extension}"

    try:
        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        if file_path.stat().st_size == 0:
            raise HTTPException(
                status_code=400,
                detail="The uploaded file is empty."
            )

        text = extract_text(file_path)

        if not text.strip():
            raise HTTPException(
                status_code=400,
                detail="No readable text found in the document."
            )

        chunks = split_into_chunks(text)

        if not chunks:
            raise HTTPException(
                status_code=400,
                detail="No text chunks could be created."
            )

        chunk_data = [
            {
                "text": chunk,
                "source": file.filename or "unknown"
            }
            for chunk in chunks
        ]

        embeddings = create_embeddings(chunks)

        document_store[document_id] = {
            "chunks": chunk_data,
            "embeddings": embeddings,
            "filename": file.filename
        }

        return {
            "message": "Document uploaded and processed successfully!",
            "document_id": document_id,
            "filename": file.filename,
            "total_chunks": len(chunks)
        }

    except HTTPException:
        file_path.unlink(missing_ok=True)
        raise

    except Exception as error:
        file_path.unlink(missing_ok=True)
        raise HTTPException(
            status_code=500,
            detail=f"Document processing failed: {str(error)}"
        )

    finally:
        await file.close()


@app.post("/ask")
def ask_question(request: QuestionRequest):

    if not request.question.strip():
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )

    document = document_store.get(request.document_id)

    if document is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found. Upload it first."
        )

    retrieved = retrieve_chunks(
        request.question,
        document["chunks"],
        document["embeddings"]
    )

    answer = generate_answer(request.question, retrieved)

    return {
        "question": request.question,
        "answer": answer,
        "sources": retrieved
    }
