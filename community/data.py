import main
from community import db
from stats.match_stats import *

default_u21_matches_file = main.app_opts['o'] + '/u21_matches.txt'


def parse_unsaved_matches(original_match_ids: (Tuple, str) = default_u21_matches_file, login: str = '', password: str = '', verbose: bool = False):
    original_match_ids = original_match_ids or default_u21_matches_file
    if type(original_match_ids) is str:
        match_round = {}
        tmp_round = 1
        match_ids = []
        fp = open(original_match_ids)
        for match_id in fp.readlines():
            try:
                int_match_id = int(match_id)
                match_ids.append(int_match_id)
                match_round[int_match_id] = tmp_round
            except:
                tmp_round += 1
                continue
    else:
        match_ids = list(original_match_ids)
    saved_data = db.load_data()
    saved_match_ids = list(map(lambda match: match['match_id'], saved_data))
    match_ids_to_get_from_site = tuple(filter(lambda match_id: match_id not in saved_match_ids, match_ids))
    matches = get_matches_statistic(match_ids_to_get_from_site, verbose)
    for match in matches:
        my_match_round = match_round[match['match_id']]
        if my_match_round:
            match['round'] = my_match_round
        roster = get_match_roster(match['match_id'], verbose)
        home_team = match['home_team']
        away_team = match['away_team']
        home_team['roster'] = roster['home_team_roster']
        away_team['roster'] = roster['away_team_roster']
        time.sleep(3)
        enrich_roster_players_with_age(home_team['id'], home_team['roster'], login, password, verbose)
        time.sleep(3)
        enrich_roster_players_with_age(away_team['id'], away_team['roster'], login, password, verbose)
    if verbose:
        print(matches)
    return matches


def add_and_save_data(data: List, verbose: bool = False, db_file: str = None):
    saved_data = db.load_data(db_file)
    saved_data.extend(data)
    result = db.save_data(saved_data, db_file)
    if verbose:
        print('add_and_save_data: %r' % result)
    return result
