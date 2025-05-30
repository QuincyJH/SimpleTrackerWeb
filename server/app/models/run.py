from datetime import datetime, timezone
from sqlalchemy import Column, DateTime, Integer, String, func
from app.models.base import Base

def utcnow():
    return datetime.now(timezone.utc)

class Run(Base):
    __tablename__ = 'runs'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    data = Column(String)
    accessed_at = Column(DateTime(timezone=True), default=utcnow())
    modified_at = Column(DateTime(timezone=True), default=utcnow())
    created_at = Column(DateTime(timezone=True), default=utcnow())
