import pytest


@pytest.fixture(scope='session')
def parse_player_data():
    return {
        'id': 123456,
        'name': 'Jan Kowalski',
        'age': 16,
        'rating': 2.0,
        'experience': 0.5,
        'energy': 100,
        'talent': 4.0,
        'team_chemistry': 1.0,
        'wage': 1668,
        'skills': {
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
        },
        'weeks_at_club': 2,
        'bmi': 29.0,
        'height': 185.0,
        'weight': 100.0,
        'current_training': ('strength', 5, 3)
    }


@pytest.fixture(scope='session')
def player_data_1(parse_player_data):
    data = parse_player_data.copy()
    data['skills'] = parse_player_data['skills'].copy()
    data['skills']['strength'] = data['skills']['strength'] - 1
    return data


@pytest.fixture(scope='session')
def player_data_2(parse_player_data):
    data = parse_player_data.copy()
    data['skills'] = parse_player_data['skills'].copy()
    data['training_data'] = {'strength': 1}
    return data
