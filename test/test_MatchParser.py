import sys
import unittest

sys.path.append('..')

from site_parser.MatchStatisticHTMLParser import *
from site_parser.MatchTeamsParser import *
from site_parser.MatchStatisticParser import MatchStatisticParser


@unittest.skip('old')
class TestMatchParser(unittest.TestCase):
    """
    Test functions from Parser class
    """

    @classmethod
    def setUpClass(cls):
        cls.parser = MatchStatisticHTMLParser()

    def test_match_statistic_html_parser(self):
        """
        Test is parser using html parser return good data
        """
        __result = {
            'home_score': [84, 28, 14, 14, 28],
            'away_score': [0, 1, 2, 3, 4],
            'home_team': 'LEWY Team',
            'away_team': 'LEGION PIŁA'
        }
        f = open('test_match_statistic.txt', encoding="utf8")
        f_data = f.read()
        f.close()
        self.parser.feed(f_data)
        self.assertDictEqual(self.parser.result, __result)

    def test_match_teams_parser_home(self):
        """
        Test is parser return home team players
        """
        __home_team = [
            {'player_id': 1776545, 'player_name': 'Kamil Šmajda', 'position': 'QB', 'player_stars': 9},
            {'player_id': 1678249, 'player_name': 'Neil Boyle', 'position': 'FB/C', 'player_stars': 8},
            {'player_id': 2105889, 'player_name': 'Gordan Šimleša', 'position': 'DE/L', 'player_stars': 7},
            {'player_id': 1791983, 'player_name': 'Vilmos Szőke', 'position': 'CB/R', 'player_stars': 8},
            {'player_id': 2227264, 'player_name': 'Alexej Lipták', 'position': '[S] CB/L', 'player_stars': 6}
        ]
        f = open('test_match_teams.txt', encoding="utf8")
        f_data = f.read()
        f.close()
        match_parser = MatchTeamsParser(f_data)
        team = match_parser.get_home_team()
        home_team_player_ids = tuple(map(lambda p: p['player_id'], __home_team))
        players = list(filter(lambda p: p['player_id'] in home_team_player_ids, team))
        self.assertListEqual(players, __home_team)

    def test_match_teams_parser_away(self):
        """
        Test is parser return away team players
        """
        __away_team = [
            {'player_id': 1948407, 'player_name': 'Yevgen Fedorov', 'position': 'QB', 'player_stars': 5},
            {'player_id': 2114794, 'player_name': 'Jindřich Hampl', 'position': 'FB/L', 'player_stars': 6},
            {'player_id': 2191331, 'player_name': 'Albrecht Pohlen', 'position': 'DE/L', 'player_stars': 6},
            {'player_id': 2076923, 'player_name': 'Otto Wiater', 'position': 'CB/R', 'player_stars': 6}
        ]
        f = open('test_match_teams.txt', encoding="utf8")
        f_data = f.read()
        f.close()
        match_parser = MatchTeamsParser(f_data)
        team = match_parser.get_away_team()
        away_team_player_ids = tuple(map(lambda p: p['player_id'], __away_team))
        players = list(filter(lambda p: p['player_id'] in away_team_player_ids, team))
        self.assertListEqual(players, __away_team)

    def test_match_statistic_parser_team(self):
        """
        Test is parser return teams data
        """
        __teams = {
            'home_team': {'id': 4775, 'name': 'LEWY Team'},
            'away_team': {'id': 4779, 'name': 'LEGION PIŁA'}
        }
        f = open('test_match_statistic.txt', encoding="utf8")
        f_data = f.read()
        f.close()
        match_parser = MatchStatisticParser(2029125, f_data)
        teams = match_parser.get_teams()
        self.assertDictEqual(teams, __teams)

    def test_match_statistic_parser_score(self):
        """
        Test is parser return score data
        """
        __score = {
            'home_team': {'score': 84, 'quarter': [28, 14, 14, 28], 'score_lost': 0},
            'away_team': {'score': 0, 'quarter': [1, 2, 3, 4], 'score_lost': 84}
        }
        f = open('test_match_statistic.txt', encoding="utf8")
        f_data = f.read()
        f.close()
        match_parser = MatchStatisticParser(2029125, f_data)
        teams = match_parser.get_score()
        self.assertDictEqual(teams, __score)

    def test_match_statistic_parser_scoring(self):
        """
        Test is parser return scoring data
        """
        __scoring = [
            {
                'point_type': 'TD',
                'player_id': 2232105,
                'player_name': 'Zygmunt Imiołek'
            },
            {
                'point_type': 'TD',
                'player_id': 2284778,
                'player_name': 'Mateusz Rycombel'
            },
            {
                'point_type': 'TD',
                'player_id': 2241778,
                'player_name': 'Aureliusz Kalandyk'
            }
        ]
        f = open('test_match_statistic.txt', encoding="utf8")
        f_data = f.read()
        f.close()
        match_parser = MatchStatisticParser(2029125, f_data)
        scoring = match_parser.get_scoring()
        self.assertListEqual(scoring[0:3], __scoring)

    def test_match_statistic_parser_teams_stat(self):
        """
        Test is parser return teams stat data
        """
        __teams_stat = {
            'home_team': {
                'total_yards': 478,
                'passing_yards': 232,
                'rushing_yards': 246,
                'tackles': 47,
                'sacks': 0,
                'interceptions': 0,
                'fumbles': 2,
                'fg': 0,
            },
            'away_team': {
                'total_yards': -6,
                'passing_yards': 8,
                'rushing_yards': -14,
                'tackles': 27,
                'sacks': 1,
                'interceptions': 0,
                'fumbles': 8,
                'fg': 0,
            }
        }
        f = open('test_match_statistic.txt', encoding="utf8")
        f_data = f.read()
        f.close()
        match_parser = MatchStatisticParser(2029125, f_data)
        teams_stat = match_parser.get_teams_stat()
        self.assertDictEqual(teams_stat, __teams_stat)

    def test_match_statistic_parser_passing_stat(self):
        """
        Test is parser return passing stat data
        """
        __passing = {
            'home_team': {
                'player_id': 1948407,
                'player_name': 'Yevgen Fedorov',
                'comp': 12,
                'att': 25,
                'pct': 48.0,
                'yds': 232,
                'yds_a': 9.3,
                'lng': 53,
            },
            'away_team': {
                'player_id': 2231927,
                'player_name': 'Sławomir Damek',
                'comp': 1,
                'att': 13,
                'pct': 7.7,
                'yds': 8,
                'yds_a': 0.6,
                'lng': 8,
            }
        }
        f = open('test_match_statistic.txt', encoding="utf8")
        f_data = f.read()
        f.close()
        match_parser = MatchStatisticParser(2029125, f_data)
        passing_stat = match_parser.get_teams_passing()
        self.assertDictEqual(passing_stat, __passing)

    def test_match_statistic_parser_rushing_stat(self):
        """
        Test is parser return rushing stat data
        """
        __rushing = {
            'home_team': [
                {
                    'player_id': 2284778,
                    'player_name': 'Mateusz Rycombel',
                    'att': 20,
                    'yds': 246,
                    'yds_a': 12.3,
                    'lng': 38,
                },
                {
                    'player_id': 2327906,
                    'player_name': 'Szymon Gatner',
                    'att': 5,
                    'yds': 25,
                    'yds_a': 5,
                    'lng': 9,
                },
                {
                    'player_id': 2246980,
                    'player_name': 'Wiktor Witaszek',
                    'att': 8,
                    'yds': 52,
                    'yds_a': 6.5,
                    'lng': 13,
                },
            ],
            'away_team': [
                {
                    'player_id': 2231925,
                    'player_name': 'Radosław Hajok',
                    'att': 32,
                    'yds': -14,
                    'yds_a': -0.4,
                    'lng': 8,
                },
                {
                    'player_id': 2231921,
                    'player_name': 'Anatol Stiller',
                    'att': 5,
                    'yds': 52,
                    'yds_a': 10.4,
                    'lng': 25,
                },
            ]
        }
        f = open('test_match_statistic.txt', encoding="utf8")
        f_data = f.read()
        f.close()
        match_parser = MatchStatisticParser(2029125, f_data)
        rushing_stat = match_parser.get_teams_rushing()
        self.assertDictEqual(rushing_stat, __rushing)

    def test_match_statistic_parser_receiving_stat(self):
        """
        Test is parser return receiving stat data
        """
        __receiving = {
            'home_team': [
                {
                    'player_id': 2241778,
                    'player_name': 'Aureliusz Kalandyk',
                    'rec': 2,
                    'yds': 48,
                    'avg': 24,
                    'lng': 28,
                },
                {
                    'player_id': 2232105,
                    'player_name': 'Zygmunt Imiołek',
                    'rec': 4,
                    'yds': 68,
                    'avg': 17,
                    'lng': 28,
                },
            ],
            'away_team': [
                {
                    'player_id': 2231921,
                    'player_name': 'Anatol Stiller',
                    'rec': 1,
                    'yds': 8,
                    'avg': 8,
                    'lng': 8,
                },
            ]
        }
        f = open('test_match_statistic.txt', encoding="utf8")
        f_data = f.read()
        f.close()
        match_parser = MatchStatisticParser(2029125, f_data)
        receiving_stat = match_parser.get_teams_receiving()
        self.assertDictEqual(receiving_stat, __receiving)

    def test_match_statistic_parser_kicking_stat(self):
        """
        Test is parser return kicking stat data
        """
        __kicking = {
            'home_team': {
                'player_id': 2119942,
                'player_name': 'Aleksy Głowicki',
                'fgm': 0,
                'fga': 1,
                'pct': 0,
                'lng': 0,
            },
            'away_team': None
        }
        f = open('test_match_statistic.txt', encoding="utf8")
        f_data = f.read()
        f.close()
        match_parser = MatchStatisticParser(2029125, f_data)
        kicking_stat = match_parser.get_teams_kicking()
        self.assertDictEqual(kicking_stat, __kicking)

    def test_match_statistic_parser_defense_stat(self):
        """
        Test is parser return defense stat data
        """
        __defense = {
            'home_team': [
                {
                    'player_id': 2113599,
                    'player_name': 'Dymitr Dziewanowski',
                    'tackles': 10,
                    'sacks': 1,
                    'interceptions': 0,
                    'fumbles': 3,
                },
                {
                    'player_id': 2100092,
                    'player_name': 'Jakub Skrzypkowski',
                    'tackles': 5,
                    'sacks': 0,
                    'interceptions': 2,
                    'fumbles': 0,
                },
            ],
            'away_team': [
                {
                    'player_id': 2231926,
                    'player_name': 'Grzegorz Kieda',
                    'tackles': 1,
                    'sacks': 2,
                    'interceptions': 3,
                    'fumbles': 4,
                },
            ]
        }
        f = open('test_match_statistic.txt', encoding="utf8")
        f_data = f.read()
        f.close()
        match_parser = MatchStatisticParser(2029125, f_data)
        defense_stat = match_parser.get_teams_defense()
        self.assertDictEqual(defense_stat, __defense)


if __name__ == '__main__':
    unittest.main()
