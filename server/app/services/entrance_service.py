from typing import List
from sqlalchemy.orm import Session
from app.repositories import entrance_repository
from app.database import get_db
from app.models.entrance import Entrance
from app.models.entrance_model import EntranceModel


def get_entrance(entrance_id: int) -> Entrance:
    db: Session = next(get_db())
    return entrance_repository.get_entrance(db, entrance_id)

def update_entrance(entrance_id: int, entrance_data: dict) -> Entrance:
    db: Session = next(get_db())
    entrance = entrance_repository.update_entrance(db, entrance_id, entrance_data)
    return entrance

def delete_entrance(entrance_id: int) -> Entrance:
    db: Session = next(get_db())
    entrance = entrance_repository.delete_entrance(db, entrance_id)
    return entrance

def create_entrance(entrance_data: dict) -> Entrance:
    db: Session = next(get_db())
    entrance = entrance_repository.create_entrance(db, entrance_data)
    return entrance

def get_all_entrances() -> list[Entrance]:
    db: Session = next(get_db())
    return entrance_repository.get_all_entrances(db)

def get_entrance_by_name(name: str) -> Entrance:
    db: Session = next(get_db())
    return entrance_repository.get_entrance_by_name(db, name)

def get_entrances_by_type(entrance_type: str) -> List[Entrance]:
    db: Session = next(get_db())
    return entrance_repository.get_entrances_by_type(db, entrance_type)

def bulk_create_entrances(entrances: List[EntranceModel]):
    db: Session = next(get_db())
    for entrance in entrances:
        entrance_repository.create_entrance(db, entrance.__dict__)
    db.commit()
    return entrances