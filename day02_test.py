"""Day 01 unit tests"""

import unittest
from day02_lib import countLetters
from day02_lib import checksum

class Day02TestCase(unittest.TestCase):
    """Tests for `day02.py`"""

    def test_countLetters_abcdef_should_return_0_0(self):
        """Test for """
        twice, threeTimes = countLetters("abcdef")
        self.assertEqual(twice, 0)
        self.assertEqual(threeTimes, 0)

    def test_countLetters_bababc_should_return_1_1(self):
        """Test for countLetters"""
        twice, threeTimes = countLetters("bababc")
        self.assertEqual(twice, 1)
        self.assertEqual(threeTimes, 1)

    def test_countLetters_abbcde_should_return_1_1(self):
        """Test for countLetters """
        twice, threeTimes = countLetters("abbcde")
        self.assertEqual(twice, 1)
        self.assertEqual(threeTimes, 0)

    def test_countLetters_abcccd_should_return_1_1(self):
        """Test for countLetters """
        twice, threeTimes = countLetters("abcccd")
        self.assertEqual(twice, 0)
        self.assertEqual(threeTimes, 1)

    def test_countLetters_aabcdd_should_return_1_1(self):
        """Test for countLetters """
        twice, threeTimes = countLetters("aabcdd")
        self.assertEqual(twice, 2)
        self.assertEqual(threeTimes, 0)

    def test_countLetters_abcdee_should_return_1_1(self):
        """Test for countLetters """
        twice, threeTimes = countLetters("abcdee")
        self.assertEqual(twice, 1)
        self.assertEqual(threeTimes, 0)

    def test_countLetters_ababab_should_return_1_1(self):
        """Test for countLetters """
        twice, threeTimes = countLetters("ababab")
        self.assertEqual(twice, 0)
        self.assertEqual(threeTimes, 2)

    def test_checksum_should_return_12(self):
        """Test for checksun """
        inputValues = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']
        checksumResult = checksum(inputValues)
        self.assertEqual(checksumResult, 12)

if __name__ == '__main__':
    unittest.main()
