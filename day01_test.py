"""Day 01 unit tests"""

import unittest
from day01_lib import calibrate_frequency

class Day01TestCase(unittest.TestCase):
    """Tests for `day01.py`"""

    def test_1(self):
        """Test for +1 +1 +1"""
        inputValues = ['+1', '+1', '+1']
        result = calibrate_frequency(inputValues)
        self.assertEqual(result, 3)

    def test_2(self):
        """Test for +1 +1 -2"""
        inputValues = ['+1', '+1', '-2']
        result = calibrate_frequency(inputValues)
        self.assertEqual(result, 0)

    def test_3(self):
        """Test for -1 -2 -3"""
        inputValues = ['-1', '-2', '-3']
        result = calibrate_frequency(inputValues)
        self.assertEqual(result, -6)

if __name__ == '__main__':
    unittest.main()
