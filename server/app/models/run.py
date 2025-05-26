from sqlalchemy import Column, DateTime, Integer, String, func
from app.models.base import Base

class Run(Base):
    __tablename__ = 'runs'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    data = Column(String)
    accessed_at = Column(DateTime, server_default=func.now())
    modified_at = Column(DateTime, server_default=func.now())
    created_at = Column(DateTime, server_default=func.now())