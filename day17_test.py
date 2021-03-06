"""Day 17 unit tests"""

import unittest
from day17_lib import countWaterTiles
from day17_lib import initializeGround

class day17TestCase(unittest.TestCase):
    """Tests for `day17.py`"""

    input0 = [
        "x=490, y=0..4",
        "x=504, y=0..4",
        "y=10, x=490..494",
    ]

    input1 = [
        "x=495, y=2..7",
        "y=7, x=495..501",
        "x=501, y=3..7",
        "x=498, y=2..4",
        "x=506, y=1..2",
        "x=498, y=10..13",
        "x=504, y=10..13",
        "y=13, x=498..504",
    ]

    input2 = [
        "x=495, y=2..5",
        "y=7, x=495..501",
        "x=501, y=3..7",
        "x=498, y=2..4",
        "x=506, y=1..2",
        "x=498, y=10..13",
        "x=504, y=10..13",
        "y=13, x=498..504",
    ]

    input3 = [
        "x=495, y=2..7",
        "y=7, x=495..501",
        "x=501, y=3..5",
        "x=498, y=2..4",
        "x=506, y=1..2",
        "x=498, y=10..13",
        "x=504, y=10..13",
        "y=13, x=498..504",
    ]

    input4 = [
        "x=495, y=2..5",
        "y=7, x=495..501",
        "x=501, y=3..5",
        "x=498, y=2..4",
        "x=506, y=1..2",
        "x=498, y=10..13",
        "x=504, y=10..13",
        "y=13, x=498..504",
    ]

    input5 = [
        "x=498, y=3..5",
        "x=504, y=1..5",
        "y=5, x=498..504",
    ]

    input6 = [
        "x=492, y=3..10",
        "x=508, y=3..10",
        "y=10, x=492..508",
        "x=498, y=5..7",
        "x=502, y=5..7",
        "y=8, x=498..502",
    ]

    input7 = [
        "x=492, y=3..10",
        "x=508, y=3..10",
        "y=10, x=492..508",
        "x=499, y=5..7",
        "x=501, y=5..7",
        "y=8, x=499..501",
    ]

    input8 = [
        "x=490, y=5..14",
        "x=510, y=5..14",
        "y=14, x=490..510",
        "x=502, y=7..10",
        "x=504, y=7..10",
        "y=10, x=502..504",
    ]

    def test_initializeGround(self):
        """Test for initializeGround"""
        
        expectedResult = {(494, 0): '.', (495, 0): '.', (496, 0): '.', (497, 0): '.', (498, 0): '.', (499, 0): '.', (500, 0): '+', (501, 0): '.', (502, 0): '.', (503, 0): '.', (504, 0): '.', (505, 0): '.', (506, 0): '.', (507, 0): '.', (494, 1): '.', (495, 1): '.', (496, 1): '.', (497, 1): '.', (498, 1): '.', (499, 1): '.', (500, 1): '.', (501, 1): '.', (502, 1): '.', (503, 1): '.', (504, 1): '.', (505, 1): '.', (506, 1): '#', (507, 1): '.', (494, 2): '.', (495, 2): '#', (496, 2): '.', (497, 2): '.', (498, 2): '#', (499, 2): '.', (500, 2): '.', (501, 2): '.', (502, 2): '.', (503, 2): '.', (504, 2): '.', (505, 2): '.', (506, 2): '#', (507, 2): '.', (494, 3): '.', (495, 3): '#', (496, 3): '.', (497, 3): '.', (498, 3): '#', (499, 3): '.', (500, 3): '.', (501, 3): '#', (502, 3): '.', (503, 3): '.', (504, 3): '.', (505, 3): '.', (506, 3): '.', (507, 3): '.', (494, 4): '.', (495, 4): '#', (496, 4): '.', (497, 4): '.', (498, 4): '#', (499, 4): '.', (500, 4): '.', (501, 4): '#', (502, 4): '.', (503, 4): '.', (504, 4): '.', (505, 4): '.', (506, 4): '.', (507, 4): '.', (494, 5): '.', (495, 5): '#', (496, 5): '.', (497, 5): '.', (498, 5): '.', (499, 5): '.', (500, 5): '.', (501, 5): '#', (502, 5): '.', (503, 5): '.', (504, 5): '.', (505, 5): '.', (506, 5): '.', (507, 5): '.', (494, 6): '.', (495, 6): '#', (496, 6): '.', (497, 6): '.', (498, 6): '.', (499, 6): '.', (500, 6): '.', (501, 6): '#', (502, 6): '.', (503, 6): '.', (504, 6): '.', (505, 6): '.', (506, 6): '.', (507, 6): '.', (494, 7): '.', (495, 7): '#', (496, 7): '#', (497, 7): '#', (498, 7): '#', (499, 7): '#', (500, 7): '#', (501, 7): '#', (502, 7): '.', (503, 7): '.', (504, 7): '.', (505, 7): '.', (506, 7): '.', (507, 7): '.', (494, 8): '.', (495, 8): '.', (496, 8): '.', (497, 8): '.', (498, 8): '.', (499, 8): '.', (500, 8): '.', (501, 8): '.', (502, 8): '.', (503, 8): '.', (504, 8): '.', (505, 8): '.', (506, 8): '.', (507, 8): '.', (494, 9): '.', (495, 9): '.', (496, 9): '.', (497, 9): '.', (498, 9): '.', (499, 9): '.', (500, 9): '.', (501, 9): '.', (502, 9): '.', (503, 9): '.', (504, 9): '.', (505, 9): '.', (506, 9): '.', (507, 9): '.', (494, 10): '.', (495, 10): '.', (496, 10): '.', (497, 10): '.', (498, 10): '#', (499, 10): '.', (500, 10): '.', (501, 10): '.', (502, 10): '.', (503, 10): '.', (504, 10): '#', (505, 10): '.', (506, 10): '.', (507, 10): '.', (494, 11): '.', (495, 11): '.', (496, 11): '.', (497, 11): '.', (498, 11): '#', (499, 11): '.', (500, 11): '.', (501, 11): '.', (502, 11): '.', (503, 11): '.', (504, 11): '#', (505, 11): '.', (506, 11): '.', (507, 11): '.', (494, 12): '.', (495, 12): '.', (496, 12): '.', (497, 12): '.', (498, 12): '#', (499, 12): '.', (500, 12): '.', (501, 12): '.', (502, 12): '.', (503, 12): '.', (504, 12): '#', (505, 12): '.', (506, 12): '.', (507, 12): '.', (494, 13): '.', (495, 13): '.', (496, 13): '.', (497, 13): '.', (498, 13): '#', (499, 13): '#', (500, 13): '#', (501, 13): '#', (502, 13): '#', (503, 13): '#', (504, 13): '#', (505, 13): '.', (506, 13): '.', (507, 13): '.', (-1, -1): (1, 13)}
        result = initializeGround(self.input1)
        self.assertEqual(expectedResult, result)

    def test_countWaterTiles_should_return_10(self):
        """Test for countWaterTiles"""
        ground = initializeGround(self.input0)
        result, _ = countWaterTiles(ground, (500, 0))
        self.assertEqual(10, result)

    def test_countWaterTiles_should_return_57_and_29(self):
        """Test for countWaterTiles"""
        ground = initializeGround(self.input1)
        result1, result2 = countWaterTiles(ground, (500, 0))
        self.assertEqual(57, result1)
        self.assertEqual(29, result2)

    def test_countWaterTiles_should_return_19(self):
        """Test for countWaterTiles"""
        ground = initializeGround(self.input2)
        result, _ = countWaterTiles(ground, (500, 0))
        self.assertEqual(19, result)

    def test_countWaterTiles_should_return_46(self):
        """Test for countWaterTiles"""
        ground = initializeGround(self.input3)
        result, _ = countWaterTiles(ground, (500, 0))
        self.assertEqual(46, result)

    def test_countWaterTiles_should_return_55(self):
        """Test for countWaterTiles"""
        ground = initializeGround(self.input4)
        result, _ = countWaterTiles(ground, (500, 0))
        self.assertEqual(55, result)

    def test_countWaterTiles_should_return_21(self):
        """Test for countWaterTiles"""
        ground = initializeGround(self.input5)
        result, _ = countWaterTiles(ground, (500, 0))
        self.assertEqual(21, result)

    def test_countWaterTiles_should_return_110(self):
        """Test for countWaterTiles"""
        ground = initializeGround(self.input6)
        result, _ = countWaterTiles(ground, (500, 0))
        self.assertEqual(110, result)

    def test_countWaterTiles_should_return_112(self):
        """Test for countWaterTiles"""
        ground = initializeGround(self.input7)
        result, _ = countWaterTiles(ground, (500, 0))
        self.assertEqual(112, result)

    def test_countWaterTiles_should_return_182(self):
        """Test for countWaterTiles"""
        ground = initializeGround(self.input8)
        result, _ = countWaterTiles(ground, (500, 0))
        self.assertEqual(182, result)

if __name__ == '__main__':
    unittest.main()
