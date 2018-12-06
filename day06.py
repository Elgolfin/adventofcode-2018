"""Day 06 puzzle solutions"""

import sys
import day06_lib

with open(sys.argv[1], 'r') as inputFile:
    COORDINATES_INPUT = inputFile.readlines()

COORDINATES, GRID = day06_lib.initializeGrid(COORDINATES_INPUT)
GRID = day06_lib.determineClosestCoordinate(COORDINATES, GRID)
print("Day06 --- Part One --- result is: {0}".format(day06_lib.getLargestArea(COORDINATES, GRID)))
# print("Day06 --- Part Two --- result is: {0}".format(RESULT_SHORTEST_POLYMER))
