import argparse
import getpass
from typing import Callable

from calculate_best_player_position import *
from get_match_team import *
from get_player_with_potential import *
from parse_team_data import get_players_data
from stats.match_stats import *
from stats.team_stats import *

# allow_methods = (
#     {
#         'name': 'calculate_position',
#         'method': 'calculate_position'
#     },
#     {
#         'name': 'potential_player',
#         'method': 'potential_player'
#     },
#     {
#         'name': 'stats',
#         'method': 'stats'
#     },
#     {
#         'name': 'match_stats',
#         'method': 'match_stats'
#     },
#     {
#         'name': 'teams_events',
#         'method': 'teams_events'
#     }
# )


def parse_team_data(verbose: bool, _config: Dict):
    get_players_data(_config['login'], _config['password'])
    # parse_player_data_and_save_in_db(_config['login'], _config['password'], _config['verbose'])


def calculate_position(verbose: bool):
    quantity = int(input("Players quantity for position: "))
    with_save = input("Save calculated position in db (Y/N): ")
    if with_save in ('Y', 'N', 'y', 'n'):
        with_save = True if with_save in ('Y', 'y') else False
        calculate_best_player_position(quantity, with_save, verbose)
    else:
        raise SyntaxError("Wrong input parameter")


def potential_player(verbose: bool):
    min_talent = float(input("Minimum talent (number, float): "))
    min_teamwork = int(input("Minimum teamwork (number, integer): "))
    min_consistency = int(input("Minimum consistency (number, integer): "))
    max_age = int(input("Maximum age (number, integer): "))
    get_player_with_potential(min_talent, min_teamwork, min_consistency, max_age, verbose)


def stats(verbose: bool):
    global app_opts
    get_team_stats(app_opts['m'], verbose)


def match_stats(verbose: bool):
    global app_opts
    if not app_opts['login']:
        app_opts['login'] = input("Grid Iron login: ")
    if not app_opts['password']:
        app_opts['password'] = getpass.getpass("Grid Iron password: ")
    match_ids = input("Match id: ")
    matches = get_matches_statistic(tuple(map(lambda m: int(m), match_ids.split(','))), verbose)
    for match in matches:
        roster = get_match_roster(match['match_id'], verbose)
        home_team = match['home_team']
        away_team = match['away_team']
        home_team['roster'] = roster['home_team_roster']
        away_team['roster'] = roster['away_team_roster']
        enrich_roster_players_with_age(home_team['id'], home_team['roster'], app_opts['login'], app_opts['password'], verbose)
    print(matches)


def teams_events(verbose: bool, _config: Dict):
    match_ids = input("Match id: ")
    matches = get_teams_events(tuple(map(lambda m: int(m), match_ids.split(','))), verbose)
    print(matches[0])


def team_events(verbose: bool):
    team_id = input("Team id: ")
    get_team_matches_stats(team_id, app_opts['login'], app_opts['password'], verbose)


def match_team(verbose: bool):
    formation = [
        Formation('qb', 1),
        Formation('wr', 1),
        Formation('de', 2),
        Formation('cb', 2),
        Formation('te', 2),
        Formation('olb', 2),
        Formation('mlb', 1),
        Formation('sf', 2),
        Formation('ol', 5),
        Formation('dl', 2),
        Formation('rb', 2),
    ]
    get_match_team(formation, verbose)


allow_methods: Dict[str, Callable] = {
    'parse_team_data': parse_team_data,
    'team_events': team_events
}


def parse_argv_argparse() -> Dict:
    parser = argparse.ArgumentParser(description='GridIron manager tool',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-v', '--verbose', action='store_true', help='increase verbosity')
    parser.add_argument('-l', '--login', help='set GridIron username', default='')
    parser.add_argument('-p', '--password', help='set GridIron user password', default='')
    parser.add_argument('-o', '--output', help='set a default output directory', default='output')
    parser.add_argument('method', help=f'method to run, available:  {", ".join(allow_methods.keys())}')
    args = parser.parse_args()
    return vars(args)


def validate_config_and_get_necessary_data(_config: Dict) -> Tuple[int, str | Dict]:
    if _config['method'] not in allow_methods.keys():
        return 1, f'method "{_config["method"]}" is not available'
    if not _config['login']:
        _config['login'] = input('GridIron username: ')
    if not _config['password']:
        _config['password'] = getpass.getpass("GridIron password: ")
    if _config['verbose']:
        print(f'call "{_config["method"]}" method')
    return 0, _config


if __name__ == "__main__":
    config = parse_argv_argparse()
    code, config = validate_config_and_get_necessary_data(config)
    if code != 0:
        print(config)
        exit(code)
    to_run = allow_methods[config['method']]
    to_run(config['verbose'], config)
