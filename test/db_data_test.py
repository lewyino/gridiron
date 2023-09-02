import os

from db.PlayerTinyDb import PlayerTinyDb
from model.PlayerDb import PlayerDb
from site_parser.players_data import get_player_data


test_db_file = './test_db.json'


def setup():
    global test_db, p
    test_db = PlayerTinyDb(test_db_file)
    f = open(f'{os.path.dirname(__file__)}/player.html', 'r')
    player_site_data = f.read()
    f.close()
    p = get_player_data(player_site_data)


def teardown():
    os.remove(test_db_file)


def test_add_to_db():
    before_add = test_db.len()
    doc_id = test_db.save_player(PlayerDb(p))
    assert doc_id
    after_add = test_db.len()
    assert after_add > before_add


def test_get_from_db():
    doc_id = test_db.save_player(PlayerDb(p))
    assert doc_id
    player_db = test_db.get_player(p.id)
    assert p.id == player_db.id
    assert player_db.training_data is not None
