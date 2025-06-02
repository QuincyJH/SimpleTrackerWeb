from typing import List
from fastapi import APIRouter, HTTPException
from app.services import location_type_service
from app.schemas.location_type_schema import LocationTypeCreateSchema, LocationTypeSchema

router = APIRouter()

@router.get("/{location_type_id}", response_model=LocationTypeSchema)
async def get_run(location_type_id: int):
    location_type = location_type_service.get_location_type(location_type_id)
    if location_type is None:
        raise HTTPException(status_code=404, detail="Location type not found")
    
    return location_type

@router.put("/{location_type_id}", response_model=LocationTypeSchema)
async def update_location_type(location_type_id: int, location_type_data: dict):
    location_type = location_type_service.update_location_type(location_type_id, location_type_data)
    if location_type is None:
        raise HTTPException(status_code=404, detail="Location type not found")
    
    return location_type

@router.delete("/{location_type_id}", response_model=LocationTypeSchema)
async def delete_location_type(location_type_id: int):
    location_type = location_type_service.delete_location_type(location_type_id)
    if location_type is None:
        raise HTTPException(status_code=404, detail="Location type not found")
    
    return location_type

@router.post("/", response_model=LocationTypeSchema)
async def create_location_type(location_type_data: LocationTypeCreateSchema):
    location_type = location_type_service.create_location_type(location_type_data)
    if location_type is None:
        raise HTTPException(status_code=400, detail="Failed to create location type")
    
    return location_type

@router.get("/", response_model=List[LocationTypeSchema])
async def get_all_location_types():
    location_types = location_type_service.get_all_location_types()
    if not len(location_types):
        raise HTTPException(status_code=404, detail="Location types not found")
    return location_types