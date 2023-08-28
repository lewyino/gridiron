from site_parser.players_data import get_players_list
import os


def test_get_players_list_count():
    __result = 9
    f = open(f'{os.path.dirname(__file__)}/players.html', 'r')
    players_site_data = f.read()
    f.close()
    assert len(get_players_list(players_site_data)) == __result
