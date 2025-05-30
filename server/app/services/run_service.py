from typing import List
from app.repositories import run_repository
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.run import Run
from app.schemas.run_schema import RunCreateSchema

def get_run(run_id: int) -> Run:
    db: Session = next(get_db())
    return run_repository.get_run(db, run_id)

def update_run(run_id: int, run_data: dict) -> Run:
    db: Session = next(get_db())
    run = run_repository.update_run(db, run_id, run_data)
    return run

def delete_run(run_id: int) -> Run:
    db: Session = next(get_db())
    run = run_repository.delete_run(db, run_id)
    return run

def create_run(run_data: RunCreateSchema) -> Run:
    db: Session = next(get_db())
    run = run_repository.create_run(db, run_data)
    return run

def get_all_runs() -> List[Run]:
    db: Session = next(get_db())
    return run_repository.get_all_runs(db)