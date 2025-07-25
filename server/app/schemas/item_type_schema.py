from app.utils.helpers import to_camel_case
from app.schemas.entry_schema import EntrySchema


class ItemTypeSchema(EntrySchema):
    id: int

    class Config:
        from_attributes = True
        alias_generator = to_camel_case
        validate_by_name = True

class ItemTypeCreateSchema(EntrySchema):

    class Config:
        from_attributes = True
        alias_generator = to_camel_case
        validate_by_name = True