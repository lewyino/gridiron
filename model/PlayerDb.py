from typing import Dict

from tinydb.table import Document

from model.PlayerParse import PlayerParse


class PlayerDb:
    def __init__(self, data: Document | PlayerParse | Dict):
        self.id = None
        self.name = None
        self.skills = {}
        self.weeks_at_club = 0
        if isinstance(data, PlayerParse):
            data = data.__dict__
        for k, v in data.items():
            if k == 'skills':
                for skill_name, skill_value in v.items():
                    self.skills[skill_name] = skill_value
            else:
                setattr(self, k, v)
        if not hasattr(self, 'training_data'):
            self.training_data = {}
