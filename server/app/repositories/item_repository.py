from sqlalchemy.orm import Session
from app.models.item import Item

def get_item(db: Session, item_id: int) -> Item:
    return db.query(Item).filter(Item.id == item_id).first()

def update_item(db: Session, item_id: int, item_data: dict) -> Item:
    item = db.query(Item).filter(Item.id == item_id).first()
    if item:
        for key, value in item_data.items():
            setattr(item, key, value)
        db.commit()
        db.refresh(item)
    return item

def delete_item(db: Session, item_id: int) -> Item:
    item = db.query(Item).filter(Item.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
    return item

def create_item(db: Session, item_data: dict) -> Item:
    item = Item(**item_data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def get_all_items(db: Session) -> list[Item]:
    return db.query(Item).all()

def get_items_by_type(db: Session, item_type: str) -> list[Item]:
    return db.query(Item).filter(Item.item_type == item_type).all()

def get_item_by_name(db: Session, name: str) -> Item:
    return db.query(Item).filter(Item.name == name).first()