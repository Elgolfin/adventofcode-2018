"""Day 06 unit tests"""

import unittest
from day06_lib import getManhattanDist
from day06_lib import initializeGrid
from day06_lib import getClosestManhattanDist
from day06_lib import determineClosestCoordinate
from day06_lib import getLargestArea
from day06_lib import getSizeOfAllLocationsWithinLimit
from day06_lib import getSumAllManhattanDist

class day06TestCase(unittest.TestCase):
    """Tests for `day06.py`"""

    def test_getManhattanDist_should_return_4(self):
        """Test for getManhattanDist"""
        result = getManhattanDist((1,1),(1,6))
        self.assertEqual(5, result)
    
    def test_initializeGrid(self):
        """Test for initializeGridt"""
        expectedCoordinates = {'a': (1, 1), 'b': (1, 6), 'c': (8, 3), 'd': (3, 4), 'e': (5, 5), 'f': (8, 9)}
        expectedGrid = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                        ['.', 'a', '.', '.', '.', '.', 'b', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', 'd', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', 'e', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', 'c', '.', '.', '.', '.', '.', 'f']]
        coordinates, grid = initializeGrid(["1, 1", "1, 6", "8, 3", "3, 4", "5, 5", "8, 9"])
        self.assertEqual(expectedCoordinates, coordinates)
        self.assertEqual(expectedGrid, grid)

    def test_closestPoint_should_return_a(self):
        """Test for getClosestManhattanDist"""
        coordinates, _ = initializeGrid(["1, 1", "1, 6", "8, 3", "3, 4", "5, 5", "8, 9"])
        result = getClosestManhattanDist((0,0), coordinates)
        self.assertEqual('a', result)

    def test_closestPoint_should_return_dot(self):
        """Test for getClosestManhattanDist"""
        coordinates, _ = initializeGrid(["1, 1", "1, 6", "8, 3", "3, 4", "5, 5", "8, 9"])
        result = getClosestManhattanDist((5,0), coordinates)
        self.assertEqual('.', result)

    def test_getSumAllManhattanDist_should_return_30(self):
        """Test for getClosestManhattanDist"""
        coordinates, _ = initializeGrid(["1, 1", "1, 6", "8, 3", "3, 4", "5, 5", "8, 9"])
        result = getSumAllManhattanDist((4,3), coordinates)
        self.assertEqual(30, result)
    
    def test_determineClosestCoordinate(self):
        """Test for determineClosestCoordinate"""
        expectedGrid = [['a', 'a', 'a', 'a', '.', 'b', 'b', 'b', 'b', 'b'],
                        ['a', 'a', 'a', 'a', '.', 'b', 'b', 'b', 'b', 'b'],
                        ['a', 'a', 'a', 'd', 'd', '.', 'b', 'b', 'b', 'b'],
                        ['a', 'a', 'd', 'd', 'd', 'd', '.', '.', '.', '.'],
                        ['a', 'a', 'd', 'd', 'd', 'e', 'e', 'e', 'e', 'f'],
                        ['.', '.', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'f'],
                        ['c', 'c', 'c', 'c', 'e', 'e', 'e', 'e', 'f', 'f'],
                        ['c', 'c', 'c', 'c', 'c', 'e', 'e', 'f', 'f', 'f'],
                        ['c', 'c', 'c', 'c', 'c', 'c', '.', 'f', 'f', 'f'],]
        coordinates, grid = initializeGrid(["1, 1", "1, 6", "8, 3", "3, 4", "5, 5", "8, 9"])
        grid = determineClosestCoordinate(coordinates, grid)
        self.assertEqual(expectedGrid, grid)

    def test_getLargestArea_should_return_17(self):
        """Test for getLargestArea"""
        coordinates, grid = initializeGrid(["1, 1", "1, 6", "8, 3", "3, 4", "5, 5", "8, 9"])
        grid = determineClosestCoordinate(coordinates, grid)
        result = getLargestArea(coordinates, grid)
        self.assertEqual(17, result)

    def test_getSizeOfAllLocationsWithinLimit_should_return_16(self):
        """Test for getSizeOfAllLocationsWithinLimit"""
        coordinates, grid = initializeGrid(["1, 1", "1, 6", "8, 3", "3, 4", "5, 5", "8, 9"])
        result = getSizeOfAllLocationsWithinLimit(coordinates, grid, 32)
        self.assertEqual(16, result)

if __name__ == '__main__':
    unittest.main()
