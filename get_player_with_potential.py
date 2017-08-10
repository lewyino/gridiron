from db.PlayerSimpleDbConnect import PlayerSimpleDbConnect
from model.Player import Player


def get_player_with_potential(
        min_talent: float = 3.5,
        min_teamwork: int = 10,
        min_consistency: int = 10,
        max_age: int = None,
        verbose: bool = True
):
    db = PlayerSimpleDbConnect()
    players = db.get_players_with_potential(min_talent, min_teamwork, min_consistency, max_age)
    if verbose:
        print('players with potential: %d' % len(players))
    result = []
    for p in players:
        player = Player.convert_from_tuple(p)
        result.append(player)
        if verbose:
            print('%s (%s)\n\ttalent: %.1f\n\tteamwork: %d\n\tconsistency: %d'
                  % (player.name, player.bpos, player.talent, player.teamwork, player.consistency))
    return result