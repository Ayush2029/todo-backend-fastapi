# Todo API (FastAPI + SQLite)

A simple **RESTful API for managing Todo items**, built with **FastAPI** and **SQLite** using **SQLAlchemy** as the ORM.
The API supports:
- Full CRUD for todos
- Filtering by status & priority
- Search by title/description
- Sorting
- Pagination
- Tags for todos
- Automated tests with pytest

---

## 1. Tech Stack
- **Language:** Python 3.9+
- **Framework:** [FastAPI]
- **Web server :** [Uvicorn]
- **Database:** SQLite 
- **ORM:** SQLAlchemy
- **Schema Validation:** Pydantic
- **Testing:** pytest + FastAPI

---

## 2. Project Structure

```text
todo-api/
├── app/
│   ├── __init__.py
│   ├── main.py          
│   ├── database.py      
│   ├── models.py        
│   ├── schemas.py       
│   ├── crud.py                
│
├── tests/
│   ├── __init__.py
│   └── test_todos.py    
│
├── requirements.txt     
└── README.md            
```
```text
Role of each file:
1] `app/main.py`
- Creates the FastAPI application instance.
- Defines the root health-check route `/`.
- Implements all Todo routes:
    (a) `POST /todos` – create
    (b) `GET /todos` – list with filters/search/sort/pagination
    (c) `GET /todos/{id}` – retrieve by ID
    (d) `PUT /todos/{id}` – update
    (e) `DELETE /todos/{id}` – delete
- Handles dependency injection for database sessions.

2] `app/database.py`
- Defines `SQLALCHEMY_DATABASE_URL` (SQLite).
- Creates the SQLAlchemy engine.
- Defines `SessionLocal` for DB sessions.
- Declares `Base` for models to inherit from.

3] `app/models.py`
- Defines ORM models:
    (a) Todo model with fields:
        - id 
        - title
        - description
        - due_date
        - priority 
        - is_completed
        - created_at
        - updated_at
    (b) Tag model and the many-to-many relationship.
- Adds relationships if using a join table for tags.

4] `app/schemas.py`
- Pydantic models for validation & serialization:
    (a) TodoBase
    (b) TodoCreate
    (c) TodoUpdate
    (d) TodoRead
    (e) Tag / TagCreate if needed
- These ensure:
    (a) title is required and non-empty.
    (b) priority is one of: low, medium, high (default: medium).
    (c) is_completed defaults to False.
    (d) Timestamps are auto-set in responses.

5] `app/crud.py`
- Encapsulates database operations:
    (a) create_todo
    (b) get_todo
    (c) list_todos (with filters/search/sort/pagination)
    (d) update_todo
    (e) delete_todo
- Keeps business logic separate from the API layer.

6] `tests/test_todos.py`
- Uses pytest and TestClient to test:
    (a) Creating a todo (201)
    (b) Fetching todos (200)
    (c) Fetching non-existing todo → 404
- Can be extended with more edge cases.

7] requirement.txt
- Contains all required dependencies:
    (a) fastapi
    (b) uvicorn
    (c) sqlalchemy
    (d) pydantic
    (e) pytest
    (f) httpx
```

## 3. Setup & Installation

These steps assume macOS and Python 3.9+ is installed and available as python or python3

**3.1. Clone the repository**
```
cd /path/where/you/want/the/project
git clone <your-repo-url> todo-api
cd todo-api
```
**3.2. Install dependencies (without venv)**
You mentioned not using a virtual environment, so you can install directly:
```
pip install -r requirements.txt
```
If your pip points to a different Python, you can use:
```
python3 -m pip install -r requirements.txt
```
Note: Using a virtualenv is generally recommended, but this project works fine without one as well.

## 4. Running the Application
From the project root (same folder as requirements.txt):
```
uvicorn app.main:app --reload
```
1]  app.main:app = app package → main.py module → app variable. <br>
2] --reload = auto-reload on code changes (development mode). <br>
