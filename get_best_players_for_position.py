from db.PlayerSimpleDbConnect import PlayerSimpleDbConnect
from model.Player import Player


def get_best_players_for_position(position: str, players_number: int = 5, verbose: bool = True):
    db = PlayerSimpleDbConnect()
    selected_players = db.get_best_players_by_position(position, players_number)
    result = []
    for p in selected_players:
        player = Player.convert_from_tuple(p)
        result.append(player)
        if verbose:
            print('%s %s' % (player.name, player.bpos))
    return result
