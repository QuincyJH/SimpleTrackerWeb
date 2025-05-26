from typing import List
from sqlalchemy import desc
from sqlalchemy.orm import Session
from app.models.run import Run
from app.schemas.run_create_schema import RunCreateSchema

def get_run(db: Session, run_id: int) -> Run:
    return db.query(Run).filter(Run.id == run_id).first()

def update_run(db: Session, run_id: int, run_data: dict) -> Run:
    run = db.query(Run).filter(Run.id == run_id).first()
    if run:
        for key, value in run_data.items():
            setattr(run, key, value)
        db.commit()
        db.refresh(run)
    return run

def delete_run(db: Session, run_id: int) -> Run:
    run = db.query(Run).filter(Run.id == run_id).first()
    if run:
        db.delete(run)
        db.commit()
    return run

def create_run(db: Session, run_data: RunCreateSchema) -> Run:
    # run_data = run_data.model_dump(exclude_unset=True)
    run = Run(**run_data.model_dump(exclude_unset=True))
    db.add(run)
    db.commit()
    db.refresh(run)
    return run

def get_all_runs(db: Session) -> List[Run]:
    return db.query(Run).order_by(desc(Run.accessed_at)).all()