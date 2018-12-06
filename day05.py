"""Day 05 puzzle solutions"""

import sys
import day05_lib

with open(sys.argv[1], 'r') as inputFile:
    POLYMER = inputFile.read()

RESULT_POLYMER = day05_lib.scanPolymer(POLYMER)
RESULT_SHORTEST_POLYMER = day05_lib.scanPolymerV2(POLYMER)
print("Day05 --- Part One --- result is: {0}".format(RESULT_POLYMER))
print("Day05 --- Part Two --- result is: {0}".format(RESULT_SHORTEST_POLYMER))
