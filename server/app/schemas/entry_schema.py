from pydantic import BaseModel
from app.utils.helpers import to_camel_case


class EntrySchema(BaseModel):
    name: str
    display_name: str

    class Config:
        from_attributes = True
        alias_generator = to_camel_case
        validate_by_name = True