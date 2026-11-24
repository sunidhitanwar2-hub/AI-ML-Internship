"""Database operations for students.

All SQL uses ? placeholders, so user input is never pasted into a query.
Functions raise StudentNotFoundError / DuplicateEmailError instead of
returning None, so the API layer can turn them into clear HTTP errors.
"""

import logging
import sqlite3

from schemas import Student, StudentCreate, StudentUpdate

logger = logging.getLogger(__name__)

# Only these column names may ever appear in an UPDATE statement.
UPDATABLE_COLUMNS = ("name", "email", "age", "course")


class StudentNotFoundError(Exception):
    def __init__(self, student_id: int):
        super().__init__(f"Student {student_id} not found.")
        self.student_id = student_id


class DuplicateEmailError(Exception):
    def __init__(self, email: str):
        super().__init__(f"A student with email {email} already exists.")
        self.email = email


def _to_student(row: sqlite3.Row) -> Student:
    return Student(**dict(row))


def create_student(db: sqlite3.Connection, data: StudentCreate) -> Student:
    try:
        with db:
            cursor = db.execute(
                "INSERT INTO students (name, email, age, course) VALUES (?, ?, ?, ?)",
                (data.name, data.email, data.age, data.course),
            )
    except sqlite3.IntegrityError as error:
        raise DuplicateEmailError(data.email) from error
    logger.info("Created student %s", cursor.lastrowid)
    return get_student(db, cursor.lastrowid)


def list_students(db: sqlite3.Connection, skip: int = 0, limit: int = 50) -> list[Student]:
    rows = db.execute(
        "SELECT * FROM students ORDER BY id LIMIT ? OFFSET ?", (limit, skip)
    ).fetchall()
    return [_to_student(row) for row in rows]


def get_student(db: sqlite3.Connection, student_id: int) -> Student:
    row = db.execute("SELECT * FROM students WHERE id = ?", (student_id,)).fetchone()
    if row is None:
        raise StudentNotFoundError(student_id)
    return _to_student(row)


def update_student(db: sqlite3.Connection, student_id: int, data: StudentUpdate) -> Student:
    changes = {
        column: value
        for column, value in data.model_dump(exclude_unset=True).items()
        if column in UPDATABLE_COLUMNS and value is not None
    }
    if not changes:
        return get_student(db, student_id)  # nothing to change; 404 if missing

    assignments = ", ".join(f"{column} = ?" for column in changes)
    try:
        with db:
            cursor = db.execute(
                f"UPDATE students SET {assignments} WHERE id = ?",
                (*changes.values(), student_id),
            )
    except sqlite3.IntegrityError as error:
        raise DuplicateEmailError(changes.get("email", "")) from error
    if cursor.rowcount == 0:
        raise StudentNotFoundError(student_id)
    logger.info("Updated student %s: %s", student_id, ", ".join(changes))
    return get_student(db, student_id)


def delete_student(db: sqlite3.Connection, student_id: int) -> None:
    with db:
        cursor = db.execute("DELETE FROM students WHERE id = ?", (student_id,))
    if cursor.rowcount == 0:
        raise StudentNotFoundError(student_id)
    logger.info("Deleted student %s", student_id)
