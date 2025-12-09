from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import List, Optional
from . import models, schemas
def create_todo(db: Session, data: schemas.TodoCreate):
    todo = models.Todo(**data.dict())
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo
def get_todo(db: Session, todo_id: int):
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()
def delete_todo(db: Session, todo_id: int):
    todo = get_todo(db, todo_id)
    if todo:
        db.delete(todo)
        db.commit()
        return True
    return False
def update_todo(db: Session, todo_id: int, data: schemas.TodoUpdate):
    todo = get_todo(db, todo_id)
    if not todo:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(todo, key, value)
    db.commit()
    db.refresh(todo)
    return todo
def list_todos(
    db: Session,
    status: str,
    priority: Optional[str],
    search: Optional[str],
    sort_by: Optional[str],
    skip: int,
    limit: int
):
    query = db.query(models.Todo)
    if status == "completed":
        query = query.filter(models.Todo.is_completed == True)
    elif status == "pending":
        query = query.filter(models.Todo.is_completed == False)
    if priority:
        query = query.filter(models.Todo.priority == priority)
    if search:
        query = query.filter(
            or_(
                models.Todo.title.contains(search),
                models.Todo.description.contains(search)
            )
        )
    if sort_by in ["due_date", "priority", "created_at"]:
        query = query.order_by(getattr(models.Todo, sort_by))
    return query.offset(skip).limit(limit).all()