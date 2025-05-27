import json
from pathlib import Path
from typing import List
from fastapi import APIRouter, HTTPException
from app.services import region_service
from app.models.region_model import RegionModel
from app.schemas.region_schema import RegionSchema

router = APIRouter()

@router.get("/{region_id}", response_model=RegionSchema)
async def get_region(region_id: int):
    region = region_service.get_region(region_id)
    if region is None:
        raise HTTPException(status_code=404, detail="Region not found")

    return region

@router.put("/{region_id}", response_model=RegionSchema)
async def update_region(region_id: int, region_data: dict):
    region = region_service.update_region(region_id, region_data)
    if region is None:
        raise HTTPException(status_code=404, detail="Region not found")
    
    return region

@router.delete("/{region_id}", response_model=RegionSchema)
async def delete_region(region_id: int):
    region = region_service.delete_region(region_id)
    if region is None:
        raise HTTPException(status_code=404, detail="Region not found")
    
    return region

@router.post("/", response_model=RegionSchema)
async def create_region(region_data: dict):
    region = region_service.create_region(region_data)
    if region is None:
        raise HTTPException(status_code=400, detail="Failed to create region")
    
    return region

@router.get("/", response_model=List[RegionSchema])
async def get_all_regions():
    regions = region_service.get_all_regions()
    if not len(regions):
        raise HTTPException(status_code=404, detail="Regions not found")
    
    return regions

@router.get("/name/{name}", response_model=RegionSchema)
async def get_region_by_name(name: str):
    region = region_service.get_region_by_name(name)
    if region is None:
        raise HTTPException(status_code=404, detail="Region not found")
    
    return region

@router.get("/bulk-create/", response_model=List[RegionSchema])
async def bulk_create_items():
    regions_path = f"{Path(__file__).resolve().parent.parent}/assets/regions.json"
    with open(regions_path, "r") as file:
        data = json.load(file)

    if not data:
        raise HTTPException(status_code=404, detail="Regions not found")
    
    regions: List[RegionModel] = [RegionModel(**region) for region in data]
    region_service.bulk_create_regions(regions)
    return regions

@router.get("/get-locations-by-region/{region_id}", response_model=List[RegionSchema])
async def get_locations_by_region(region_id: int):
    locations = region_service.get_locations_by_region(region_id)
    if not len(locations):
        raise HTTPException(status_code=404, detail="Locations not found")
    
    return locations

@router.get("/get-all-locations-by-region/", response_model=List[RegionSchema])
async def get_all_locations_by_region():
    regions = region_service.get_all_locations_by_region()
    if not len(regions):
        raise HTTPException(status_code=404, detail="Regions not found")
    
    return regions