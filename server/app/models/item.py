from sqlalchemy import Column, Integer, String
from app.models.base import Base

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    display_name = Column(String(255), nullable=False)
    item_type = Column(String(50), nullable=True)