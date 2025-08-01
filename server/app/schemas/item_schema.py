from typing import Optional
from app.utils.helpers import to_camel_case
from app.schemas.entry_schema import EntrySchema
from app.schemas.item_type_schema import ItemTypeSchema


class ItemSchema(EntrySchema):
    id: int
    item_type: Optional[ItemTypeSchema] = None

    class Config:
        from_attributes = True
        alias_generator = to_camel_case
        validate_by_name = True

class ItemCreateSchema(EntrySchema):
    item_type: Optional[str]

    class Config:
        from_attributes = True
        alias_generator = to_camel_case
        validate_by_name = True