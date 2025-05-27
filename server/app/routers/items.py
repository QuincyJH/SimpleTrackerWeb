import json
from pathlib import Path
from typing import List
from fastapi import APIRouter, HTTPException
from app.services import item_service
from app.models.item_model import ItemModel
from app.schemas.item_schema import ItemSchema

router = APIRouter()

@router.get("/{item_id}", response_model=ItemSchema)
async def get_item(item_id: int):
    item = item_service.get_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return item

@router.put("/{item_id}", response_model=ItemSchema)
async def update_item(item_id: int, item_data: dict):
    item = item_service.update_item(item_id, item_data)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return item

@router.delete("/{item_id}", response_model=ItemSchema)
async def delete_item(item_id: int):
    item = item_service.delete_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return item

@router.post("/", response_model=ItemSchema)
async def create_item(item_data: dict):
    item = item_service.create_item(item_data)
    if item is None:
        raise HTTPException(status_code=400, detail="Failed to create item")
    
    return item

@router.get("/", response_model=List[ItemSchema])
async def get_all_items():
    items = item_service.get_all_items()
    if not len(items):
        raise HTTPException(status_code=404, detail="Items not found")
    
    return items

@router.get("/name/{name}", response_model=ItemSchema)
async def get_item_by_name(name: str):
    item = item_service.get_item_by_name(name)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return item

@router.get("/type/{item_type}", response_model=List[ItemSchema])
async def get_items_by_type(item_type: str):
    items = item_service.get_items_by_type(item_type)
    if not len(items):
        raise HTTPException(status_code=404, detail="Items not found")
    
    return items

@router.get("/bulk-create/", response_model=List[ItemSchema])
async def bulk_create_items():
    items_path = f"{Path(__file__).resolve().parent.parent}/assets/items.json"
    with open(items_path, "r") as file:
        data = json.load(file)

    if not data:
        raise HTTPException(status_code=404, detail="Items not found")

    items: List[ItemModel] = [ItemModel(**item) for item in data]
    item_service.bulk_create_items(items)
    return items