from typing import Tuple, Sequence
import re

from db.PlayerSimpleDbConnect import PlayerSimpleDbConnect
from model.Player import Player

from site_parser.GridIronLoginUrllib import GridIronLoginUrllib as GridIronLogin
from site_parser.TeamMatchArchiveParser import TeamMatchArchiveParser
from stats.match_stats import get_teams_events


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


def get_match_archive_page(team_id: int, login: str, password: str, verbose: bool = False):
    if verbose:
        print('get matches archive page for team_id: %d' % team_id)
    site = GridIronLogin(login, password)
    site.get_session()
    return site.get_match_archive_site(team_id)


def get_team_matches(team_id: str, login: str, password: str) -> Tuple[Tuple[str, str, str]]:
    page = get_match_archive_page(int(team_id), login, password, True)
    parser = TeamMatchArchiveParser(page)
    matches = parser.get_team_matches()
    return tuple(matches)


def get_team_match_ids_stats_last(matches: Sequence[Tuple[str, str, str]], last: str, verbose=False) -> Tuple[int]:
    count = int(re.search(r'last(\d+)', last).group(1))
    if verbose:
        print('try to get last {count} matches stats'.format(count=count))
    return tuple(map(lambda match: int(match[0]), matches[:count]))


def get_team_match_ids_stats_league(matches: Sequence[Tuple[str, str, str]], last: str, verbose=False) -> Tuple[int]:
    count = int(re.search(r'league(\d+)', last).group(1))
    if verbose:
        print('try to get last {count} league matches stats'.format(count=count))
    filtered = list(filter(lambda match: match[1] == 'League', matches))[:count]
    return tuple(map(lambda match: int(match[0]), filtered))


def get_team_match_ids_stats_cup(matches: Tuple[Tuple[str, str, str]], last: str, verbose=False) -> Tuple[int]:
    count = int(re.search(r'cup(\d+)', last).group(1))
    if verbose:
        print('try to get last {count} cup matches stats'.format(count=count))
    filtered = list(filter(lambda match: match[1] == 'Cup', matches))[:count]
    return tuple(map(lambda match: int(match[0]), filtered))


def get_team_match_ids_stats_friendly(matches: Tuple[Tuple[str, str, str]], last: str, verbose=False) -> Tuple[int]:
    count = int(re.search(r'friendly(\d+)', last).group(1))
    if verbose:
        print('try to get last {count} friendly matches stats'.format(count=count))
    filtered = list(filter(lambda match: match[1] == 'Friendly', matches))[:count]
    return tuple(map(lambda match: int(match[0]), filtered))


def get_team_match_ids_stats_indexes(matches: Sequence[Tuple[str, str, str]], indexes: str, verbose=False) -> Tuple[int]:
    indexes_list = indexes.split(',')
    if verbose:
        print(f'try to get {len(indexes_list)} (indexes: {",".join(indexes_list)} matches stats')
    filtered = []
    i = 1
    for match in matches:
        try:
            indexes_list.index(str(i))
            filtered.append(int(match[0]))
        except:
            pass
        i += 1
    return tuple(filtered)


def get_team_matches_stats(team_id: str, login: str, password: str, verbose=False):
    matches = get_team_matches(team_id, login, password)
    i = 1
    for m in matches:
        print('{i}: [{match_id}] {teams} ({type})'.format(match_id=m[0], teams=m[2], type=m[1], i=i))
        i += 1
    print('lastX - last X matches')
    print('leagueX - last X league matches')
    print('cupX - last X cup matches')
    print('friendlyX - last X friendly matches')
    print('id1,id2,id3,... - selected matches (index)')
    print('q - quit')
    decision = input('decision: ')
    ids = []
    if re.match('last(\d+)', decision):
        ids = get_team_match_ids_stats_last(matches, decision, verbose)
    elif re.match('league(\d+)', decision):
        ids = get_team_match_ids_stats_league(matches, decision, verbose)
    elif re.match('cup(\d+)', decision):
        ids = get_team_match_ids_stats_cup(matches, decision, verbose)
    elif re.match('friendly(\d+)', decision):
        ids = get_team_match_ids_stats_friendly(matches, decision, verbose)
    elif re.match('^\d+(,\d+)*$', decision):
        ids = get_team_match_ids_stats_indexes(matches, decision, verbose)
    elif decision == 'q':
        return None
    else:
        print("not recognize decision")
    teams_events = get_teams_events(ids, verbose)
    s = ''
    for team, attempts in teams_events[0].items():
        s += f'{team}:\n'
        for attempt, decisions in attempts.items():
            s += f'  {attempt}: '
            tmp = []
            for type, percent in decisions.items():
                tmp.append(f'{type}: {percent}')
            s += f'{", ".join(tmp)}\n'
    print(s)
    again = input("Again? [Y/n] ")
    if again == 'Y' or again == 'y' or again == '':
        get_team_matches_stats(team_id, login, password, verbose)

