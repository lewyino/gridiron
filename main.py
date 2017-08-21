import getopt
import getpass
import sys

from calculate_best_player_position import *
from get_match_team import *
from get_player_with_potential import *
from parse_player_data_and_save_in_db import *

login = None
password = None

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
    }
)


def get_error_msg(filename):
    return 'use \'%s [args]\', allowed args: %s' % (filename, ', '.join(map(lambda p: p['name'], allow_arguments)))


def print_help():
    print('help')


def parse(verbose: bool):
    global login
    global password
    if login is None:
        login = input("Grid Iron login: ")
    if password is None:
        password = getpass.getpass("Grid Iron password: ")
    parse_player_data_and_save_in_db(login, password, verbose)


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
    try:
        opts, args = getopt.getopt(argv, "hvl:p:")
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
            global login
            login = arg
            print('You are login as: %s' % (login,))
        elif opt == '-p':
            global password
            password = arg

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
