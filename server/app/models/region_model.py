from app.models.entry_model import EntryModel

class RegionModel(EntryModel):
    def __init__(self, name, display_name):
        super().__init__(name, display_name)
        