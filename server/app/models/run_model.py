class RunModel():
    def __init__(self, name, data, accessed_at=None, modified_at=None, created_at=None):
        self.name = name
        self.data = data
        self.accessed_at = accessed_at
        self.modified_at = modified_at
        self.created_at = created_at