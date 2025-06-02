from app.utils.helpers import to_camel_case
from app.schemas.entry_schema import EntrySchema


class LocationTypeSchema(EntrySchema):
    id: int

    class Config:
        from_attributes = True
        alias_generator = to_camel_case
        validate_by_name = True

class LocationTypeCreateSchema(EntrySchema):

    class Config:
        from_attributes = True
        alias_generator = to_camel_case
        validate_by_name = True