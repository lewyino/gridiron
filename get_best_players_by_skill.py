from db.PlayerSimpleDbConnect import PlayerSimpleDbConnect
from model.Player import Player


def get_best_players_by_skill(skill: str, min_value: int = 15, verbose: bool = True):
    db = PlayerSimpleDbConnect()
    selected_players = db.get_best_players_by_skill(skill, min_value)
    i = 1
    result = []
    for p in selected_players:
        player = Player.convert_from_tuple(p)
        result.append(player)
        if verbose:
            print('%.2d. %s, %s, %s: %s' % (i, player.name, player.bpos, skill, player.__getattribute__(skill)))
        i += 1
    return result
