from model.PlayerDb import PlayerDb
from model.PlayerParse import PlayerParse
from player.player_skills import update_player_skills
from test.fixures import parse_player_data, player_data_1, player_data_2


def test_update_player_data_skill1(parse_player_data, player_data_1):
    p1 = PlayerDb(player_data_1)
    p1.weeks_at_club -= 1
    p2 = PlayerParse.from_dict(parse_player_data)
    result = update_player_skills(p1, p2)
    assert len(result[1]) == 1
    assert result[1][0][0] == 'strength'
    assert result[1][0][1] == 1
    assert result[0].weeks_at_club == p1.weeks_at_club + 1


def test_update_player_data_skill2(parse_player_data, player_data_1):
    p1 = PlayerDb(player_data_1)
    p1.weeks_at_club -= 1
    p1.training_data['strength'] = 4
    p1.training_data['positioning'] = 4
    p2 = PlayerParse.from_dict(parse_player_data)
    result = update_player_skills(p1, p2)
    assert len(result[1]) == 1
    assert result[1][0][0] == 'strength'
    assert result[1][0][1] == 1
    assert result[0].training_data['strength'] == 0
    assert result[0].training_data['positioning'] == 4
    assert result[0].weeks_at_club == p1.weeks_at_club + 1


def test_update_player_data_training1(parse_player_data, player_data_2):
    p1 = PlayerDb(player_data_2)
    p1.weeks_at_club -= 1
    p2 = PlayerParse.from_dict(parse_player_data)
    result = update_player_skills(p1, p2)
    assert len(result[1]) == 0
    assert result[0].training_data['strength'] == 2
    assert result[0].weeks_at_club == p1.weeks_at_club + 1


def test_update_player_data_training2(parse_player_data, player_data_2):
    p1 = PlayerDb(player_data_2)
    p1.weeks_at_club -= 1
    del p1.training_data['strength']
    p2 = PlayerParse.from_dict(parse_player_data)
    result = update_player_skills(p1, p2)
    assert len(result[1]) == 0
    assert result[0].training_data['strength'] == 1
    assert result[0].weeks_at_club == p1.weeks_at_club + 1


def test_update_player_data_same_weeks_at_club(parse_player_data, player_data_1):
    p1 = PlayerDb(player_data_1)
    p2 = PlayerParse.from_dict(parse_player_data)
    result = update_player_skills(p1, p2)
    assert len(result[1]) == 0
    assert p1.__dict__ == result[0].__dict__
