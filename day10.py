"""Day 10 puzzle solutions"""

import sys
import day10_lib

with open(sys.argv[1], 'r') as inputFile:
    INPUT = inputFile.readlines()


print("Day10 --- Part One --- result is: ")
DURATION = day10_lib.getMessage(INPUT)
print("Day10 --- Part Two --- result is: {0}".format(DURATION))