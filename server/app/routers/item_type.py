from typing import List
from fastapi import HTTPException, APIRouter
from app.services import entrance_service
from app.schemas.item_type_schema import ItemTypeCreateSchema, ItemTypeSchema


router = APIRouter()

@router.get("/{item_type_id}", response_model=ItemTypeSchema)
async def get_entrance(item_type_id: int):
    item_type = entrance_service.get_entrance(item_type_id)
    if item_type is None:
        raise HTTPException(status_code=404, detail="Item type not found")
    
    return item_type

@router.put("/{item_type_id}", response_model=ItemTypeSchema)
async def update_entrance(item_type_id: int, item_type_data: dict):
    item_type = entrance_service.update_entrance(item_type_id, item_type_data)
    if item_type is None:
        raise HTTPException(status_code=404, detail="Item type not found")
    
    return item_type

@router.delete("/{item_type_id}", response_model=ItemTypeSchema)
async def delete_entrance(item_type_id: int):
    item_type = entrance_service.delete_entrance(item_type_id)
    if item_type is None:
        raise HTTPException(status_code=404, detail="Item type not found")
    
    return item_type

@router.post("/", response_model=ItemTypeSchema)
async def create_entrance(item_type_data: ItemTypeCreateSchema):
    item_type = entrance_service.create_entrance(item_type_data)
    if item_type is None:
        raise HTTPException(status_code=400, detail="Failed to create item type")
    
    return item_type

@router.get("/", response_model=List[ItemTypeSchema])
async def get_all_entrances():
    item_types = entrance_service.get_all_entrances()
    if not len(item_types):
        raise HTTPException(status_code=404, detail="Item types not found")
    
    return item_types

@router.get("/name/{name}", response_model=ItemTypeSchema)
async def get_entrance_by_name(name: str):
    item_type = entrance_service.get_entrance_by_name(name)
    if item_type is None:
        raise HTTPException(status_code=404, detail="Item type not found")
    
    return item_type