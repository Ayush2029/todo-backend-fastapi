from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional, List
from .database import Base, engine, SessionLocal
from . import schemas, crud, models
Base.metadata.create_all(bind=engine)
app = FastAPI(title="Todo RESTAPI")
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.get("/")
def root():
    return "Todo API is running"
@app.post("/todos", response_model=schemas.TodoResponse, status_code=201)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db, todo)
@app.get("/todos", response_model=List[schemas.TodoResponse])
def list_todos(
    db: Session = Depends(get_db),
    status: str = Query("all", pattern="^(all|completed|pending)$"),
    priority: Optional[str] = None,
    search: Optional[str] = None,
    sort_by: Optional[str] = Query(None, pattern="^(due_date|priority|created_at)$"),
    page: int = 1,
    page_size: int = 10,
):
    skip = (page - 1) * page_size
    return crud.list_todos(db, status, priority, search, sort_by, skip, page_size)
@app.get("/todos/{id}", response_model=schemas.TodoResponse)
def get_todo(id: int, db: Session = Depends(get_db)):
    todo = crud.get_todo(db, id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo
@app.put("/todos/{id}", response_model=schemas.TodoResponse)
def update_todo(id: int, todo: schemas.TodoUpdate, db: Session = Depends(get_db)):
    updated = crud.update_todo(db, id, todo)
    if not updated:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated
@app.delete("/todos/{id}", status_code=204)
def delete_todo(id: int, db: Session = Depends(get_db)):
    result = crud.delete_todo(db, id)
    if not result:
        raise HTTPException(status_code=404, detail="Todo not found")
    return None