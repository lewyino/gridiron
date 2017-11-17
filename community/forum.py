import json

from stats.match_stats import *


def print_for_forum(data: List, max_players: int = 5, file_name: str = None, verbose: bool = False):
    passing = get_best_passing(data)
    rushing = get_best_rushing(data)
    receiving = get_best_receiving(data)
    defense = get_best_defense(data)
    kicking = get_best_kicking(data)
    teams_stat = get_teams_stat(data)
    result = '=== passing ===\n'
    result += get_match_stats(passing, 'yds', ['player_name', 'yds'], '[b]QB (jardów podaniami)[/b]', max_players)
    result += '\n'
    result += get_match_stats(passing, 'lng', ['player_name', 'lng'], '[b]QB (najdłuższe podanie)[/b]', max_players)
    result += '\n'
    result += get_match_stats(passing, 'pct', ['player_name', 'pct'], '[b]QB (procent kompletnych podań)[/b]', max_players)
    result += '\n'
    result += get_match_stats(passing, 'yds_a', ['player_name', 'yds_a'], '[b]QB (jardów na podanie)[/b]', max_players)
    result += '\n'
    result += '=== receiving ===\n'
    result += get_match_stats(receiving, 'yds', ['player_name', 'yds'], '[b]WR (jardów odbiorami)[/b]', max_players)
    result += '\n'
    result += get_match_stats(receiving, 'rec', ['player_name', 'rec'], '[b]WR (odebranych podań)[/b]', max_players)
    result += '\n'
    result += get_match_stats(receiving, 'avg', ['player_name', 'avg'], '[b]WR (jardów na odbiór)[/b]', max_players)
    result += '\n'
    result += get_match_stats(receiving, 'lng', ['player_name', 'lng'], '[b]WR (najdłuższy odbiór)[/b]', max_players)
    result += '\n'
    result += '=== rushing ===\n'
    result += get_match_stats(rushing, 'yds', ['player_name', 'yds'], '[b]RB (jardów biegami)[/b]', max_players)
    result += '\n'
    result += get_match_stats(rushing, 'yds_a', ['player_name', 'yds_a'], '[b]RB (jardów na bieg)[/b]', max_players)
    result += '\n'
    result += get_match_stats(rushing, 'lng', ['player_name', 'lng'], '[b]RB (najdłuższy bieg)[/b]', max_players)
    result += '\n'
    result += '=== defense ===\n'
    result += get_match_stats(defense, 'interceptions', ['player_name', 'interceptions'], '[b]DEF (przechwytów)[/b]', max_players)
    result += '\n'
    result += get_match_stats(defense, 'sacks', ['player_name', 'sacks'], '[b]DEF (sacków)[/b]', max_players)
    result += '\n'
    result += get_match_stats(defense, 'tackles', ['player_name', 'tackles'], '[b]DEF (tackli)[/b]', max_players)
    result += '\n'
    result += get_match_stats(defense, 'fumbles', ['player_name', 'fumbles'], '[b]DEF (upuszczonych piłek)[/b]', max_players)
    result += '\n'
    result += '=== kicking ===\n'
    result += get_match_stats(kicking, 'fgm', ['player_name', 'fgm'], '[b]K (gole trafione)[/b]', max_players)
    result += '\n'
    result += get_match_stats(kicking, 'pct', ['player_name', 'pct'], '[b]K (procent trafionych goli)[/b]', max_players)
    result += '\n'
    result += get_match_stats(kicking, 'lng', ['player_name', 'lng'], '[b]K (najdłuższy gol)[/b]', max_players)
    result += '\n'
    result += '=== team ===\n'
    result += get_match_stats(teams_stat, 'score', ['team_name', 'score'], '[b]TEAM (punkty zdobyte)[/b]', max_players)
    result += '\n'
    result += get_match_stats(teams_stat, 'score_lost', ['team_name', 'score_lost'], '[b]TEAM (punkty stracone)[/b]', max_players)
    result += '\n'
    result += get_match_stats(teams_stat, 'total_yards', ['team_name', 'total_yards'], '[b]TEAM (suma jardów)[/b]', max_players)
    result += '\n'
    result += get_match_stats(teams_stat, 'passing_yards', ['team_name', 'passing_yards'], '[b]TEAM (jardów podaniami)[/b]', max_players)
    result += '\n'
    result += get_match_stats(teams_stat, 'rushing_yards', ['team_name', 'rushing_yards'], '[b]TEAM (jardów biegami)[/b]', max_players)
    result += '\n'
    result += get_match_stats(teams_stat, 'fg', ['team_name', 'fg'], '[b]TEAM (fg)[/b]', max_players)
    result += '\n'
    result += get_match_stats(teams_stat, 'interceptions', ['team_name', 'interceptions'], '[b]TEAM (przechwytów)[/b]', max_players)
    result += '\n'
    result += get_match_stats(teams_stat, 'sacks', ['team_name', 'sacks'], '[b]TEAM (sacków)[/b]', max_players)
    result += '\n'
    result += get_match_stats(teams_stat, 'tackles', ['team_name', 'tackles'], '[b]TEAM (tackli)[/b]', max_players)
    result += '\n'
    result += get_match_stats(teams_stat, 'fumbles', ['team_name', 'fumbles'], '[b]TEAM (upuszczonych piłek)[/b]', max_players)
    if verbose:
        print(result)
    if file_name:
        fp = open(file_name, 'w', encoding="utf8")
        fp.write(result)
        fp.close()


