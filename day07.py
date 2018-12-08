"""Day 07 puzzle solutions"""

import sys
import day07_lib

with open(sys.argv[1], 'r') as inputFile:
    STEP_ENTRIES = inputFile.readlines()

STARTING_STEPS, STEPS = day07_lib.findStartingSteps(STEP_ENTRIES)
print("Day07 --- Part One --- result is: {0}".format(day07_lib.completeSteps(STARTING_STEPS, STEPS, 1, 0)))
STARTING_STEPS, STEPS = day07_lib.findStartingSteps(STEP_ENTRIES)
print("Day07 --- Part Two --- result is: {0}".format(day07_lib.completeSteps(STARTING_STEPS, STEPS, 5, 60)))