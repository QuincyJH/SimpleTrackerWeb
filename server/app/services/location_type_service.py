from typing import List
from app.repositories import location_type_repository
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.location_type import LocationType
from app.schemas.location_type_schema import LocationTypeCreateSchema

def get_location_type(location_type_id: int) -> LocationType:
    db: Session = next(get_db())
    return location_type_repository.get_location_type(db, location_type_id)

def update_location_type(location_type_id: int, location_type_data: dict) -> LocationType:
    db: Session = next(get_db())
    location_type = location_type_repository.update_location_type(db, location_type_id, location_type_data)
    return location_type

def delete_location_type(location_type_id: int) -> LocationType:
    db: Session = next(get_db())
    location_type = location_type_repository.delete_location_type(db, location_type_id)
    return location_type

def create_location_type(location_type_data: LocationTypeCreateSchema) -> LocationType:
    db: Session = next(get_db())
    location_type = location_type_repository.create_location_type(db, location_type_data)
    return location_type

def get_all_location_types() -> List[LocationType]:
    db: Session = next(get_db())
    return location_type_repository.get_all_location_types(db)