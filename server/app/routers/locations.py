import json
from pathlib import Path
from typing import List
from fastapi import APIRouter, HTTPException
from app.services import location_service
from app.models.location_model import LocationModel

router = APIRouter()

@router.get("/{location_id}")
async def get_location(location_id: int):
    location = location_service.get_location(location_id)
    if location is None:
        raise HTTPException(status_code=404, detail="Location not found")

    return location

@router.put("/{location_id}")
async def update_location(location_id: int, location_data: dict):
    location = location_service.update_location(location_id, location_data)
    if location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    
    return location

@router.delete("/{location_id}")
async def delete_location(location_id: int):
    location = location_service.delete_location(location_id)
    if location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    
    return location

@router.post("/")
async def create_location(location_data: dict):
    location = location_service.create_location(location_data)
    if location is None:
        raise HTTPException(status_code=400, detail="Failed to create location")
    
    return location
@router.get("/")
async def get_all_locations():
    locations = location_service.get_all_locations()
    if not len(locations):
        raise HTTPException(status_code=404, detail="Locations not found")
    
    return locations
@router.get("/name/{name}")
async def get_location_by_name(name: str):
    location = location_service.get_location_by_name(name)
    if location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    
    return location

@router.get("/bulk-create/")
async def bulk_create_items():
    locations_path = f"{Path(__file__).resolve().parent.parent}/assets/locations.json"
    with open(locations_path, "r") as file:
        data = json.load(file)

    if not data:
        raise HTTPException(status_code=404, detail="Location not found")

    location: List[LocationModel] = [LocationModel(**location) for location in data]
    location_service.bulk_create_items(location)
    return location