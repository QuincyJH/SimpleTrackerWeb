from sqlalchemy.orm import Session
from app.models.item import Item
from app.schemas.item_schema import ItemCreateSchema

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

def create_item(db: Session, item_data: ItemCreateSchema, item_type_id: int) -> Item:
    data = item_data.model_dump(exclude_unset=True)
    data.pop('item_type', None)
    item = Item(**data, item_type_id=item_type_id)

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