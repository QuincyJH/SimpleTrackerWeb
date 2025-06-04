from sqlalchemy.orm import Session
from app.database import get_db
from app.repositories import item_type_repository
from app.models.item_type import ItemType


def get_item_type(item_id: int) -> ItemType:
    db: Session = next(get_db())
    return item_type_repository.get_item_type(db, item_id)

def update_item_type(item_id: int, item_type_data: dict) -> ItemType:
    db: Session = next(get_db())
    item_type = item_type_repository.update_item_type(db, item_id, item_type_data)
    return item_type

def delete_item_type(item_id: int) -> ItemType:
    db: Session = next(get_db())
    item_type = item_type_repository.delete_item_type(db, item_id)
    return item_type

def create_item_type(item_type_data: dict) -> ItemType:
    db: Session = next(get_db())
    item_type = item_type_repository.create_item_type(db, item_type_data)
    return item_type

def get_all_item_types() -> list[ItemType]:
    db: Session = next(get_db())
    return item_type_repository.get_all_item_types(db)

def get_item_type_by_name(name: str) -> ItemType:
    db: Session = next(get_db())
    return item_type_repository.get_item_type_by_name(db, name)