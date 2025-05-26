from sqlalchemy import Column, Integer, String
from app.models.base import Base

class Run(Base):
    __tablename__ = 'runs'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    data = Column(String)
    accessed_at = Column(String, default='CURRENT_TIMESTAMP')
    modified_at = Column(String, default='CURRENT_TIMESTAMP')
    created_at = Column(String, default='CURRENT_TIMESTAMP')