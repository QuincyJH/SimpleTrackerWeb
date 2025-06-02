from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.models.base import Base

class Location(Base):
    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    display_name = Column(String(255), nullable=False)
    region_id = Column(Integer, ForeignKey("regions.id"))
    location_type_id = Column(Integer, ForeignKey("location_type.id"))

    region = relationship("Region", back_populates="locations")
    location_type = relationship("LocationType", back_populates="locations")