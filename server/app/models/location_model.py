from app.models.entry_model import EntryModel

class LocationModel(EntryModel):
    def __init__(self, name, display_name, region_name=None):
        super().__init__(name, display_name)
        self.region_name = region_name