from typing import List, Optional
from app.schemas.entry_schema import EntrySchema
from app.utils.helpers import to_camel_case
from app.schemas.location_schema import LocationSchema


class RegionSchema(EntrySchema):
    id: int
    locations: Optional[List[LocationSchema]]

    class Config:
        from_attributes = True
        alias_generator = to_camel_case
        validate_by_name = True

class RegionCreateSchema(EntrySchema):

    class Config:
        from_attributes = True
        alias_generator = to_camel_case
        validate_by_name = True