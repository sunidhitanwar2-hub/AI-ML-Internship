"""SQLite connection handling and schema creation."""

import sqlite3
from collections.abc import Iterator

from config import get_database_path

SCHEMA = """
CREATE TABLE IF NOT EXISTS students (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    name    TEXT    NOT NULL,
    email   TEXT    NOT NULL UNIQUE,
    age     INTEGER NOT NULL CHECK (age BETWEEN 5 AND 100),
    course  TEXT    NOT NULL
)
"""


def connect(path: str | None = None) -> sqlite3.Connection:
    """Open a connection whose rows can be read by column name."""
    connection = sqlite3.connect(path or get_database_path())
    connection.row_factory = sqlite3.Row
    return connection


def init_db(path: str | None = None) -> None:
    """Create the tables if they do not exist yet."""
    connection = connect(path)
    try:
        with connection:  # commits on success, rolls back on error
            connection.execute(SCHEMA)
    finally:
        connection.close()


def get_db() -> Iterator[sqlite3.Connection]:
    """FastAPI dependency: one connection per request, always closed."""
    connection = connect()
    try:
        yield connection
    finally:
        connection.close()
