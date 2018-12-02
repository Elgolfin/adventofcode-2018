"""Day 01 unit tests"""

import unittest
from day01_lib import calibrate_frequency
from day01_lib import get_first_frequency_reached_twice

class Day01TestCase(unittest.TestCase):
    """Tests for `day01.py`"""

    def test_calibrate_frequency_1(self):
        """Test for +1 +1 +1"""
        inputValues = ['+1', '+1', '+1']
        result = calibrate_frequency(inputValues)
        self.assertEqual(result, 3)

    def test_calibrate_frequency_2(self):
        """Test for +1 +1 -2"""
        inputValues = ['+1', '+1', '-2']
        result = calibrate_frequency(inputValues)
        self.assertEqual(result, 0)

    def test_calibrate_frequency_3(self):
        """Test for -1 -2 -3"""
        inputValues = ['-1', '-2', '-3']
        result = calibrate_frequency(inputValues)
        self.assertEqual(result, -6)

    def test_get_first_frequency_reached_twice_1(self):
        """Test for +1 -2 +3 +1"""
        inputValues = ['+1', '-2', '+3', '+1']
        result = get_first_frequency_reached_twice(inputValues)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
