"""Day 07 unit tests"""

import unittest
from day07_lib import findStartingSteps
from day07_lib import completeSteps

class day07TestCase(unittest.TestCase):
    """Tests for `day07.py`"""

    def test_findStartingSteps_should_return_C(self):
        """Test for findStartingSteps"""
        input = ["Step C must be finished before step A can begin.",
                 "Step C must be finished before step F can begin.",
                 "Step A must be finished before step B can begin.",
                 "Step A must be finished before step D can begin.",
                 "Step B must be finished before step E can begin.",
                 "Step D must be finished before step E can begin.",
                 "Step F must be finished before step E can begin.",
                ]
        startingSteps, _ = findStartingSteps(input)
        self.assertEqual(['C'], startingSteps)

    def test_completeSteps_should_return_CABDFE(self):
        """Test for completeSteps (result only, 1 worker)"""
        input = ["Step C must be finished before step A can begin.",
                 "Step C must be finished before step F can begin.",
                 "Step A must be finished before step B can begin.",
                 "Step A must be finished before step D can begin.",
                 "Step B must be finished before step E can begin.",
                 "Step D must be finished before step E can begin.",
                 "Step F must be finished before step E can begin.",
                ]
        startingSteps, steps = findStartingSteps(input)
        result, _ = completeSteps(startingSteps, steps, 1, 0)
        self.assertEqual("CABDFE", result)

    def test_completeSteps_should_return_15(self):
        """Test for completeSteps (duration only, 2 workers)"""
        input = ["Step C must be finished before step A can begin.",
                 "Step C must be finished before step F can begin.",
                 "Step A must be finished before step B can begin.",
                 "Step A must be finished before step D can begin.",
                 "Step B must be finished before step E can begin.",
                 "Step D must be finished before step E can begin.",
                 "Step F must be finished before step E can begin.",
                ]
        startingSteps, steps = findStartingSteps(input)
        _, duration = completeSteps(startingSteps, steps, 2, 0)
        self.assertEqual(15, duration)

if __name__ == '__main__':
    unittest.main()
