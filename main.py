import sys
import getopt
import getpass
from parse_player_data_and_save_in_db import *
from calculate_best_player_position import *
from get_player_with_potential import *
from get_match_team import *
import get_best_players_for_position

login = None
password = None


def get_error_msg(filename):
    return 'use %s with param, allowed: parse, bp' % (filename,)


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
    get_match_team(verbose)


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
        if arg == 'parse':
            parse(verbose)
            exit(0)
        elif arg == 'calculate_position':
            calculate_position(verbose)
            exit(0)
        elif arg == 'potential_player':
            potential_player(verbose)
            exit(0)
        elif arg == 'match_team':
            match_team(verbose)
            exit(0)

if __name__ == "__main__":
    parse_argv(sys.argv[1:])


# get_best_players_for_position('MLB', 10)
# get_best_players_by_skill('strength', 15)
# get_best_players_by_skill('tackling', 6)
