from model.PlayerParse import PlayerParse
from site_parser.players_data import get_players_list, get_player_data
from test.fixures import parse_player_data
import os


def test_get_players_list_count():
    __result = 9
    f = open(f'{os.path.dirname(__file__)}/players.html', 'r')
    players_site_data = f.read()
    f.close()
    result = get_players_list(players_site_data)
    assert len(result) == __result


def test_get_players_list_data():
    __result = PlayerParse(123456, 'Jan Kowalski')
    f = open(f'{os.path.dirname(__file__)}/players.html', 'r')
    players_site_data = f.read()
    f.close()
    result = get_players_list(players_site_data)
    assert result[0].__dict__ == __result.__dict__


def test_get_player_data(parse_player_data):
    f = open(f'{os.path.dirname(__file__)}/player.html', 'r')
    player_site_data = f.read()
    f.close()
    result = get_player_data(player_site_data)
    assert result.__dict__ == parse_player_data