def print_for_forum_small(data: List, max_players: int = 5, file_name: str = None, verbose: bool = False):
    passing = get_best_passing(data)
    rushing = get_best_rushing(data)
    receiving = get_best_receiving(data)
    defense = get_best_defense(data)
    teams_stat = get_teams_stat(data)
    result = get_match_stats(passing, 'lng', ['player_name', 'lng'], '[b]QB (najdłuższe podanie)[/b]', max_players)
    result += '\n'
    result += get_match_stats(passing, 'yds_a', ['player_name', 'yds_a'], '[b]QB (jardów na podanie)[/b]', max_players)
    result += '\n'
    result += get_match_stats(receiving, 'lng', ['player_name', 'lng'], '[b]WR (najdłuższy odbiór)[/b]', max_players)
    result += '\n'
    result += get_match_stats(receiving, 'avg', ['player_name', 'avg'], '[b]WR (jardów na odbiór)[/b]', max_players)
    result += '\n'
    result += get_match_stats(rushing, 'lng', ['player_name', 'lng'], '[b]RB (najdłuższy bieg)[/b]', max_players)
    result += '\n'
    result += get_match_stats(defense, 'tackles', ['player_name', 'tackles'], '[b]DEF (tackli)[/b]', max_players)
    result += '\n'
    result += get_match_stats(defense, 'fumbles', ['player_name', 'fumbles'], '[b]DEF (upuszczonych piłek)[/b]', max_players)
    result += '\n'
    result += get_match_stats(teams_stat, 'score', ['team_name', 'score'], '[b]TEAM (punkty zdobyte)[/b]', max_players)
    result += '\n'
    result += get_match_stats(teams_stat, 'score_lost', ['team_name', 'score_lost'], '[b]TEAM (punkty stracone)[/b]', max_players)
    result += '\n'
    result += get_match_stats(teams_stat, 'total_yards', ['team_name', 'total_yards'], '[b]TEAM (suma jardów)[/b]', max_players)
    result += '\n'
    result += get_match_stats(teams_stat, 'passing_yards', ['team_name', 'passing_yards'], '[b]TEAM (jardów podaniami)[/b]', max_players)
    result += '\n'
    result += get_match_stats(teams_stat, 'rushing_yards', ['team_name', 'rushing_yards'], '[b]TEAM (jardów biegami)[/b]', max_players)
    result += '\n'
    result += get_match_stats(teams_stat, 'fg', ['team_name', 'fg'], '[b]TEAM (fg)[/b]', max_players)
    result += '\n'
    result += get_match_stats(teams_stat, 'interceptions', ['team_name', 'interceptions'], '[b]TEAM (przechwytów)[/b]', max_players)
    result += '\n'
    result += get_match_stats(teams_stat, 'sacks', ['team_name', 'sacks'], '[b]TEAM (sacków)[/b]', max_players)
    result += '\n'
    result += get_match_stats(teams_stat, 'tackles', ['team_name', 'tackles'], '[b]TEAM (tackli)[/b]', max_players)
    result += '\n'
    result += get_match_stats(teams_stat, 'fumbles', ['team_name', 'fumbles'], '[b]TEAM (upuszczonych piłek)[/b]', max_players)
    if verbose:
        print(result)
    if file_name:
        fp = open(file_name, 'w', encoding="utf8")
        fp.write(result)
        fp.close()


