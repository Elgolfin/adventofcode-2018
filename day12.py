"""Day 12 puzzle solutions"""

import sys
import day12_lib

with open(sys.argv[1], 'r') as inputFile:
    INPUT = inputFile.readlines()

STATE, SPREAD_TABLE = day12_lib.initializeGarden(INPUT)
RESULT = day12_lib.sumPotNumbersAfterNGenerations(STATE, SPREAD_TABLE, 20)
print("Day12 --- Part One --- result is: {0}".format(RESULT))
RESULT = day12_lib.sumPotNumbersAfterNGenerations(STATE, SPREAD_TABLE, 50000000000)
print("Day12 --- Part Two --- result is: {0}".format(RESULT))