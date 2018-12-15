"""Day 11 puzzle solutions"""

import sys
import day11_lib

with open(sys.argv[1], 'r') as inputFile:
    INPUT = int(inputFile.read())

RESULT, _ = day11_lib.getLargestTotalPowerArea(INPUT)
print("Day11 --- Part One --- result is: {0}".format(RESULT))
print("Day11 --- Part Two --- result is: {0}".format(day11_lib.getLargestTotalPowerArea2(INPUT)))