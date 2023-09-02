from model.PlayerDb import PlayerDb
from tinydb import TinyDB, Query, where


class PlayerTinyDb:

    def __init__(self, db_file='./db.json'):
        self.__db = TinyDB(db_file)
        self.__players_table = self.__db.table('players')
        self.__player_query = Query()

    def get_player(self, _id: int) -> PlayerDb:
        player_doc = self.__players_table.get(self.__player_query.id == _id)
        return None if player_doc is None else PlayerDb(player_doc)

    def save_player(self, player: PlayerDb):
        if self.__players_table.contains(where('id') == player.id):
            return self.__players_table.upsert(player.__dict__, where('id') == player.id)
        return self.__players_table.insert(player.__dict__)

    def len(self):
        return len(self.__players_table)
