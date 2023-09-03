from typing import Dict


class PlayerParse:
    def __init__(self, _id: str | int, name: str):
        self.id = int(_id) if type(_id) == str else _id
        self.name = " ".join(name.split())
        self.weeks_at_club = 0
        self.skills = {}
        self.current_training = ('', 0, 0)

    def __str__(self):
        return f'id: {self.id}\n' \
               f'name: {self.name}\n' \
               f'age: {getattr(self, "age")}\n' \
               f'rating: {getattr(self, "rating")}*\n' \
               f'energy: {getattr(self, "energy")}%\n' \
               f'wage: {getattr(self, "wage")}$\n'

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def from_dict(data: Dict):
        p = PlayerParse(0, '')
        for k, v in data.items():
            setattr(p, k, v)
        return p

