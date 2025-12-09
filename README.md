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

## 4. Architecture Overview
**4.1. Layers** <br>
1] API Layer: <br>
• Defines endpoints and query parameters. <br>
• Uses Pydantic schemas for request & response models. <br>
• Handles HTTP concerns (status codes, error messages). <br>
2] CRUD Layer: <br>
• Contains the core logic for interacting with the database: <br>
&nbsp;&nbsp;(a) Filtering by status/priority. <br>
&nbsp;&nbsp;(b) Search by title/description. <br>
&nbsp;&nbsp;(c) Sorting and pagination. <br>
• Keeps DB operations separate and reusable. <br>
3] Data Layer: <br>
• models.py: SQLAlchemy models mapping to DB tables. <br>
• database.py: engine + session management + Base. <br>
4] Validation / Serialization Layer: <br>
• Defines what clients can send and what they receive. <br>
• Enforces constraints like required title, valid priority, etc. <br>
5] Tests: <br>
• Ensures behavior is correct and stable. <br>
• Makes refactoring safer. <br><br>
**4.2. Error Handling** <br>
(a) Uses HTTPException from FastAPI for controlled errors: <br>
• Returns 404 when a Todo is not found. <br>
(b) Relies on FastAPI/Pydantic for validation errors → returns 422 with structured details. <br>
(c) Does not expose raw stack traces to the client. <br>


## 5. Running the Application
From the project root (same folder as requirements.txt):
```
uvicorn app.main:app --reload
```
1]  app.main:app = app package → main.py module → app variable. <br>
2] --reload = auto-reload on code changes (development mode). <br>

By default, the app runs at: <br>
Base URL: ```http://127.0.0.1:8000/```
<br>

**5.1. Health check**
Open this in your browser: <br>
```GET http://127.0.0.1:8000/ <br>```
You should see a simple JSON response like:
```
{
  "message": "Todo API is running"
}
```
 **5.2 API Docs**
 FastAPI automatically provides docs:
 ```http://127.0.0.1:8000/docs <br>```
From this UI, you can: <br>
- Explore all endpoints <br>
- Send requests <br>
- Inspect responses and status codes <br>

## 6. HTTP Status Codes Used
(a) 201 Created <br>
• Successful creation of a todo (POST /todos) <br>
(b) 200 OK <br>
• Successful read or update: <br>
&nbsp;&nbsp;- GET /todos <br>
&nbsp;&nbsp;- GET /todos/{id} <br>
&nbsp;&nbsp;- PUT /todos/{id} <br>
(c) 204 No Content <br>
• Successful delete with no response body: <br>
&nbsp;&nbsp;- DELETE /todos/{id} <br>
(d) 404 Not Found <br>
• Todo with the given ID does not exist. <br>
(e) 422 Unprocessable Entity <br>
• Validation errors (invalid data), automatically handled by FastAPI/Pydantic. <br>

## 7. Running Tests
From the project root, run: <br>
```pytest -q <br> ```
or: <br>
```python -m pytest -q```

• -q = quiet mode (less verbose). <br>
• The tests use TestClient from FastAPI to: <br>
- Create a todo and assert 201. <br>
- Fetch todos and assert 200. <br>
- Attempt to fetch a non-existent todo and assert 404. <br>

You do not need a separate terminal to run tests, but it is convenient to: <br>
• Run the API server in one terminal (for manual testing via Postman/Browser). <br>
• Run pytest in another terminal (for automated test execution). <br>

## 8. How to Manually Verify All Features
You can verify using: <br>
- Swagger UI at ```/docs``` <br>
- curl from terminal <br>
- Postman / Insomnia / any REST client <br>
