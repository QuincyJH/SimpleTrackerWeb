from sqlalchemy.orm import Session
from app.models.region import Region

def get_region(db: Session, region_id: int) -> Region:
    return db.query(Region).filter(Region.id == region_id).first()

def update_region(db: Session, region_id: int, region_data: dict) -> Region:
    region = db.query(Region).filter(Region.id == region_id).first()
    if region:
        for key, value in region_data.items():
            setattr(region, key, value)
        db.commit()
        db.refresh(region)
    return region

def delete_region(db: Session, region_id: int) -> Region:
    region = db.query(Region).filter(Region.id == region_id).first()
    if region:
        db.delete(region)
        db.commit()
    return region

def create_region(db: Session, region_data: dict) -> Region:
    region = Region(**region_data)
    db.add(region)
    db.commit()
    db.refresh(region)
    return region

def get_all_regions(db: Session) -> list[Region]:
    return db.query(Region).all()

def get_region_by_name(db: Session, name: str) -> Region:
    return db.query(Region).filter(Region.name == name).first()