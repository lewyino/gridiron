import time
from typing import Tuple, List, Dict

from site_parser.GridIronLoginUrllib import GridIronLoginUrllib as GridIronLogin
from site_parser.GridIronParser import GridIronParser
from site_parser.MatchParser import MatchParser
from site_parser.MatchStatisticParser import MatchStatisticParser
from site_parser.MatchTeamsParser import MatchTeamsParser


def get_matches_statistic(match_ids: Tuple[int], verbose: bool = False):
    matches = []
    for match_id in match_ids:
        page_boxscore = get_match_boxscore_page(match_id, verbose)
        msp = MatchStatisticParser(match_id, page_boxscore)
        msp.get_teams()
        msp.get_score()
        msp.get_scoring()
        msp.get_teams_stat()
        msp.get_teams_passing()
        msp.get_teams_rushing()
        msp.get_teams_receiving()
        msp.get_teams_kicking()
        msp.get_teams_defense()
        result = msp.get_result()
        page = get_match_page(match_id, verbose)
        mp = MatchParser(page)
        result['audience'] = mp.get_audience()
        matches.append(result)
        time.sleep(3)
    return matches


def get_match_boxscore_page(match_id: int, verbose: bool = False):
    if verbose:
        print('get match statistic for match_id: %d' % match_id)
    return GridIronLogin.get_match_statistic_site(match_id)


def get_match_page(match_id: int, verbose: bool = False):
    if verbose:
        print('get match page for match_id: %d' % match_id)
    return GridIronLogin.get_match_site(match_id)


def get_match_roster(match_id: int, verbose: bool = False):
    roster_page = get_match_roster_page(match_id, verbose)
    mtp = MatchTeamsParser(roster_page)
    return {
        'home_team_roster': mtp.get_home_team(),
        'away_team_roster': mtp.get_away_team(),
    }


def get_match_roster_page(match_id: int, verbose: bool = False):
    if verbose:
        print('get match roster for match_id: %d' % match_id)
    return GridIronLogin.get_match_teams_site(match_id)


def get_best_passing(matches: List):
    passing = {}
    for match in matches:
        home_team = match['home_team']
        home_passing = __get_match_passing(home_team, passing)
        if home_passing:
            passing[home_passing[0]] = home_passing[1]
        away_team = match['away_team']
        away_passing = __get_match_passing(away_team, passing)
        if away_passing:
            passing[away_passing[0]] = away_passing[1]
    return {
        'yds': sorted(passing.values(), key=lambda p: p['yds'], reverse = True),
        'yds_a': sorted(passing.values(), key=lambda p: p['yds_a'], reverse = True),
        'pct': sorted(passing.values(), key=lambda p: p['pct'], reverse = True),
        'lng': sorted(passing.values(), key=lambda p: p['lng'], reverse = True),
    }


def __get_match_passing(team, passing: Dict):
    if 'passing' not in team or team['passing'] is None:
        return None
    passing_tmp = team['passing']
    if passing_tmp['player_id'] in passing:
        player = passing[passing_tmp['player_id']]
        player['att'] += passing_tmp['att']
        player['comp'] += passing_tmp['comp']
        player['yds'] += passing_tmp['yds']
        player['yds_a'] = float(player['yds']) / player['att']
        player['pct'] = (float(player['comp']) / player['att']) * 100
        player['lng'] = passing_tmp['lng'] if passing_tmp['lng'] > player['lng'] else player['lng']
    else:
        player = {
            'att': passing_tmp['att'],
            'comp': passing_tmp['comp'],
            'player_id': passing_tmp['player_id'],
            'yds_a': passing_tmp['yds_a'],
            'pct': passing_tmp['pct'],
            'yds': passing_tmp['yds'],
            'lng': passing_tmp['lng'],
            'player_name': passing_tmp['player_name']
        }
    return passing_tmp['player_id'], player


def get_best_rushing(matches: List):
    rushing = {}
    for match in matches:
        home_team = match['home_team']
        for rush in home_team['rushing']:
            home_rushing = __get_match_rushing(rush, rushing)
            rushing[home_rushing[0]] = home_rushing[1]
        away_team = match['away_team']
        for rush in away_team['rushing']:
            away_rushing = __get_match_rushing(rush, rushing)
            rushing[away_rushing[0]] = away_rushing[1]
    return {
        'yds': sorted(rushing.values(), key=lambda p: p['yds'], reverse = True),
        'yds_a': sorted(rushing.values(), key=lambda p: p['yds_a'], reverse = True),
        'lng': sorted(rushing.values(), key=lambda p: p['lng'], reverse = True),
    }


