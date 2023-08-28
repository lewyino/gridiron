import sys
import unittest

sys.path.append('../')

from site_parser.GridIronParser import *


@unittest.skip('old')
class TestParser(unittest.TestCase):
    """
    Test functions from Parser class
    """

    @classmethod
    def setUpClass(cls):
        cls.parser = GridIronParser()

    def test_getPlayersList_return_list(self):
        """
        Test is getPlayerList return list
        """
        f = open('test_Parser_players_list.txt', encoding="utf8")
        f_data = f.read()
        f.close()
        res = self.parser.get_players_list(f_data)
        self.assertIsInstance(res, list)

    def test_getPlayersList_return_list_with_all_elements(self):
        """
        Test is getPlayerList return list with correct number of elements
        """
        f = open('test_Parser_players_list.txt', encoding="utf8")
        f_data = f.read()
        f.close()
        res = self.parser.get_players_list(f_data)
        self.assertEqual(len(res), 6)

    def test_getPlayersList_returned_list_with_Player(self):
        """
        Test is getPlayerList returned list with Player class element
        """
        f = open('test_Parser_players_list.txt', encoding="utf8")
        f_data = f.read()
        f.close()
        res = self.parser.get_players_list(f_data)
        self.assertIsInstance(res[0], Player)

    def test_updatePlayerData(self):
        """
        Test is updatePlayerData add skills player data to Player class
        """
        player = Player(1, 'player', 'QB', 22, 4, 100, '1000', 'health')
        f = open('test_Parser_player_data.txt', encoding="utf8")
        f_data = f.read()
        f.close()
        player = self.parser.update_player_data(player, f_data)
        self.assertEqual(player.positioning, 1)
        self.assertEqual(player.catching, 6)
        self.assertEqual(player.agility, 12)
        self.assertEqual(player.footwork, 14)
        self.assertEqual(player.weeks_at_club, 1)
        self.assertEqual(player.trained, 'Kondycja / Siła')


if __name__ == '__main__':
    unittest.main()
