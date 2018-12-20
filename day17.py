"""Day 17 puzzle solutions"""

import sys
import day17_lib

with open(sys.argv[1], 'r') as inputFile:
    INPUT = inputFile.readlines()

GROUND = day17_lib.initializeGround(INPUT)
print("Day17 --- Part One --- result is: {0}".format(day17_lib.countWaterTiles(GROUND, (500, 0))))
# print("Day12 --- Part Two --- result is: {0}".format(RESULT))