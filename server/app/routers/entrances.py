import json
from typing import List
from fastapi import HTTPException, APIRouter
from app.services import entrance_service
from pathlib import Path
from app.models.entrance_model import EntranceModel
from app.schemas.entrance_schema import EntranceSchema


router = APIRouter()

@router.get("/{entrance_id}", response_model=EntranceSchema)
async def get_entrance(entrance_id: int):
    entrance = entrance_service.get_entrance(entrance_id)
    if entrance is None:
        raise HTTPException(status_code=404, detail="Entrance not found")

    return entrance

@router.put("/{entrance_id}", response_model=EntranceSchema)
async def update_entrance(entrance_id: int, entrance_data: dict):
    entrance = entrance_service.update_entrance(entrance_id, entrance_data)
    if entrance is None:
        raise HTTPException(status_code=404, detail="Entrance not found")
    
    return entrance

@router.delete("/{entrance_id}", response_model=EntranceSchema)
async def delete_entrance(entrance_id: int):
    entrance = entrance_service.delete_entrance(entrance_id)
    if entrance is None:
        raise HTTPException(status_code=404, detail="Entrance not found")
    
    return entrance

@router.post("/", response_model=EntranceSchema)
async def create_entrance(entrance_data: dict):
    entrance = entrance_service.create_entrance(entrance_data)
    if entrance is None:
        raise HTTPException(status_code=400, detail="Failed to create entrance")
    
    return entrance

@router.get("/", response_model=List[EntranceSchema])
async def get_all_entrances():
    entrances = entrance_service.get_all_entrances()
    if not len(entrances):
        raise HTTPException(status_code=404, detail="Entrance not found")
    
    return entrances

@router.get("/name/{name}", response_model=EntranceSchema)
async def get_entrance_by_name(name: str):
    entrance = entrance_service.get_entrance_by_name(name)
    if entrance is None:
        raise HTTPException(status_code=404, detail="Entrance not found")
    
    return entrance

@router.get("/type/{entrance_type}", response_model=List[EntranceSchema])
async def get_entrances_by_type(entrance_type: str):
    entrances = entrance_service.get_entrances_by_type(entrance_type)
    if not len(entrances):
        raise HTTPException(status_code=404, detail="Entrance not found")
    
    return entrances

@router.get("/bulk-create/", response_model=List[EntranceSchema])
async def bulk_create_entrances():
    entrances_path = f"{Path(__file__).resolve().parent.parent}/assets/entrances.json"
    with open(entrances_path, "r") as file:
        data = json.load(file)

    if not data:
        raise HTTPException(status_code=404, detail="Entrance not found")

    entrances: List[EntranceModel] = [EntranceModel(**entrance) for entrance in data]
    entrance_service.bulk_create_entrances(entrances)
    return entrances

