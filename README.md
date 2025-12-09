# todo-backend-fastapi

# Todo API (FastAPI + SQLite)

A simple but complete **RESTful API for managing Todo items**, built with **FastAPI** and **SQLite** using **SQLAlchemy** as the ORM.
The API supports:
- Full CRUD for todos
- Filtering by status & priority
- Search by title/description
- Sorting
- Pagination
- Tags for todos
- Automated tests with `pytest`

---

## 1. Tech Stack
- **Language:** Python 3.9+
- **Framework:** [FastAPI]
- **Web server :** [Uvicorn]
- **Database:** SQLite 
- **ORM:** SQLAlchemy
- **Schema Validation:** Pydantic
- **Testing:** pytest + FastAPI `TestClient`

---

## 2. Project Structure

```text
todo-api/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI app, routes, dependency wiring
│   ├── database.py      # DB engine, SessionLocal, Base
│   ├── models.py        # SQLAlchemy models (Todo, Tag, TodoTag link, etc.)
│   ├── schemas.py       # Pydantic models (request/response schemas)
│   ├── crud.py          # DB access logic for todos
│   └── config.py        # (optional) settings, DB URL, etc. if present
│
├── tests/
│   ├── __init__.py
│   └── test_todos.py    # pytest tests for Todo endpoints
│
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
