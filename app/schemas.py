from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from .models import PriorityEnum
class TodoBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    priority: Optional[PriorityEnum] = PriorityEnum.medium
    is_completed: Optional[bool] = False
    tags: Optional[List[str]] = []
class TodoCreate(TodoBase):
    title: str = Field(..., min_length=1)
class TodoUpdate(TodoBase):
    pass  
class TodoResponse(TodoBase):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    class Config:
        orm_mode = True