from typing import Optional
from pydantic import BaseModel


class RunCreateSchema(BaseModel):
    name: str
    data: Optional[str] = None