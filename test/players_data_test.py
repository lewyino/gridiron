from model.TeamPlayer import TeamPlayer
from site_parser.players_data import get_players_list, get_player_data
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


def test_get_player_data():
    __result = {
        'id': 123456,
        'name': 'Jan Kowalski',
        'age': 16,
        'rating': 2.0,
        'experience': 0.5,
        'energy': 100,
        'talent': 4.0,
        'team_chemistry': 1.0,
        'wage': 1668,
        'positioning': 5,
        'passing': 1,
        'tackling': 1,
        'speed': 14,
        'vision': 6,
        'catching': 4,
        'blocking': 2,
        'strength': 15,
        'intelligence': 18,
        'carrying': 1,
        'kicking': 5,
        'agility': 3,
        'aggression': 7,
        'footwork': 7,
        'punting': 2,
        'stamina': 2,
        'teamwork': 15,
        'consistency': 10,
        'weeks_at_club': 2,
        'bmi': 29.0,
        'height': 185.0,
        'weight': 100.0
    }
    f = open(f'{os.path.dirname(__file__)}/player.html', 'r')
    player_site_data = f.read()
    f.close()
    result = get_player_data(player_site_data)
    assert result.__dict__ == __result
