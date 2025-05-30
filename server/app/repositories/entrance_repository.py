from sqlalchemy.orm import Session
from app.models.entrance import Entrance
from app.schemas.entrance_schema import EntranceCreateSchema

def get_entrance(db: Session, entrance_id: int) -> Entrance:
    return db.query(Entrance).filter(Entrance.id == entrance_id).first()

def update_entrance(db: Session, entrance_id: int, entrance_data: dict) -> Entrance:
    entrance = db.query(Entrance).filter(Entrance.id == entrance_id).first()
    if entrance:
        for key, value in entrance_data.items():
            setattr(entrance, key, value)
        db.commit()
        db.refresh(entrance)
    return entrance

def delete_entrance(db: Session, entrance_id: int) -> Entrance:
    entrance = db.query(Entrance).filter(Entrance.id == entrance_id).first()
    if entrance:
        db.delete(entrance)
        db.commit()
    return entrance

def create_entrance(db: Session, entrance_data: EntranceCreateSchema) -> Entrance:
    entrance = Entrance(**entrance_data.model_dump(exclude_unset=True))
    db.add(entrance)
    db.commit()
    db.refresh(entrance)
    return entrance

def get_all_entrances(db: Session) -> list[Entrance]:
    return db.query(Entrance).all()

def get_entrances_by_type(db: Session, entrance_type: str) -> list[Entrance]:
    return db.query(Entrance).filter(Entrance.entrance_type == entrance_type).all()

def get_entrance_by_name(db: Session, name: str) -> Entrance:
    return db.query(Entrance).filter(Entrance.name == name).first()