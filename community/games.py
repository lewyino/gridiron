from typing import Dict

import main
from community import data as u21_data
from community import db as u21_db
from community import forum as u21_forum


def make_all(login: str, password: str, file_prefix: str = 'u21', verbose: bool = False):
    __file_prefix = main.app_opts['o'] + '/' + file_prefix + '_' if file_prefix else ''
    db_file = main.app_opts['o'] + '/' + (file_prefix or 'db') + '.json'
    new_data = u21_data.parse_unsaved_matches(__file_prefix + 'matches.txt', login, password, verbose)
    print('\n=== NEW DATA ===')
    u21_forum.print_for_forum(new_data, 5, __file_prefix + 'new_data_forum.txt', verbose)
    print('\n=== PLAYERS OVER 21 ===')
    u21_forum.print_over_21_players(new_data, __file_prefix + 'players_o21.txt', verbose)
    u21_data.add_and_save_data(new_data, verbose, db_file)
    print('\n=== ALL SMALL DATA ===')
    loaded_data = u21_db.load_data(db_file)
    u21_forum.print_for_forum_small(loaded_data, 5, __file_prefix + 'data_forum_small.txt', verbose)
    print('\n=== ALL DATA ===')
    u21_forum.print_for_forum(loaded_data, 5, __file_prefix + 'data_forum.txt', verbose)
    max_round = max(map(lambda d: d['round'], loaded_data))
    print('\n=== MVP round %d ===' % max_round)
    u21_forum.print_mvp(list(filter(lambda d: d['round'] == max_round, loaded_data)), __file_prefix + 'mvp.txt', verbose)


def make_output(login: str, password: str, file_prefix: str = 'u21', verbose: bool = False, output: Dict = None):
    if output is None:
        return make_all(login, password, file_prefix, verbose)
    __file_prefix = main.app_opts['o'] + '/' + file_prefix + '_' if file_prefix else ''
    db_file = main.app_opts['o'] + '/' + (file_prefix or 'db') + '.json'
    new_data = u21_data.parse_unsaved_matches(__file_prefix + 'matches.txt', login, password, verbose)
    u21_data.add_and_save_data(new_data, verbose, db_file)
    loaded_data = u21_db.load_data(db_file)
    if 'new_data' in output and output['new_data']:
        print('\n=== NEW DATA ===')
        u21_forum.print_for_forum(new_data, 5, __file_prefix + 'new_data_forum.txt', verbose)
    if 'over_21' in output and output['over_21']:
        print('\n=== PLAYERS OVER 21 ===')
        u21_forum.print_over_21_players(new_data, __file_prefix + 'players_o21.txt', verbose)
    if 'small_data' in output and output['small_data']:
        print('\n=== ALL SMALL DATA ===')
        u21_forum.print_for_forum_small(loaded_data, 5, __file_prefix + 'data_forum_small.txt', verbose)
    if 'all_data' in output and output['all_data']:
        print('\n=== ALL DATA ===')
        u21_forum.print_for_forum(loaded_data, 5, __file_prefix + 'data_forum.txt', verbose)
    if 'mvp' in output and output['mvp']:
        max_round = max(map(lambda d: d['round'], loaded_data))
        print('\n=== MVP round %d ===' % max_round)
        u21_forum.print_mvp(list(filter(lambda d: d['round'] == max_round, loaded_data)), __file_prefix + 'mvp.txt', verbose)