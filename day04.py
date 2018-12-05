"""Day 04 puzzle solutions"""

import sys
import day04_lib

with open(sys.argv[1], 'r') as inputFile:
    ENTRIES = inputFile.readlines()
    
print("Day04 --- Part One --- result is: {0}".format(day04_lib.getGuardResult(ENTRIES)))
# print("Day03 --- Part Two --- result is: {0}".format(NOT_OVERLAPPING_CLAIM_ID))
