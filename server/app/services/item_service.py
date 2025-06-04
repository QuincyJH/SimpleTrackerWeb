from typing import List
from app.repositories import item_repository
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.item import Item
from app.schemas.item_schema import ItemCreateSchema
from app.repositories import item_type_repository



def get_item(item_id: int) -> Item:
    db: Session = next(get_db())
    return item_repository.get_item(db, item_id)

def update_item(item_id: int, item_data: dict) -> Item:
    db: Session = next(get_db())
    item = item_repository.update_item(db, item_id, item_data)
    return item

def delete_item(item_id: int) -> Item:
    db: Session = next(get_db())
    item = item_repository.delete_item(db, item_id)
    return item

def create_item(item_data: ItemCreateSchema) -> Item:
    db: Session = next(get_db())
    item_type = item_type_repository.get_item_type_by_name(db, item_data.item_type)
    item = item_repository.create_item(db, item_data, item_type.id if item_type else None)
    return item

def get_all_items() -> list[Item]:
    db: Session = next(get_db())
    return item_repository.get_all_items(db)

def get_item_by_name(name: str) -> Item:
    db: Session = next(get_db())
    return item_repository.get_item_by_name(db, name)

def get_items_by_type(item_type: str) -> list[Item]:
    db: Session = next(get_db())
    return item_repository.get_items_by_type(db, item_type)

def bulk_create_items(bulk_items: List[ItemCreateSchema]) -> List[Item]:
    db: Session = next(get_db())
    items: List[Item] = []
    for item in bulk_items:
        item_type = item_type_repository.get_item_type_by_name(db, item.item_type)
        items.append(item_repository.create_item(db, item, item_type.id if item_type else None))
    db.commit()
    return items