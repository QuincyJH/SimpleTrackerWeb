from sqlalchemy import Column, ForeignKey, Integer, String
from app.models.base import Base
from sqlalchemy.orm import relationship

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    display_name = Column(String(255), nullable=False)
    item_type_id = Column(Integer, ForeignKey("item_type.id"))

    item_type = relationship("ItemType", back_populates="items")