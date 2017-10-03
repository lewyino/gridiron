from u21 import data as u21_data
from u21 import db as u21_db
from u21 import forum as u21_forum


def make_all(login: str, password: str, verbose: bool = False):
    new_data = u21_data.parse_unsaved_matches('u21_matches.txt', login, password, verbose)
    print('\n=== NEW DATA ===')
    u21_forum.print_for_forum(new_data, 5, 'new_data_forum.txt', verbose)
    print('\n=== PLAYERS OVER 21 ===')
    u21_forum.print_over_21_players(new_data, 'players_o21.txt', verbose)
    u21_data.add_and_save_data(new_data, verbose)
    print('\n=== ALL SMALL DATA ===')
    loaded_data = u21_db.load_data()
    u21_forum.print_for_forum_small(loaded_data, 5, 'data_forum_small.txt', verbose)
    print('\n=== ALL DATA ===')
    u21_forum.print_for_forum(loaded_data, 5, 'data_forum.txt', verbose)
    max_round = max(map(lambda d: d['round'], loaded_data))
    print('\n=== MVP round %d ===' % max_round)
    u21_forum.print_mvp(list(filter(lambda d: d['round'] == max_round, loaded_data)), 'mvp.txt', verbose)
