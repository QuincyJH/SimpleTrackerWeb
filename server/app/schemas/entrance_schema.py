from app.schemas.entry_schema import EntrySchema
from app.utils.helpers import to_camel_case


class EntranceSchema(EntrySchema):
    id: int
    entrance_type: str

    class Config:
        from_attributes = True
        alias_generator = to_camel_case
        validate_by_name = True