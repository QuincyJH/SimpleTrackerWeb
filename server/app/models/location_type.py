from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.base import Base

class LocationType(Base):
    __tablename__ = 'location_type'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    display_name = Column(String(255), nullable=False)

    locations = relationship("Location", back_populates="location_type")