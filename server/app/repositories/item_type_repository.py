from sqlalchemy.orm import Session
from app.models.item_type import ItemType
from app.schemas.item_type_schema import ItemTypeCreateSchema



def get_item_type(db: Session, item_type_id: int) -> ItemType:
    return db.query(ItemType).filter(ItemType.id == item_type_id).first()

def update_item_type(db: Session, item_type_id: int, item_type_data: dict) -> ItemType:
    item_type = db.query(ItemType).filter(ItemType.id == item_type_id).first()
    
    if item_type:
        for key, value in item_type_data.items():
            setattr(item_type, key, value)
        db.commit()
        db.refresh(item_type)
    return item_type

def delete_item_type(db: Session, item_type_id: int) -> ItemType:
    item_type = db.query(ItemType).filter(ItemType.id == item_type_id).first()

    if item_type:
        db.delete(item_type)
        db.commit()
    return item_type

def create_item_type(db: Session, item_type_data: ItemTypeCreateSchema) -> ItemType:
    item_type = ItemType(**item_type_data.model_dump(exclude_unset=True))
    db.add(item_type)
    db.commit()
    db.refresh(item_type)
    return item_type

def get_all_item_types(db: Session) -> list[ItemType]:
    return db.query(ItemType).all()

def get_item_type_by_name(db: Session, name: str) -> ItemType:
    return db.query(ItemType).filter(ItemType.name == name).first()