from stats.match_stats import *
from u21 import db

default_u21_matches_file = 'u21_matches.txt'


def parse_unsaved_matches(original_match_ids: (Tuple, str) = default_u21_matches_file, verbose: bool = False):
    original_match_ids = original_match_ids or default_u21_matches_file
    if type(original_match_ids) is str:
        match_ids = []
        fp = open(original_match_ids)
        for match_id in fp.readlines():
            try:
                match_ids.append(int(match_id))
            except:
                continue
    else:
        match_ids = list(original_match_ids)
    saved_data = db.load_data()
    saved_match_ids = list(map(lambda match: match['match_id'], saved_data))
    match_ids_to_get_from_site = tuple(filter(lambda match_id: match_id not in saved_match_ids, match_ids))
    matches = get_matches_statistic(match_ids_to_get_from_site, verbose)
    if verbose:
        print(matches)
    return matches


def add_and_save_data(data: List, verbose: bool = False):
    saved_data = db.load_data()
    saved_data.extend(data)
    result = db.save_data(saved_data)
    if verbose:
        print('add_and_save_data: %r' % result)
    return result
