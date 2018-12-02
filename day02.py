"""Day 02 puzzle solutions"""

import sys
import day02_lib

with open(sys.argv[1], 'r') as inputFile:
    STRINGS = inputFile.readlines()

CHECKSUM = day02_lib.checksum(STRINGS)
print("Day02 --- Part One --- result is: {0}".format(CHECKSUM))
COMMON_LETTERS = day02_lib.getCommonLetters(STRINGS)
print("Day02 --- Part Two --- result is: {0}".format(COMMON_LETTERS))
