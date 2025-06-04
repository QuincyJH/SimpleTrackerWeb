from app.utils.helpers import to_camel_case
from app.schemas.entry_schema import EntrySchema
from app.schemas.location_type_schema import LocationTypeSchema


class LocationSchema(EntrySchema):
    id: int
    region_id: int
    location_type: LocationTypeSchema

    class Config:
        from_attributes = True
        alias_generator = to_camel_case
        validate_by_name = True

class LocationCreateSchema(EntrySchema):
    location_type: str
    region_name: str

    class Config:
        from_attributes = True
        alias_generator = to_camel_case
        validate_by_name = True