def print_over_21_players(data: List, file_name: str = None, verbose: bool = False):
    result = ''
    for match in data:
        tmp_result = ''
        home_team = match['home_team']
        away_team = match['away_team']
        home_roster = home_team['roster']
        away_roster = away_team['roster']
        home_team_o21_players = tuple(filter(lambda r: 'age' in r and r['age'] > 21, home_roster))
        away_team_o21_players = tuple(filter(lambda r: 'age' in r and r['age'] > 21, away_roster))
        if len(home_team_o21_players) > 0 or len(away_team_o21_players) > 0:
            tmp_result += 'match_id: %d (%s - %s)\n' % (match['match_id'], home_team['name'], away_team['name'])
            if len(home_team_o21_players) > 0:
                for p in home_team_o21_players:
                    tmp_result += '%s (%s, %s), age: %d\n' % (p['player_name'], home_team['name'], p['position'], p['age'])
            if len(away_team_o21_players) > 0:
                for p in away_team_o21_players:
                    tmp_result += '%s (%s, %s), age: %d\n' % (p['player_name'], away_team['name'], p['position'], p['age'])
        if tmp_result:
            result += tmp_result + '\n'
    if verbose:
        print(result)
    if file_name:
        fp = open(file_name, 'w', encoding="utf8")
        fp.write(result)
        fp.close()


def print_mvp(data: List, file_name: str = None, verbose: bool = False):
    qb = __get_qb_mvp(data, verbose)
    wr = __get_wr_mvp(data, verbose)
    rb = __get_rb_mvp(data, verbose)
    deff = __get_def_mvp(data, verbose)
    result = 'QB: %s\n' % qb[0]['player_name']
    result += 'WR: %s\n' % wr[0]['player_name']
    result += 'RB: %s\n' % rb[0]['player_name']
    result += 'DEF: %s\n' % deff[0]['player_name']
    if verbose:
        print(result)
    if file_name:
        fp = open(file_name, 'w', encoding="utf8")
        fp.write(result + '\n')
        fp.write('QB: %s' % json.dumps(qb))
        fp.write('WR: %s' % json.dumps(wr))
        fp.write('RB: %s' % json.dumps(rb))
        fp.write('DEF: %s' % json.dumps(deff))
        fp.close()
    return {
        'qb': qb,
        'wr': wr,
        'rb': rb,
        'def': deff
    }


def __get_qb_mvp(data: List, verbose: bool = False):
    player_list = []
    for d in data:
        scoring = d['scoring']
        home_team_passing = d['home_team']['passing']
        if home_team_passing:
            player_list.append(__get_qb_point(home_team_passing, d['home_team']['receiving'], scoring, verbose))
        away_team_passing = d['away_team']['passing']
        if away_team_passing:
            player_list.append(__get_qb_point(away_team_passing, d['away_team']['receiving'], scoring, verbose))
    player_list = sorted(player_list, key=lambda p: p['point'], reverse = True)
    if verbose:
        print('QB:', player_list)
    return player_list


def __get_qb_point(player: Dict, receiving: List, scoring: List, verbose: bool = False):
    point = player['pct'] / 10
    point += float(player['yds']) * 0.04
    point += float(player['lng']) / 20
    receiving_ids = list(map(lambda r: r['player_id'], receiving))
    scoring_td = list(filter(lambda p: p['point_type'] == 'TD', scoring))
    scoring_receiving = list(filter(lambda p: p['player_id'] in receiving_ids, scoring_td))
    td = len(scoring_receiving)
    point += td * 4
    if verbose:
        print('[QB] %s: %.3f' % (player['player_name'], point))
    return {
        'player_name': player['player_name'],
        'player_id': player['player_id'],
        'point': point,
        'yds': player['yds'],
        'pct': player['pct'],
        'td': td
    }


