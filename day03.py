"""Day 03 puzzle solutions"""

import sys
import day03_lib

with open(sys.argv[1], 'r') as inputFile:
    CLAIMS = inputFile.readlines()

OVERLAPPING_INCHES = day03_lib.countOverlappingInches(day03_lib.fillSquare(CLAIMS))
print("Day03 --- Part One --- result is: {0}".format(OVERLAPPING_INCHES))
# COMMON_LETTERS = day02_lib.getCommonLetters(STRINGS)
# print("Day02 --- Part Two --- result is: {0}".format(COMMON_LETTERS))
