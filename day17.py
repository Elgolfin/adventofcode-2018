"""Day 17 puzzle solutions"""

import sys
import day17_lib

with open(sys.argv[1], 'r') as inputFile:
    INPUT = inputFile.readlines()

GROUND = day17_lib.initializeGround(INPUT)
WATER_TILES, STILL_WATER_TILES = day17_lib.countWaterTiles(GROUND, (500, 0), False)
print("Day17 --- Part One --- result is: {0}".format(WATER_TILES))
print("Day17 --- Part Two --- result is: {0}".format(STILL_WATER_TILES))