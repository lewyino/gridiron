from model.TeamPlayer import TeamPlayer
from site_parser.players_data import get_players_list
import os


def test_get_players_list_count():
    __result = 9
    f = open(f'{os.path.dirname(__file__)}/players.html', 'r')
    players_site_data = f.read()
    f.close()
    result = get_players_list(players_site_data)
    assert len(result) == __result


def test_get_players_list_data():
    __result = TeamPlayer(123456, 'Jan Kowalski')
    f = open(f'{os.path.dirname(__file__)}/players.html', 'r')
    players_site_data = f.read()
    f.close()
    result = get_players_list(players_site_data)
    assert result[0].__dict__ == __result.__dict__
