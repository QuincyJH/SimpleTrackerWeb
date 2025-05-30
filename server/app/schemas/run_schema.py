from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from app.utils.helpers import to_camel_case


class RunSchema(BaseModel):
    id: Optional[int]
    name:str
    data: Optional[str]
    accessed_at: Optional[datetime]
    modified_at: Optional[datetime]
    created_at: Optional[datetime]

    class Config:
        from_attributes = True
        alias_generator = to_camel_case
        validate_by_name = True

class RunCreateSchema(BaseModel):
    name: str
    data: Optional[str] = None