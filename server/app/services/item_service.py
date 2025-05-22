from typing import List
from app.repositories import item_repository
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.item import Item
from app.models.item_model import ItemModel



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

def create_item(item_data: dict) -> Item:
    db: Session = next(get_db())
    item = item_repository.create_item(db, item_data)
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

def bulk_create_items(items: List[ItemModel]):
    db: Session = next(get_db())
    for item in items:
        item_repository.create_item(db, item.__dict__)
    db.commit()
    return items