from typing import List
from sqlalchemy.orm import Session
from app.models.location_type import LocationType
from app.schemas.location_schema import LocationCreateSchema

def get_location_type(db: Session, location_type_id: int) -> LocationType:
    return db.query(LocationType).filter(LocationType.id == location_type_id).first()

def update_location_type(db: Session, location_type_id: int, location_type_data: dict) -> LocationType:
    location_type = db.query(LocationType).filter(LocationType.id == location_type_id).first()
    if location_type:
        for key, value in location_type_data.items():
            setattr(location_type, key, value)
        db.commit()
        db.refresh(location_type)
    return location_type

def delete_location_type(db: Session, location_type_id: int) -> LocationType:
    location_type = db.query(LocationType).filter(LocationType.id == location_type_id).first()
    if location_type:
        db.delete(location_type)
        db.commit()
    return location_type

def create_location_type(db: Session, location_type_data: LocationCreateSchema) -> LocationType:
    location_type = LocationType(**location_type_data.model_dump(exclude_unset=True))
    db.add(location_type)
    db.commit
    db.refresh(location_type)
    return location_type

def get_all_location_types(db: Session) -> List[LocationType]:
    return db.query(LocationType).order_by(LocationType.name).all()

def get_location_type_by_name(db: Session, name: str) -> LocationType:
    return db.query(LocationType).filter(LocationType.name == name).first()