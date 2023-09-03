import sys
import unittest

sys.path.append('../')

from site_parser.MatchParser import *


@unittest.skip('old')
class TestMatchParser(unittest.TestCase):
    """
    Test functions from MachParser class
    """

    @classmethod
    def setUpClass(cls):
        f = open('test_match_log.txt', encoding="utf8")
        f_data = f.read()
        f.close()
        cls.mach_parser = MatchParser(f_data)

    def test_get_audience(self):
        """
        Test is get_audience return right value
        """
        res = self.mach_parser.get_audience()
        self.assertEqual(res, 9263)

    def test_get_team_evens(self):
        """
        Test is get_team_evens return right value
        """
        res = self.mach_parser.get_team_evens('LEWY Team')
        self.assertEqual(res, 'aaa')


if __name__ == '__main__':
    unittest.main()
