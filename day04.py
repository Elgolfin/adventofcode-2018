"""Day 04 puzzle solutions"""

import sys
import day04_lib

with open(sys.argv[1], 'r') as inputFile:
    ENTRIES = inputFile.readlines()

RES1, RES2 = day04_lib.getGuardResult(ENTRIES)
print("Day04 --- Part One --- result is: {0}".format(RES1))
print("Day04 --- Part Two --- result is: {0}".format(RES2))
