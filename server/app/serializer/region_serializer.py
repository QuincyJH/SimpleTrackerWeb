from app.models.region import Region


def serialize_region_with_locations(region: Region):
    return {
        "id": region.id,
        "name": region.name,
        "display_name": region.display_name,
        "locations": [
            {
                "id": loc.id,
                "name": loc.name,
                "display_name": loc.display_name,
                "region_id": loc.region_id,
                "location_type": loc.location_type
            }
            for loc in region.locations
        ]
    }