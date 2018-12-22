"""Day 09 unit tests"""

import unittest
from day09_lib import playMarble

class day10TestCase(unittest.TestCase):
    """Tests for `day09.py`"""

    def test_playMarble_with_9_players_25_marbles_should_return_a_high_score_of_32(self):
        """Test for playMarble"""
        highScore = playMarble(9, 25)
        self.assertEqual(32, highScore)

    def test_playMarble_with_10_players_1618_marbles_should_return_a_high_score_of_8317(self):
        """Test for playMarble"""
        highScore = playMarble(10, 1618)
        self.assertEqual(8317, highScore)

    def test_playMarble_with_13_players_7999_marbles_should_return_a_high_score_of_146373(self):
        """Test for playMarble"""
        highScore = playMarble(13, 7999)
        self.assertEqual(146373, highScore)

    def test_playMarble_with_17_players_1104_marbles_should_return_a_high_score_of_2764(self):
        """Test for playMarble"""
        highScore = playMarble(17, 1104)
        self.assertEqual(2764, highScore)

    def test_playMarble_with_21_players_6111_marbles_should_return_a_high_score_of_54718(self):
        """Test for playMarble"""
        highScore = playMarble(21, 6111)
        self.assertEqual(54718, highScore)

    def test_playMarble_with_30_players_5807_marbles_should_return_a_high_score_of_37305(self):
        """Test for playMarble"""
        highScore = playMarble(30, 5807)
        self.assertEqual(37305, highScore)

if __name__ == '__main__':
    unittest.main()
