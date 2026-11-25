"""Application settings, read from environment variables.

DATABASE_PATH  SQLite file to use (default: students.db)
LOG_LEVEL      Logging level such as DEBUG, INFO, WARNING (default: INFO)
"""

import os

DEFAULT_DATABASE_PATH = "students.db"
DEFAULT_LOG_LEVEL = "INFO"


def get_database_path() -> str:
    """Read on every call so tests can point the app at a temporary database."""
    return os.environ.get("DATABASE_PATH", DEFAULT_DATABASE_PATH)


def get_log_level() -> str:
    return os.environ.get("LOG_LEVEL", DEFAULT_LOG_LEVEL).upper()