def __get_wr_mvp(data: List, verbose: bool = False):
    player_list = []
    for d in data:
        scoring = d['scoring']
        home_team_receiving = d['home_team']['receiving']
        if home_team_receiving:
            for r in home_team_receiving:
                player_list.append(__get_wr_point(r, scoring, verbose))
        away_team_receiving = d['away_team']['receiving']
        if away_team_receiving:
            for r in away_team_receiving:
                player_list.append(__get_wr_point(r, scoring, verbose))
    player_list = sorted(player_list, key=lambda p: p['point'], reverse = True)
    if verbose:
        print('WR:', player_list)
    return player_list


def __get_wr_point(player: List, scoring: List, verbose: bool = False):
    point = player['avg'] / 5
    point += float(player['yds']) * 0.1
    point += float(player['lng']) / 20
    point += float(player['rec']) / 5
    scoring_td = list(filter(lambda p: p['point_type'] == 'TD', scoring))
    scoring_receiving = list(filter(lambda p: p['player_id'] == player['player_id'], scoring_td))
    td = len(scoring_receiving)
    point += td * 6
    if verbose:
        print('[WR] %s: %.3f' % (player['player_name'], point))
    return {
        'player_name': player['player_name'],
        'player_id': player['player_id'],
        'point': point,
        'yds': player['yds'],
        'rec': player['rec'],
        'avg': player['avg'],
        'td': td
    }


def __get_rb_mvp(data: List, verbose: bool = False):
    player_list = []
    for d in data:
        scoring = d['scoring']
        home_team_rushing = d['home_team']['rushing']
        if home_team_rushing:
            for r in home_team_rushing:
                player_list.append(__get_rb_point(r, scoring, verbose))
        away_team_rushing = d['away_team']['rushing']
        if away_team_rushing:
            for r in away_team_rushing:
                player_list.append(__get_rb_point(r, scoring, verbose))
    player_list = sorted(player_list, key=lambda p: p['point'], reverse = True)
    if verbose:
        print('RB:', player_list)
    return player_list


def __get_rb_point(player: List, scoring: List, verbose: bool = False):
    point = float(player['yds']) * 0.1
    point += float(player['lng']) / 20
    point += player['yds_a'] / 5
    scoring_td = list(filter(lambda p: p['point_type'] == 'TD', scoring))
    scoring_rushing = list(filter(lambda p: p['player_id'] == player['player_id'], scoring_td))
    td = len(scoring_rushing)
    point += td * 6
    if verbose:
        print('[RB] %s: %.3f' % (player['player_name'], point))
    return {
        'player_name': player['player_name'],
        'player_id': player['player_id'],
        'point': point,
        'yds': player['yds'],
        'lng': player['lng'],
        'yds_a': player['yds_a'],
        'td': td
    }


def __get_def_mvp(data: List, verbose: bool = False):
    player_list = []
    for d in data:
        home_team_defence = d['home_team']['defense']
        if home_team_defence:
            for r in home_team_defence:
                player_list.append(__get_def_point(r, verbose))
        away_team_defence = d['away_team']['defense']
        if away_team_defence:
            for r in away_team_defence:
                player_list.append(__get_def_point(r, verbose))
    player_list = sorted(player_list, key=lambda p: p['point'], reverse = True)
    if verbose:
        print('DEF:', player_list)
    return player_list


def __get_def_point(player: List, verbose: bool = False):
    point = player['tackles']
    point += player['interceptions'] * 3
    point += player['sacks'] * 2
    point += player['fumbles'] * 2
    if verbose:
        print('[DEF] %s: %.3f' % (player['player_name'], point))
    return {
        'player_name': player['player_name'],
        'player_id': player['player_id'],
        'point': point,
        'tackles': player['tackles'],
        'interceptions': player['interceptions'],
        'sacks': player['sacks'],
        'fumbles': player['fumbles']
    }
