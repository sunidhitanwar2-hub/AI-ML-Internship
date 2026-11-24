"""HTTP endpoints for student registration and profiles."""

import sqlite3

from fastapi import APIRouter, Depends, HTTPException, Query, Response, status

import crud
from database import get_db
from schemas import Student, StudentCreate, StudentUpdate

router = APIRouter(prefix="/students", tags=["Students"])

NOT_FOUND = {404: {"description": "Student not found"}}
CONFLICT = {409: {"description": "Email already registered"}}


@router.post("", response_model=Student, status_code=status.HTTP_201_CREATED, responses=CONFLICT)
def register_student(data: StudentCreate, db: sqlite3.Connection = Depends(get_db)) -> Student:
    """Register a new student."""
    try:
        return crud.create_student(db, data)
    except crud.DuplicateEmailError as error:
        raise HTTPException(status.HTTP_409_CONFLICT, str(error)) from error


@router.get("", response_model=list[Student])
def list_students(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(50, ge=1, le=100, description="Maximum records to return"),
    db: sqlite3.Connection = Depends(get_db),
) -> list[Student]:
    """List students, a page at a time."""
    return crud.list_students(db, skip, limit)


@router.get("/{student_id}", response_model=Student, responses=NOT_FOUND)
def get_student(student_id: int, db: sqlite3.Connection = Depends(get_db)) -> Student:
    """Get one student's profile."""
    try:
        return crud.get_student(db, student_id)
    except crud.StudentNotFoundError as error:
        raise HTTPException(status.HTTP_404_NOT_FOUND, str(error)) from error


@router.patch("/{student_id}", response_model=Student, responses={**NOT_FOUND, **CONFLICT})
def update_student(
    student_id: int, data: StudentUpdate, db: sqlite3.Connection = Depends(get_db)
) -> Student:
    """Update some or all fields of a student's profile."""
    try:
        return crud.update_student(db, student_id, data)
    except crud.StudentNotFoundError as error:
        raise HTTPException(status.HTTP_404_NOT_FOUND, str(error)) from error
    except crud.DuplicateEmailError as error:
        raise HTTPException(status.HTTP_409_CONFLICT, str(error)) from error


@router.delete("/{student_id}", status_code=status.HTTP_204_NO_CONTENT, responses=NOT_FOUND)
def delete_student(student_id: int, db: sqlite3.Connection = Depends(get_db)) -> Response:
    """Delete a student."""
    try:
        crud.delete_student(db, student_id)
    except crud.StudentNotFoundError as error:
        raise HTTPException(status.HTTP_404_NOT_FOUND, str(error)) from error
    return Response(status_code=status.HTTP_204_NO_CONTENT)
