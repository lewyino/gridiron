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
    result += '\=== defense ===\n'
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