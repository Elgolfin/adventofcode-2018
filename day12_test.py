"""Day 12 unit tests"""

import unittest
from day12_lib import initializeGarden
from day12_lib import growNextGeneration
from day12_lib import sumPotNumbersAfterNGenerations

class day12TestCase(unittest.TestCase):
    """Tests for `day12.py`"""

    def test_initializeGarden_returns_good_values(self):
        """Test for initializeGarden"""
        input = [
            "initial state: #..#.#..##......###...###",
            "",
            "...## => #",
            "..#.. => #",
            ".#... => #",
            ".#.#. => #",
            ".#.## => #",
            ".##.. => #",
            ".#### => #",
            "#.#.# => #",
            "#.### => #",
            "##.#. => #",
            "##.## => #",
            "###.. => #",
            "###.# => #",
            "####. => #",
        ]
        initialState, spreadTable = initializeGarden(input)
        self.assertEqual("#..#.#..##......###...###", initialState)
        self.assertEqual(14, len(spreadTable))

    def test_growNextGeneration_returns_next_generation_1(self):
        """Test for growNextGeneration"""
        input = [
            "initial state: #..#.#..##......###...###",
            "",
            "...## => #",
            "..#.. => #",
            ".#... => #",
            ".#.#. => #",
            ".#.## => #",
            ".##.. => #",
            ".#### => #",
            "#.#.# => #",
            "#.### => #",
            "##.#. => #",
            "##.## => #",
            "###.. => #",
            "###.# => #",
            "####. => #",
        ]
        initialState, spreadTable = initializeGarden(input)
        newState, idx = growNextGeneration(initialState, spreadTable)
        self.assertEqual("#...#....#.....#..#..#..#", newState)
        self.assertEqual(0, idx)

    def test_growNextGeneration_returns_next_generation_2(self):
        """Test for growNextGeneration"""
        input = [
            "initial state: #...#....#.....#..#..#..#",
            "",
            "...## => #",
            "..#.. => #",
            ".#... => #",
            ".#.#. => #",
            ".#.## => #",
            ".##.. => #",
            ".#### => #",
            "#.#.# => #",
            "#.### => #",
            "##.#. => #",
            "##.## => #",
            "###.. => #",
            "###.# => #",
            "####. => #",
        ]
        initialState, spreadTable = initializeGarden(input)
        newState, idx = growNextGeneration(initialState, spreadTable)
        self.assertEqual("##..##...##....#..#..#..##", newState)
        self.assertEqual(0, idx)

    def test_growNextGeneration_returns_next_generation_3(self):
        """Test for growNextGeneration"""
        input = [
            "initial state: ##..##...##....#..#..#..##",
            "",
            "...## => #",
            "..#.. => #",
            ".#... => #",
            ".#.#. => #",
            ".#.## => #",
            ".##.. => #",
            ".#### => #",
            "#.#.# => #",
            "#.### => #",
            "##.#. => #",
            "##.## => #",
            "###.. => #",
            "###.# => #",
            "####. => #",
        ]
        initialState, spreadTable = initializeGarden(input)
        newState, idx = growNextGeneration(initialState, spreadTable)
        self.assertEqual("#.#...#..#.#....#..#..#...#", newState)
        self.assertEqual(1, idx)

    def test_sumPotNumbersAfterNGenerations_returns_325(self):
        """Test for sumPotNumbersAfterNGenerations"""
        input = [
            "initial state: #..#.#..##......###...###",
            "",
            "...## => #",
            "..#.. => #",
            ".#... => #",
            ".#.#. => #",
            ".#.## => #",
            ".##.. => #",
            ".#### => #",
            "#.#.# => #",
            "#.### => #",
            "##.#. => #",
            "##.## => #",
            "###.. => #",
            "###.# => #",
            "####. => #",
        ]
        initialState, spreadTable = initializeGarden(input)
        result = sumPotNumbersAfterNGenerations(initialState, spreadTable, 20)
        self.assertEqual(325, result)

if __name__ == '__main__':
    unittest.main()