def __get_match_rushing(rush, rushing: Dict):
    if rush['player_id'] in rushing:
        player = rushing[rush['player_id']]
        player['att'] += rush['att']
        player['yds'] += rush['yds']
        player['yds_a'] = float(player['yds']) / player['att']
        player['lng'] = rush['lng'] if rush['lng'] > player['lng'] else player['lng']
    else:
        player = {
            'att': rush['att'],
            'player_id': rush['player_id'],
            'yds_a': rush['yds_a'],
            'yds': rush['yds'],
            'lng': rush['lng'],
            'player_name': rush['player_name']
        }
    return rush['player_id'], player


def get_best_receiving(matches: List):
    receiving = {}
    for match in matches:
        home_team = match['home_team']
        for rush in home_team['receiving']:
            home_receiving = __get_match_receiving(rush, receiving)
            receiving[home_receiving[0]] = home_receiving[1]
        away_team = match['away_team']
        for rush in away_team['receiving']:
            away_receiving = __get_match_receiving(rush, receiving)
            receiving[away_receiving[0]] = away_receiving[1]
    return {
        'yds': sorted(receiving.values(), key=lambda p: p['yds'], reverse = True),
        'rec': sorted(receiving.values(), key=lambda p: p['rec'], reverse = True),
        'lng': sorted(receiving.values(), key=lambda p: p['lng'], reverse = True),
        'avg': sorted(receiving.values(), key=lambda p: p['avg'], reverse = True),
    }


def __get_match_receiving(receive, receiving: Dict):
    if receive['player_id'] in receiving:
        player = receiving[receive['player_id']]
        player['rec'] += receive['rec']
        player['yds'] += receive['yds']
        player['avg'] = float(player['yds']) / player['rec']
        player['lng'] = receive['lng'] if receive['lng'] > player['lng'] else player['lng']
    else:
        player = {
            'avg': receive['avg'],
            'player_id': receive['player_id'],
            'rec': receive['rec'],
            'yds': receive['yds'],
            'lng': receive['lng'],
            'player_name': receive['player_name']
        }
    return receive['player_id'], player


def get_best_defense(matches: List):
    defense = {}
    for match in matches:
        home_team = match['home_team']
        for d in home_team['defense']:
            home_defense = __get_match_defense(d, defense)
            defense[home_defense[0]] = home_defense[1]
        away_team = match['away_team']
        for d in away_team['defense']:
            away_defense = __get_match_defense(d, defense)
            defense[away_defense[0]] = away_defense[1]
    return {
        'tackles': sorted(defense.values(), key=lambda p: p['tackles'], reverse = True),
        'sacks': sorted(defense.values(), key=lambda p: p['sacks'], reverse = True),
        'fumbles': sorted(defense.values(), key=lambda p: p['fumbles'], reverse = True),
        'interceptions': sorted(defense.values(), key=lambda p: p['interceptions'], reverse = True),
    }


def __get_match_defense(d, defense: Dict):
    if d['player_id'] in defense:
        player = defense[d['player_id']]
        player['tackles'] += d['tackles']
        player['sacks'] += d['sacks']
        player['fumbles'] += d['fumbles']
        player['interceptions'] += d['interceptions']
    else:
        player = {
            'tackles': d['tackles'],
            'player_id': d['player_id'],
            'sacks': d['sacks'],
            'fumbles': d['fumbles'],
            'interceptions': d['interceptions'],
            'player_name': d['player_name']
        }
    return d['player_id'], player


def get_best_kicking(matches: List):
    kicking = {}
    for match in matches:
        home_team = match['home_team']
        home_kicking = __get_match_kicking(home_team, kicking)
        if home_kicking:
            kicking[home_kicking[0]] = home_kicking[1]
        away_team = match['away_team']
        away_kicking = __get_match_kicking(away_team, kicking)
        if away_kicking:
            kicking[away_kicking[0]] = away_kicking[1]
    return {
        'fgm': sorted(kicking.values(), key=lambda p: p['fgm'], reverse = True),
        'fga': sorted(kicking.values(), key=lambda p: p['fga'], reverse = True),
        'pct': sorted(kicking.values(), key=lambda p: p['pct'], reverse = True),
        'lng': sorted(kicking.values(), key=lambda p: p['lng'], reverse = True),
    }


