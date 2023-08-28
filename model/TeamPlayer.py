
class TeamPlayer:

    def __init__(self, _id: str | int, name: str):
        self.id = int(_id) if type(_id) == str else _id
        self.name = " ".join(name.split())

    def __setattr__(self, *args, **kwargs):
        return super().__setattr__(*args, **kwargs)

    def __getattribute__(self, *args, **kwargs):
        try:
            if args[0] in ('rating', 'experience', 'talent', 'teamChemistry'):
                return super().__getattribute__(*args, **kwargs) / 2
            return super().__getattribute__(*args, **kwargs)
        except:
            if args[0] in ('name', 'bpos', 'wage', 'health'):
                return ''
            else:
                return 0

    def __str__(self):
        return f'id: {self.id}\n' \
               f'name: {self.name}\n' \
               f'bpos: {self.bpos}\n' \
               f'age: {self.age}\n' \
               f'rating: {self.rating}*\n' \
               f'energy: {self.energy}%\n' \
               f'wage: {self.wage}$\n' \
               f'health: {self.health}\n'

    def __repr__(self):
        return self.__str__()
