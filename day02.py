"""Day 02 puzzle solutions"""

import sys
import day02_lib

with open(sys.argv[1], 'r') as inputFile:
    STRINGS = inputFile.readlines()

CHECKSUM = day02_lib.checksum(STRINGS)
print("Day02 --- Part One --- result is: {0}".format(CHECKSUM))
# RESULTING_FREQUENCY = day01_lib.get_first_frequency_reached_twice(FREQUENCIES)
# print("Day01 --- Part Two --- result is: {0}".format(RESULTING_FREQUENCY))
