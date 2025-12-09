from sqlalchemy import Column, Integer, String, DateTime, Boolean, Enum, TEXT
from sqlalchemy.sql import func
from sqlalchemy.types import JSON
import enum
from .database import Base
class PriorityEnum(str, enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"
class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(TEXT, nullable=True)
    due_date = Column(DateTime, nullable=True)
    priority = Column(Enum(PriorityEnum), default=PriorityEnum.medium)
    is_completed = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    tags = Column(JSON, default=[])