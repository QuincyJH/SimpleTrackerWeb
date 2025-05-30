from typing import List
from app.repositories import region_repository
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.region import Region
from app.serializer.region_serializer import serialize_region_with_locations
from app.schemas.region_schema import RegionCreateSchema

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

def create_region(region_data: RegionCreateSchema) -> Region:
    db: Session = next(get_db())
    region = region_repository.create_region(db, region_data)
    return region

def get_all_regions() -> List[Region]:
    db: Session = next(get_db())
    return region_repository.get_all_regions(db)

def get_region_by_name(name: str) -> Region:
    db: Session = next(get_db())
    return region_repository.get_region_by_name(db, name)

def bulk_create_regions(bulk_regions: List[RegionCreateSchema]):
    unique_regions = _get_unique_regions(bulk_regions)
    regions: List[Region] = []
    db: Session = next(get_db())
    for region in unique_regions:
        regions.append(region_repository.create_region(db, region))
    db.commit()
    return regions

def _get_unique_regions(regions: List[RegionCreateSchema]) -> List[RegionCreateSchema]:
    unique_regions = {}
    for region in regions:
        if region.name not in unique_regions:
            unique_regions[region.name] = region
    return list(unique_regions.values())

def get_locations_by_region(region_id: int) -> List[Region]:
    db: Session = next(get_db())
    return region_repository.get_locations_by_region(db, region_id)

def get_all_locations_by_region() -> List[Region]:
    db: Session = next(get_db())
    regions = region_repository.get_all_locations_by_region(db)
    return [serialize_region_with_locations(region) for region in regions]