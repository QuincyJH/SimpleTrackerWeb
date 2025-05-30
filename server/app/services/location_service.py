from typing import List
from app.repositories import location_repository, region_repository
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.location import Location
from app.utils.helpers import to_snake_case
from app.schemas.location_schema import LocationCreateSchema

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
    location = location_repository.create_location(db, location_data)
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
        region = region_repository.get_region_by_name(db, to_snake_case(location.region_name))
        if not region:
            raise ValueError(f"Region {location.region_name} does not exist.")
        locations.append(location_repository.create_location_with_region(db, location, region.id))
    db.commit()
    return locations
