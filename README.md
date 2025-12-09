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

Role of each file: <br>
1] `app/main.py` <br>
- Creates the FastAPI application instance. <br>
- Defines the root health-check route `/`. <br>
- Implements all Todo routes:<br>
    (a) `POST /todos` – create<br>
    (b) `GET /todos` – list with filters/search/sort/pagination<br>
    (c) `GET /todos/{id}` – retrieve by ID<br>
    (d) `PUT /todos/{id}` – update<br>
    (e) `DELETE /todos/{id}` – delete<br>
- Handles dependency injection for database sessions.<br>

2] `app/database.py`<br>
- Defines `SQLALCHEMY_DATABASE_URL` (SQLite).<br>
- Creates the SQLAlchemy engine.<br>
- Defines `SessionLocal` for DB sessions.<br>
- Declares `Base` for models to inherit from.<br>

3] `app/models.py`<br>
- Defines ORM models:<br>
    (a) Todo model with fields:<br>
        - id <br>
        - title<br>
        - description<br>
        - due_date<br>
        - priority <br>
        - is_completed<br>
        - created_at<br>
        - updated_at<br>
    (b) Tag model and the many-to-many relationship.<br>
- Adds relationships if using a join table for tags.<br>

4] `app/schemas.py`<br>
- Pydantic models for validation & serialization:<br>
    (a) TodoBase <br>
    (b) TodoCreate<br>
    (c) TodoUpdate<br>
    (d) TodoRead<br>
    (e) Tag / TagCreate if needed<br>
- These ensure:<br>
    (a) title is required and non-empty.<br>
    (b) priority is one of: low, medium, high (default: medium).<br>
    (c) is_completed defaults to False.<br>
    (d) Timestamps are auto-set in responses.<br>

5] `app/crud.py`<br>
- Encapsulates database operations:<br>
    (a) create_todo<br>
    (b) get_todo<br>
    (c) list_todos (with filters/search/sort/pagination)<br>
    (d) update_todo<br>
    (e) delete_todo<br>
- Keeps business logic separate from the API layer.<br>

6] `tests/test_todos.py`<br>
- Uses pytest and TestClient to test:<br>
    (a) Creating a todo (201)<br>
    (b) Fetching todos (200)<br>
    (c) Fetching non-existing todo → 404<br>
- Can be extended with more edge cases.<br>

7] requirement.txt<br>
- Contains all required dependencies:<br>
    (a) fastapi<br>
    (b) uvicorn<br>
    (c) sqlalchemy<br>
    (d) pydantic<br>
    (e) pytest<br>
    (f) httpx<br>

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