def __get_match_kicking(team, kicking: Dict):
    if 'kicking' not in team or team['kicking'] is None:
        return None
    kicking_tmp = team['kicking']
    if kicking_tmp['player_id'] in kicking:
        player = kicking[kicking_tmp['player_id']]
        player['fgm'] += kicking_tmp['fgm']
        player['fga'] += kicking_tmp['fga']
        player['pct'] = round(float(player['fgm']) / player['fga'] * 100, 1)
        player['lng'] = kicking_tmp['lng'] if kicking_tmp['lng'] > player['lng'] else player['lng']
    else:
        player = {
            'fgm': kicking_tmp['fgm'],
            'fga': kicking_tmp['fga'],
            'player_id': kicking_tmp['player_id'],
            'pct': kicking_tmp['pct'],
            'lng': kicking_tmp['lng'],
            'player_name': kicking_tmp['player_name']
        }
    return kicking_tmp['player_id'], player


def get_teams_stat(matches: List):
    teams_stat = {}
    for match in matches:
        home_team = match['home_team']
        home_stats = __get_team_stat(home_team, teams_stat)
        if home_stats:
            teams_stat[home_stats[0]] = home_stats[1]
        away_team = match['away_team']
        away_stats = __get_team_stat(away_team, teams_stat)
        if away_stats:
            teams_stat[away_stats[0]] = away_stats[1]
    return {
        'total_yards': sorted(teams_stat.values(), key=lambda t: t['total_yards'], reverse = True),
        'tackles': sorted(teams_stat.values(), key=lambda t: t['tackles'], reverse = True),
        'fumbles': sorted(teams_stat.values(), key=lambda t: t['fumbles'], reverse = True),
        'rushing_yards': sorted(teams_stat.values(), key=lambda t: t['rushing_yards'], reverse = True),
        'interceptions': sorted(teams_stat.values(), key=lambda t: t['interceptions'], reverse = True),
        'passing_yards': sorted(teams_stat.values(), key=lambda t: t['passing_yards'], reverse = True),
        'sacks': sorted(teams_stat.values(), key=lambda t: t['sacks'], reverse = True),
        'fg': sorted(teams_stat.values(), key=lambda t: t['fg'], reverse = True),
        'score': sorted(teams_stat.values(), key=lambda t: t['score'], reverse = True),
        'score_lost': sorted(teams_stat.values(), key=lambda t: t['score_lost']),
    }


def __get_team_stat(team, teams_stat: Dict):
    if team['id'] in teams_stat:
        t = teams_stat[team['id']]
        t['total_yards'] += team['total_yards']
        t['tackles'] += team['tackles']
        t['fumbles'] += team['fumbles']
        t['rushing_yards'] += team['rushing_yards']
        t['interceptions'] += team['interceptions']
        t['passing_yards'] += team['passing_yards']
        t['sacks'] += team['sacks']
        t['fg'] += team['fg']
        t['score'] += team['score']
        t['score_lost'] += team['score_lost']
    else:
        t = {
            'team_name': team['name'],
            'team_id': team['id'],
            'total_yards': team['total_yards'],
            'tackles': team['tackles'],
            'fumbles': team['fumbles'],
            'rushing_yards': team['rushing_yards'],
            'interceptions': team['interceptions'],
            'passing_yards': team['passing_yards'],
            'sacks': team['sacks'],
            'fg': team['fg'],
            'score': team['score'],
            'score_lost': team['score_lost'],
        }
    return team['id'], t


def get_match_stats(dict, field, fields, title = None, max_count = 9999):
    d = dict[field]
    max_count = len(d) if len(d) < max_count else max_count
    title = title if title is not None else 'print_match_stats: %s' % field
    result = title + '\n'
    for i in range(max_count):
        tmp_d = d[i]
        s = ''
        for f in fields:
            if type(tmp_d[f]) is float:
                tmp_d[f] = format(tmp_d[f], '.2f')
            s += '%s, ' % str(tmp_d[f])
        result += s[:-2] + '\n'
    return result


def enrich_roster_players_with_age(team_id: int, roster: List, login: str, password: str, verbose: bool):
    players = __get_team_players(team_id, login, password, verbose)
    for r in roster:
        player = tuple(filter(lambda p: p.id == r['player_id'], players))
        if len(player) > 0:
            r['age'] = player[0].age
    return roster


def __get_team_players(team_id: int, login: str, password: str, verbose: bool):
    if verbose:
        print('get players for team_id: %d' % team_id)
    site = GridIronLogin(login, password)
    site.get_session()
    players_list_page = site.get_players_list_page(team_id)
    players = GridIronParser.get_players_list(players_list_page)
    return players
