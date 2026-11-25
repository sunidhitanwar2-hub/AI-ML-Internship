# Code Review Report – Student Registration and Profiles Feature

**Project:** Student Management System with AI Features (company project, Day 27 plan)
**Feature:** Student registration and profiles (Task 5 in the Task Priority Table, Sprint 2), with project setup, database design and the backend API it needs (Tasks 2–4)
**Branch / pull request:** `feature/student-profiles` → `main`
**Reviewed version:** first version (`main.py`, a single file of 49 lines)
**Review areas:** code readability, modularity, naming conventions, documentation, error handling (plus security and testing)

## 1. Summary
The first version works when every request is correct. It has five endpoints that add, list, get, update and delete students in SQLite. The review found **15 issues**, including a security problem (SQL injection), crashes on normal input, and wrong responses when a student does not exist. All 15 are fixed in the improved version, which adds 10 automated API tests that all pass.

Severity: **High** = security risk, crash or wrong data. **Medium** = wrong behaviour or hard to maintain. **Low** = style or clarity.

## 2. Findings

### Error handling and security
| # | Severity | Finding in first version | Evidence (tested) | Fix in improved version |
|---|---|---|---|---|
| 1 | High | SQL built with f-strings from user input: **SQL injection**. | `GET /get/1 OR 1=1` returned a student; a name like `O'Brien` crashed with 500. | All queries use `?` placeholders (`crud.py`); test `test_sql_injection_text_is_stored_as_plain_text`. |
| 2 | High | Body is a plain `dict` with no validation; missing fields cause `KeyError`. | `POST /add {"name": "Riya"}` returned **500 Internal Server Error**. | Pydantic models in `schemas.py` give a clear **422** with the reason. |
| 3 | High | Same email could be registered twice. | Two identical `POST /add` calls both returned 200. | `email UNIQUE` in the table; the API returns **409 Conflict**. |
| 4 | Medium | Missing student returned `200 null` (get) or `200 "deleted"` (delete). | `GET /get/999` → 200 `null`; `DELETE /delete/999` → 200. | Returns **404 Not Found** with a message. |
| 5 | Medium | No checks on age, email format or empty names. | `age: "abc"` → 500. | Age 5–100, email pattern, name and course 2–100 characters, spaces trimmed, email lower-cased. |
| 6 | Medium | One global connection and cursor shared by all requests (`check_same_thread=False`). | Not safe when requests run at the same time. | New connection per request via the `get_db` dependency, always closed. |
| 7 | Medium | Update required every field and overwrote them all. | Partial update was impossible. | `PATCH /students/{id}` changes only the fields sent. |

### Modularity
| # | Severity | Finding | Fix |
|---|---|---|---|
| 8 | Medium | Everything was in `main.py`: database setup, SQL and routes. | Split into `config.py`, `database.py`, `schemas.py`, `crud.py`, `routers/students.py` and a small `main.py`. |
| 9 | Medium | Database created at import time with a hard-coded path. | Created at startup (`lifespan`). The path comes from the `DATABASE_PATH` environment variable (`.env.example`). |
| 10 | Low | Row-to-dict code repeated in two places. | One helper `_to_student()` and `sqlite3.Row` for access by column name. |

### Naming conventions
| # | Severity | Finding | Fix |
|---|---|---|---|
| 11 | Low | Names `c`, `d`, `r`, `res`. Function `all` hides Python's built-in `all()`, and `id` hides the built-in `id()`. | `connection`, `data`, `row`, `student_id`, `list_students`, `register_student`. |
| 12 | Low | Verb-style URLs (`/add`, `/get/{id}`, `/delete/{id}`) and 200 for everything. | REST style: `POST /students` (201), `GET /students`, `GET /students/{id}`, `PATCH /students/{id}`, `DELETE /students/{id}` (204). |

### Readability and documentation
| # | Severity | Finding | Fix |
|---|---|---|---|
| 13 | Low | No docstrings, type hints or API descriptions; one 150-character SQL line. | Module and function docstrings, type hints, examples in the models, readable multi-line schema. Swagger shows descriptions and error codes. |
| 14 | Low | No logging, so nothing to debug or audit. | `logging` set up in `main.py` (level from `LOG_LEVEL`); create, update and delete are logged. |
| 15 | Medium | No tests; `requirements.txt` had no versions. | `tests/test_students_api.py` with 10 tests, each on a temporary database; minimum versions in `requirements.txt`. |

## 3. Positive Points in the First Version
- The feature matched the plan: all CRUD operations for students were present.
- SQLite with `CREATE TABLE IF NOT EXISTS` was a good, simple start.
- FastAPI gave automatic Swagger docs from the beginning.

## 4. Verification
- Improved version: `python -m unittest discover -s tests -v` ran **10 tests, all passing** (24 Nov 2026). They cover register, duplicate email, invalid input, SQL-injection text, listing and pagination, 404s, partial update, delete and a non-numeric id.
- First version: the problems in the Evidence column were reproduced with FastAPI's `TestClient` on a scratch copy.

## 5. Pull Request Review Comments (to post on GitHub)
1. `main.py`: "Queries are built with f-strings. This allows SQL injection and breaks on names with apostrophes. Please use `?` placeholders."
2. `main.py`: "`d: dict` means no validation; a missing field gives a 500. Please add Pydantic request models."
3. `main.py`: "Email should be unique, and duplicates should return 409."
4. `main.py`: "Get and delete of a missing student should return 404, not 200."
5. `main.py`: "Please split database, models, queries and routes into separate modules, and add tests."

## 6. Next Steps (later sprints)
- Attendance and marks modules (Sprint 3) will link to `students.id`.
- Add authentication before the API is used outside development.
- Add a database migration tool once the schema starts to change.
