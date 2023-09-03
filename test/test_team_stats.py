import sys
import unittest

sys.path.append('..')

from stats.team_stats import get_team_match_ids_stats_last, get_team_match_ids_stats_league, \
    get_team_match_ids_stats_indexes


@unittest.skip('old')
class TestMatchParser(unittest.TestCase):

    def test_get_team_match_ids_stats_last(self):
        __matches = (
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
        )
        __matches_last_6 = (
            3128936,
            3185491,
            3128928,
            3190269,
            3128926,
            3128922,
        )

        matches = get_team_match_ids_stats_last(__matches, 'last6')
        self.assertTupleEqual(matches, __matches_last_6)

    def test_get_team_match_ids_stats_league(self):
        __matches = (
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
        )
        __matches_last_6 = (
            3128936,
            3128928,
            3128926,
            3128922,
            3128916,
            3128912,
        )

        matches = get_team_match_ids_stats_league(__matches, 'league6')
        self.assertTupleEqual(matches, __matches_last_6)

    def test_get_team_match_ids_stats_indexes(self):
        __matches = (
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
        )
        __matches_selected = (
            3128936,  # 1
            3185491,  # 2
            3190269,  # 4
            3187597,  # 7
            3128916,  # 8
            3128905,  # 12
        )

        matches = get_team_match_ids_stats_indexes(__matches, '1,2,4,7,8,12')
        self.assertTupleEqual(matches, __matches_selected)


if __name__ == '__main__':
    unittest.main()
