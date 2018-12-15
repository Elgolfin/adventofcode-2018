"""Day 11 unit tests"""

import unittest
from day11_lib import getPowerLevel
from day11_lib import getLargestTotalPowerArea
from day11_lib import getLargestTotalPowerArea2

class day11TestCase(unittest.TestCase):
    """Tests for `day11.py`"""

    def test_getPowerLevel_Of_x3_y5_should_return_4(self):
        """Test for getPowerLevel"""
        input = 8
        powerLevel = getPowerLevel(3, 5, input)
        self.assertEqual(4, powerLevel)

    def test_getPowerLevel_Of_x122_y79_should_return_minus_5(self):
        """Test for getPowerLevel"""
        input = 57
        powerLevel = getPowerLevel(122, 79, input)
        self.assertEqual(-5, powerLevel)

    def test_getPowerLevel_Of_x217_y196_should_return_0(self):
        """Test for getPowerLevel"""
        input = 39
        powerLevel = getPowerLevel(217, 196, input)
        self.assertEqual(0, powerLevel)

    def test_getPowerLevel_Of_x101_y153_should_return_4(self):
        """Test for getPowerLevel"""
        input = 71
        powerLevel = getPowerLevel(101,153, input)
        self.assertEqual(4, powerLevel)

    def test_getLargestTotalPowerArea_should_return_x33_y45(self):
        """Test for getLargestTotalPowerArea"""
        input = 18
        coordinates, _ = getLargestTotalPowerArea(input)
        self.assertEqual((33, 45), coordinates)

    def test_getLargestTotalPowerArea2_should_return_x90_y269_16(self):
        """Test for getLargestTotalPowerArea2"""
        input = 18
        coordinates = getLargestTotalPowerArea2(input)
        self.assertEqual((90, 269, 16), coordinates)

    # def test_getLargestTotalPowerArea2_should_return_x232_y251_12(self):
    #     """Test for getLargestTotalPowerArea2"""
    #     input = 42
    #     coordinates = getLargestTotalPowerArea2(input)
    #     self.assertEqual((232, 251, 12), coordinates)


if __name__ == '__main__':
    unittest.main()
