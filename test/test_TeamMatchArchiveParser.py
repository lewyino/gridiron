import sys
import unittest

sys.path.append('..')

from site_parser.TeamMatchArchiveParser import TeamMatchArchiveParser

from site_parser.MatchStatisticHTMLParser import *
from site_parser.MatchTeamsParser import *
from site_parser.MatchStatisticParser import MatchStatisticParser


@unittest.skip('old')
class TestMatchParser(unittest.TestCase):

    def test_match_team_archive_seasons(self):
        """
        Test is parser return list of archive seasons
        """
        __seasons = [('{i}'.format(i=i), 'Season {i}'.format(i=i)) for i in range(1, 40)]
        f = open('match_archive.txt', encoding="utf8")
        f_data = f.read()
        f.close()
        match_parser = TeamMatchArchiveParser(f_data)
        seasons = match_parser.get_seasons()
        self.assertListEqual(seasons, __seasons)

    def test_match_team_matches_id(self):
        """
        Test is parser return list of match id
        """
        __matches_id = [
            ('3128936', 'League', 'Red Dragons - Cuiavia Miners'),
            ('3185491', 'Cup', 'Cuiavia Miners - Banska Bystrica Daemons'),
            ('3128928', 'League', 'Łazarz Raiders - Cuiavia Miners'),
            ('3190269', 'Friendly', 'Cuiavia Miners - nonameyet2'),
            ('3128926', 'League', 'Cuiavia Miners - Cassovia Steelers'),
            ('3128922', 'League', 'nonameyet2 - Cuiavia Miners'),
            ('3187597', 'Friendly', 'Cuiavia Miners - nonameyet2'),
            ('3128916', 'League', 'Cuiavia Miners - Bielsko-Biała Highlanders'),
            ('3186369', 'Friendly', 'Cuiavia Miners - nonameyet2'),
            ('3128912', 'League', 'Svätý Jur Snakers - Cuiavia Miners'),
            ('3112795', 'Friendly', 'Cuiavia Miners - AFC Zurich State Spartans'),
            ('3128905', 'League', 'Cuiavia Miners - Libouchec Wolverines'),
        ]
        f = open('match_archive.txt', encoding="utf8")
        f_data = f.read()
        f.close()
        match_parser = TeamMatchArchiveParser(f_data)
        matches_id = match_parser.get_team_matches()
        self.assertListEqual(matches_id, __matches_id)


if __name__ == '__main__':
    unittest.main()
