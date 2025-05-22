from app.models.entry_model import EntryModel

class EntranceModel(EntryModel):
    def __init__(self, name, display_name, entrance_type):
        super().__init__(name, display_name)
        self.entrance_type = entrance_type

