from typing import List
from sqlalchemy.orm import Session
from app.repositories import entrance_repository
from app.database import get_db
from app.models.entrance import Entrance
from app.schemas.entrance_schema import EntranceCreateSchema


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

def create_entrance(entrance_data: EntranceCreateSchema) -> Entrance:
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

def bulk_create_entrances(bulk_entrances: List[EntranceCreateSchema]):
    entrances: List[Entrance] = []
    db: Session = next(get_db())
    for entrance in bulk_entrances:
        entrances.append(entrance_repository.create_entrance(db, entrance))
    db.commit()
    return entrances