"""Day 03 puzzle solutions"""

import sys
import day03_lib

with open(sys.argv[1], 'r') as inputFile:
    CLAIMS = inputFile.readlines()
CLAIMS_DICT, MATRIX = day03_lib.fillSquare(CLAIMS)
OVERLAPPING_INCHES = day03_lib.countOverlappingInches(MATRIX)
NOT_OVERLAPPING_CLAIM_ID = day03_lib.lookForNotVerlappingClaim(CLAIMS_DICT, MATRIX)
print("Day03 --- Part One --- result is: {0}".format(OVERLAPPING_INCHES))
print("Day03 --- Part Two --- result is: {0}".format(NOT_OVERLAPPING_CLAIM_ID))
