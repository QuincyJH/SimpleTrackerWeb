from app.models.entry_model import EntryModel

class ItemModel(EntryModel):
    def __init__(self, name, display_name, item_type = None):
        super().__init__(name, display_name)
        self.item_type = item_type