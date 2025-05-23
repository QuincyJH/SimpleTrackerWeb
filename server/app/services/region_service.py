from typing import List
from app.repositories import region_repository
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.region import Region
from app.models.region_model import RegionModel

def get_region(region_id: int) -> Region:
    db: Session = next(get_db())
    return region_repository.get_region(db, region_id)

def update_region(region_id: int, region_data: dict) -> Region:
    db: Session = next(get_db())
    region = region_repository.update_region(db, region_id, region_data)
    return region

def delete_region(region_id: int) -> Region:
    db: Session = next(get_db())
    region = region_repository.delete_region(db, region_id)
    return region

def create_region(region_data: dict) -> Region:
    db: Session = next(get_db())
    region = region_repository.create_region(db, region_data)
    return region

def get_all_regions() -> List[Region]:
    db: Session = next(get_db())
    return region_repository.get_all_regions(db)

def get_region_by_name(name: str) -> Region:
    db: Session = next(get_db())
    return region_repository.get_region_by_name(db, name)

def bulk_create_regions(regions: List[RegionModel]):
    unique_regions = _get_unique_regions(regions)

    db: Session = next(get_db())
    for region in unique_regions:
        region_repository.create_region(db, region.__dict__)
    db.commit()
    return regions

def _get_unique_regions(regions: List[RegionModel]) -> List[RegionModel]:
    unique_regions = {}
    for region in regions:
        if region.name not in unique_regions:
            unique_regions[region.name] = region
    return list(unique_regions.values())
