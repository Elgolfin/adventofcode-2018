"""Day 03 unit tests"""

import unittest
from day03_lib import fillSquare
from day03_lib import parseClaim
from day03_lib import countOverlappingInches

class Day03TestCase(unittest.TestCase):
    """Tests for `day03.py`"""

    def test_parseClaim_1(self):
        """Test for parseClaim #1 @ 3,2: 5x4"""
        result = parseClaim("#1 @ 3,2: 5x4")
        self.assertEqual(1, result["id"])
        self.assertEqual(3, result["left"])
        self.assertEqual(2, result["top"])
        self.assertEqual(5, result["width"])
        self.assertEqual(4, result["height"])

    def test_fillSquare_1(self):
        """Test for print square"""
        result = fillSquare(["#1 @ 3,2: 5x4"], 11, 9)
        expected = [['.','.','.','.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.','.','.','.'],['.','.','.',1,1,1,1,1,'.','.','.'],['.','.','.',1,1,1,1,1,'.','.','.'],['.','.','.',1,1,1,1,1,'.','.','.'],['.','.','.',1,1,1,1,1,'.','.','.'],['.','.','.','.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.','.','.','.']]
        self.assertEqual(expected, result)

    def test_fillSquare_2(self):
        """Test for print square"""
        result = fillSquare(["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"], 8, 8)
        expected = [['.','.','.','.','.','.','.','.'],['.','.','.',2,2,2,2,'.'],['.','.','.',2,2,2,2,'.'],['.',1,1,'X','X',2,2,'.'],['.',1,1,'X','X',2,2,'.'],['.',1,1,1,1,3,3,'.'],['.',1,1,1,1,3,3,'.'],['.','.','.','.','.','.','.','.']]
        self.assertEqual(expected, result)

    def test_countOverlappingInches_should_return_4(self):
        """Test for countOverlappingInches"""
        matrix = fillSquare(["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"], 8, 8)
        result = countOverlappingInches(matrix)
        self.assertEqual(4, result);

if __name__ == '__main__':
    unittest.main()
