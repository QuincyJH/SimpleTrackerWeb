from typing import List
from fastapi import APIRouter, HTTPException
from app.services import run_service
from app.schemas.run_schema import RunCreateSchema, RunSchema

router = APIRouter()

@router.get("/{run_id}", response_model=RunSchema)
async def get_run(run_id: int):
    run = run_service.get_run(run_id)
    if run is None:
        raise HTTPException(status_code=404, detail="Run not found")
    
    return run

@router.put("/{run_id}", response_model=RunSchema)
async def update_run(run_id: int, run_data: dict):
    run = run_service.update_run(run_id, run_data)
    if run is None:
        raise HTTPException(status_code=404, detail="Run not found")
    
    return run

@router.delete("/{run_id}", response_model=RunSchema)
async def delete_run(run_id: int):
    run = run_service.delete_run(run_id)
    if run is None:
        raise HTTPException(status_code=404, detail="Run not found")
    
    return run

@router.post("/", response_model=RunSchema)
async def create_run(run_data: RunCreateSchema):
    run = run_service.create_run(run_data)
    if run is None:
        raise HTTPException(status_code=400, detail="Failed to create run")
    
    return run

@router.get("/", response_model=List[RunSchema])
async def get_all_runs():
    runs = run_service.get_all_runs()
    if not len(runs):
        raise HTTPException(status_code=404, detail="Runs not found")
    return runs