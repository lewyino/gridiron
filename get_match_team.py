from typing import List

from db.PlayerSimpleDbConnect import PlayerSimpleDbConnect
from model.Formation import Formation
from model.Player import Player


def get_match_team(formation: List[Formation], verbose: bool = True):
    db = PlayerSimpleDbConnect()
    used_players = []
    selected_players = []

    player_count = 0
    for f in formation:
        player_count += f.quantity
        players = db.get_best_players(f.position, f.quantity + len(selected_players))
        for p in players:
            player = Player.convert_from_tuple(p)
            try:
                used_players.index(player.id)
            except:
                player.my_pos = f.position.upper()
                used_players.append(player.id)
                selected_players.append(player)
                if len(used_players) == player_count:
                    break

    if verbose:
        for p in selected_players:
            print('%s - %s, %s' % (p.my_pos, p.name, p.bpos))

    return selected_players


def get_basic_formation__4_3_a_formation(verbose: bool = True):
    formation = [
        Formation('qb', 1),
        Formation('wr', 2),
        Formation('te', 2),
        Formation('de', 2),
        Formation('olb', 2),
        Formation('cb', 2),
        Formation('ol', 5),
        Formation('mlb', 1),
        Formation('sf', 2),
        Formation('dl', 2),
        Formation('rb', 1),
    ]
    selected_players = get_match_team(formation)

    if verbose:
        for p in selected_players:
            print('%s - %s, %s' % (p.my_pos, p.name, p.bpos))

    return selected_players

