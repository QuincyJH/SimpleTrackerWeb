from typing import List
from app.repositories import location_repository
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.location import Location
from app.models.location_model import LocationModel

def get_location(location_id: int) -> Location:
    db: Session = next(get_db())
    return location_repository.get_location(db, location_id)

def update_location(location_id: int, location_data: dict) -> Location:
    db: Session = next(get_db())
    location = location_repository.update_location(db, location_id, location_data)
    return location

def delete_location(location_id: int) -> Location:
    db: Session = next(get_db())
    location = location_repository.delete_location(db, location_id)
    return location

def create_location(location_data: dict) -> Location:
    db: Session = next(get_db())
    location = location_repository.create_location(db, location_data)
    return location

def get_all_locations() -> list[Location]:
    db: Session = next(get_db())
    return location_repository.get_all_locations(db)

def get_location_by_name(name: str) -> Location:
    db: Session = next(get_db())
    return location_repository.get_location_by_name(db, name)

def bulk_create_locations(locations: List[LocationModel]):
    db: Session = next(get_db())
    for location in locations:
        location_repository.create_location(db, location.__dict__)
    db.commit()
    return locations
