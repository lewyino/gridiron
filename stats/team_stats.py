from typing import Tuple

from db.PlayerSimpleDbConnect import PlayerSimpleDbConnect
from model.Player import Player


def get_players_salary(players: Tuple[Player], max_age: int = None, verbose: bool = False):
    players_salary = 0
    for p in players:
        if max_age is None or p.age <= max_age:
            players_salary += p.wage
    if verbose:
        str = 'players (%d) salary: %d'
        if max_age is not None:
            str += ', with max age: %d'
        print(str % (len(players), players_salary, max_age))
    return players_salary


def get_players_salary_avg(players: Tuple[Player], max_age: int = None, verbose: bool = False):
    players_salary = 0
    players_count = 0
    for p in players:
        if max_age is None or p.age <= max_age:
            players_salary += p.wage
            players_count += 1
    players_salary_avg = float(players_salary) / players_count if players_count > 0 else 0
    if verbose:
        str = 'players (%d) salary avg: %.2f'
        if max_age is not None:
            str += ', with max age: %d'
        print(str % (len(players), players_salary_avg, max_age))
    return players_salary_avg


def get_players_age_stats(players: Tuple[Player], max_age: int = None, verbose: bool = False):
    players_age = 0
    players_count = 0
    players_max = 0
    players_min = 99
    for p in players:
        if max_age is None or p.age <= max_age:
            players_age += p.age
            players_count += 1
            players_max = p.age if p.age > players_max else players_max
            players_min = p.age if p.age < players_min else players_min
    players_avg = float(players_age) / players_count
    if verbose:
        str_avg = 'players (%d) age avg: %.2f'
        if max_age is not None:
            str_avg += ', with max age: %d'
        print(str_avg % (len(players), players_avg, max_age))
        str_max = 'players (%d) age max: %d'
        if max_age is not None:
            str_max += ', with max age: %d'
        print(str_max % (len(players), players_max, max_age))
        str_min = 'players (%d) age min: %d'
        if max_age is not None:
            str_min += ', with max age: %d'
        print(str_min % (len(players), players_min, max_age))
    return players_avg, players_min, players_max


def get_team_stats(max_age: int = None, verbose: bool = False):
    max_age = 99 if max_age is None else max_age
    db = PlayerSimpleDbConnect(None, False)
    players = tuple(map(lambda p: Player.convert_from_tuple(p), db.get_current_all_players()))
    players = tuple(filter(lambda p: p.age <= max_age, players))
    players_salary = get_players_salary(players, max_age, verbose)
    players_salary_avg = get_players_salary_avg(players, max_age, verbose)
    players_age_stats = get_players_age_stats(players, max_age, verbose)
    players_count = len(players)
    if verbose:
        print('==========')
        print('players count: %d, max age: %d' % (players_count, max_age))
        print('players salary: %d, max age: %d' % (players_salary, max_age))
        print('players salary avg: %.2f, max age: %d' % (players_salary_avg, max_age))
        print('players age avg: %.2f, max age: %d' % (players_age_stats[0], max_age))
        print('players age min: %d, max age: %d' % (players_age_stats[1], max_age))
        print('players age max: %d, max age: %d' % (players_age_stats[2], max_age))
    return players_count, players_salary, players_salary_avg
