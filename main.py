import getopt
import getpass
import sys

from calculate_best_player_position import *
from community.games import *
from get_match_team import *
from get_player_with_potential import *
from parse_player_data_and_save_in_db import *
from stats.match_stats import *
from stats.team_stats import *

app_opts = {
    'login': None,
    'password': None,
    'm': None,
    'o': 'output'
}

allow_arguments = (
    {
        'name': 'parse',
        'method': 'parse'
    },
    {
        'name': 'calculate_position',
        'method': 'calculate_position'
    },
    {
        'name': 'potential_player',
        'method': 'potential_player'
    },
    {
        'name': 'stats',
        'method': 'stats'
    },
    {
        'name': 'match_stats',
        'method': 'match_stats'
    },
    {
        'name': 'teams_events',
        'method': 'teams_events'
    },
    {
        'name': 'u21',
        'method': 'u21'
    },
    {
        'name': 'pp',
        'method': 'pp'
    },
    {
        'name': 'my',
        'method': 'my'
    }
)


def get_error_msg(filename):
    return 'use \'%s [args]\', allowed args: %s' % (filename, ', '.join(map(lambda p: p['name'], allow_arguments)))


def print_help():
    print('help')


def parse(verbose: bool):
    global app_opts
    if app_opts['login'] is None:
        app_opts['login'] = input("Grid Iron login: ")
    if app_opts['password'] is None:
        app_opts['password'] = getpass.getpass("Grid Iron password: ")
    parse_player_data_and_save_in_db(app_opts['login'], app_opts['password'], verbose)


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
    if app_opts['login'] is None:
        app_opts['login'] = input("Grid Iron login: ")
    if app_opts['password'] is None:
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


def teams_events(verbose: bool):
    global app_opts
    if app_opts['login'] is None:
        app_opts['login'] = input("Grid Iron login: ")
    if app_opts['password'] is None:
        app_opts['password'] = getpass.getpass("Grid Iron password: ")
    match_ids = input("Match id: ")
    matches = get_teams_events(tuple(map(lambda m: int(m), match_ids.split(','))), verbose)
    print(matches[0])


def u21(verbose: bool):
    global app_opts
    if app_opts['login'] is None:
        app_opts['login'] = input("Grid Iron login: ")
    if app_opts['password'] is None:
        app_opts['password'] = getpass.getpass("Grid Iron password: ")
    make_all(app_opts['login'], app_opts['password'], 'u21', verbose)


def pp(verbose: bool):
    global app_opts
    if app_opts['login'] is None:
        app_opts['login'] = input("Grid Iron login: ")
    if app_opts['password'] is None:
        app_opts['password'] = getpass.getpass("Grid Iron password: ")
    output = {
        'new_data': True,
        'all_data': True,
        'mvp': True
    }
    make_output(app_opts['login'], app_opts['password'], 'pp', verbose, output)


def my(verbose: bool):
    data = u21_db.load_data('output/pp.json')
    round_1 = list(filter(lambda d: d['round'] == 1, data))
    max_round_1 = max(map(lambda d: d['audience'], round_1))
    max_round = [list(filter(lambda d: d['audience'] == max_round_1, round_1))[0]]
    round_2 = list(filter(lambda d: d['round'] == 2, data))
    max_round_2 = max(map(lambda d: d['audience'], round_2))
    max_round.append(list(filter(lambda d: d['audience'] == max_round_2, round_2))[0])
    round_3 = list(filter(lambda d: d['round'] == 3, data))
    max_round_3 = max(map(lambda d: d['audience'], round_3))
    max_round.append(list(filter(lambda d: d['audience'] == max_round_3, round_3))[0])
    round_4 = list(filter(lambda d: d['round'] == 4, data))
    max_round_4 = max(map(lambda d: d['audience'], round_4))
    max_round.append(list(filter(lambda d: d['audience'] == max_round_4, round_4))[0])
    for d in max_round:
        print('%s - %s: %d' % (d['home_team']['name'], d['away_team']['name'], d['audience']))
    print(data)

    passing = get_best_passing(data)
    print(passing)
    print(get_match_stats(passing, 'pct', ['player_name', 'pct'], '[b]QB (procent kompletnych podań)[/b]', 5))


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


def parse_argv(argv):
    print(argv)
    global app_opts
    try:
        opts, args = getopt.getopt(argv, "hvl:p:m:o:")
        print('opts', opts)
        print('args', args)
    except getopt.GetoptError:
        sys.exit(2)

    verbose = False

    for opt, arg in opts:
        if opt == '-h':
            print_help()
            exit(0)
        elif opt == '-v':
            print('verbose')
            verbose = True
        elif opt == '-l':
            app_opts['login'] = arg
            print('You are login as: %s' % (app_opts['login'],))
        elif opt == '-p':
            app_opts['password'] = arg
        elif opt == '-m':
            app_opts['m'] = int(arg)
        elif opt == '-o':
            app_opts['o'] = arg

    print(opts)
    print(app_opts)

    for arg in args:
        for ap in allow_arguments:
            if arg == ap['name']:
                print('call \'%s\' method' % (arg,))
                method = eval(ap['method'])
                method(verbose)
                exit(0)


if __name__ == "__main__":
    parse_argv(sys.argv[1:])
    print(get_error_msg(sys.argv[0]))


# get_best_players_for_position('MLB', 10)
# get_best_players_by_skill('strength', 15)
# get_best_players_by_skill('tackling', 6)
