from typing import List
from app.repositories import location_repository, region_repository
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.location import Location
from app.utils.helpers import to_snake_case
from app.schemas.location_schema import LocationCreateSchema
from app.repositories import location_type_repository

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

def create_location(location_data: LocationCreateSchema) -> Location:
    db: Session = next(get_db())
    location_type = location_type_repository.get_location_type_by_name(db, location_data.location_type)
    region = region_repository.get_region_by_name(db, location_data.region_name)
    location = location_repository.create_location(db, location_data, location_type.id if location_type else None, region.id if region else None)
    return location

def get_all_locations() -> list[Location]:
    db: Session = next(get_db())
    return location_repository.get_all_locations(db)

def get_location_by_name(name: str) -> Location:
    db: Session = next(get_db())
    return location_repository.get_location_by_name(db, name)

def bulk_create_locations(bulk_locations: List[LocationCreateSchema]):
    db: Session = next(get_db())
    locations: List[Location] = []
    for location in bulk_locations:
        location_type = location_type_repository.get_location_type_by_name(db, location.location_type)
        region = region_repository.get_region_by_name(db, location.region_name)
        locations.append(location_repository.create_location(db, location, location_type.id if location_type else None, region.id if region else None))
    db.commit()
    return locations
