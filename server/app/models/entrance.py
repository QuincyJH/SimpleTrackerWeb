from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Entrance(Base):
    __tablename__ = 'entrances'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    display_name = Column(String(255), nullable=False)
    entrance_type = Column(String(50), nullable=True)
