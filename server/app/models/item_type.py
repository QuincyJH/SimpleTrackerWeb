from sqlalchemy import Column, Integer, String
from app.models.base import Base
from sqlalchemy.orm import relationship

class ItemType(Base):
    __tablename__ = 'item_type'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    display_name = Column(String(255), nullable=False)

    items = relationship("Item", back_populates="item_type")