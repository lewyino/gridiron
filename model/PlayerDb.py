from tinydb.table import Document

from model.PlayerParse import PlayerParse


class PlayerDb:
    def __init__(self, data: Document | PlayerParse):
        self.id = None
        if isinstance(data, PlayerParse):
            data = data.__dict__
        for k, v in data.items():
            setattr(self, k, v)
        if not hasattr(self, 'training_data'):
            self.training_data = {}

