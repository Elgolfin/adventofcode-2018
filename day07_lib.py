"""Day 07 puzzle solutions"""

import string
from collections import defaultdict

def findStartingSteps (entries):
    """Gets all starting steps"""
    steps = defaultdict(lambda: set())
    successors = set()
    for entry in entries:
        step1, step2 = parseStepLine(entry)
        steps[step2].add(step1)
        if step1 not in steps:
            steps[step1] = set()
        successors.add(step2)
    startingSteps = sorted(list((steps.keys() | set()).difference(successors)))
    # print(steps)
    # print(startingSteps)
    return startingSteps, steps 

def orderSteps (availableSteps, steps):
    done = set()
    result = []
    while len(availableSteps) > 0:
        currentStep = availableSteps.pop(0)
        result.append(currentStep)
        done.add(currentStep)
        del steps[currentStep]
        availableSteps = getAvailableSteps(done, steps)
    return ''.join(result)

def getAvailableSteps (doneSteps, steps):
    availableSteps = []
    for step, nextSteps in steps.items():
        if nextSteps.issubset(doneSteps):
            availableSteps.append(step)
    return sorted(availableSteps)

def parseStepLine (line):
    result = line.strip().split(" must be finished before step ")
    step1Name = result[0].replace("Step ", "").strip()
    step2Name = result[1].replace(" can begin.", "").strip()
    return step1Name, step2Name