"""Day 01 puzzle solutions"""

import sys
import day01_lib

with open(sys.argv[1], 'r') as inputFile:
    FREQUENCIES = inputFile.readlines()

RESULTING_FREQUENCY = day01_lib.calibrate_frequency(FREQUENCIES)
print("Day01 --- Part One --- result is: {0}".format(RESULTING_FREQUENCY))
RESULTING_FREQUENCY = day01_lib.get_first_frequency_reached_twice(FREQUENCIES)
print("Day01 --- Part Two --- result is: {0}".format(RESULTING_FREQUENCY))
