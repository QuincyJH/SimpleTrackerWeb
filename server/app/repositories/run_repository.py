import json
from typing import List
from sqlalchemy import desc
from sqlalchemy.orm import Session
from app.models.run import Run

def get_run(db: Session, run_id: int) -> Run:
    run = db.query(Run).filter(Run.id == run_id).first()
    return ensure_data_is_string(run)

def update_run(db: Session, run_id: int, run_data: dict) -> Run:
    run = db.query(Run).filter(Run.id == run_id).first()
    if "data" in run_data and not isinstance(run_data["data"], str):
        run_data["data"] = json.dumps(run_data["data"])
    for key, value in run_data.items():
        setattr(run, key, value)
    db.commit()
    db.refresh(run)
    
    return ensure_data_is_string(run)

def delete_run(db: Session, run_id: int) -> Run:
    run = db.query(Run).filter(Run.id == run_id).first()
    if run:
        db.delete(run)
        db.commit()
    return ensure_data_is_string(run)

def create_run(db: Session, run_data: dict) -> Run:
    if "data" in run_data and not isinstance(run_data["data"], str):
        run_data["data"] = json.dumps(run_data["data"])
    run = Run(**run_data)
    db.add(run)
    db.commit()
    db.refresh(run)
    return ensure_data_is_string(run)

def get_all_runs(db: Session) -> List[Run]:
    return [ensure_data_is_string(run) for run in db.query(Run).order_by(desc(Run.accessed_at)).all()]

def ensure_data_is_string(run):
    if run and hasattr(run, "data") and run.data is not None and not isinstance(run.data, str):
        run.data = json.dumps(run.data)
    return run