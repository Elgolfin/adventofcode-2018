"""Day 05 unit tests"""

import unittest
from day05_lib import scanPolymer
from day05_lib import scanPolymer2

class day05TestCase(unittest.TestCase):
    """Tests for `day04.py`"""

    def test_scanPolymer_should_return_dabCBAcaDA(self):
        """Test for scanPolymer"""
        polymer = "dabAcCaCBAcCcaDA"
        expectedResult = "dabCBAcaDA"
        result = scanPolymer(polymer)
        self.assertEqual(len(expectedResult), result)

    def test_scanPolymer2_should_return_dabCBAcaDA(self):
        """Test for scanPolymer2"""
        polymer = "dabAcCaCBAcCcaDA"
        expectedResult = "dabCBAcaDA"
        result = scanPolymer2(polymer)
        self.assertEqual(len(expectedResult), result)

if __name__ == '__main__':
    unittest.main()
