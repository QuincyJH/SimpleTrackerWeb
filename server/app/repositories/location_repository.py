from sqlalchemy.orm import Session
from app.models.location import Location

def get_location(db: Session, location_id: int) -> Location:
    return db.query(Location).filter(Location.id == location_id).first()

def update_location(db: Session, location_id: int, location_data: dict) -> Location:
    location = db.query(Location).filter(Location.id == location_id).first()
    if location:
        for key, value in location_data.items():
            setattr(location, key, value)
        db.commit()
        db.refresh(location)
    return location

def delete_location(db: Session, location_id: int) -> Location:
    location = db.query(Location).filter(Location.id == location_id).first()
    if location:
        db.delete(location)
        db.commit()
    return location

def create_location(db: Session, location_data: dict) -> Location:
    location = Location(**location_data)
    db.add(location)
    db.commit()

def get_all_locations(db: Session) -> list[Location]:
    return db.query(Location).all()

def get_location_by_name(db: Session, name: str) -> Location:
    return db.query(Location).filter(Location.name == name).first()