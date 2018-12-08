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
    return startingSteps, steps

def getAvailableSteps (doneSteps, steps):
    availableSteps = []
    for step, nextSteps in steps.items():
        if nextSteps.issubset(doneSteps):
            availableSteps.append(step)
    return sorted(availableSteps)

def completeSteps (availableSteps, steps, numWorkers = 5, stepDuration = 60):
    numSteps = len(steps)
    second = 0
    done = set()
    result = []
    workers =  {worker: ('.', 0) for worker in range(numWorkers)}
    while len(result) < numSteps:
        # Free the workers if they are done with the processing of a step
        workers, stepsDone = freeWorkers(workers, second)
        for stepDone in stepsDone:
            result.append(stepDone)
            done.add(stepDone)
            availableSteps = getAvailableSteps(done, steps)

        # Feed the workers if any is available and if any step avalable to be processed
        worker = returnAvailableWorker(workers)
        while worker > -1 and len(availableSteps) > 0:
            currentStep = availableSteps.pop(0)
            workers[worker] = (currentStep, second + ord(currentStep) - 65 + stepDuration)
            del steps[currentStep]
            worker = returnAvailableWorker(workers)
        second += 1
    return ''.join(result), second - 1

def returnAvailableWorker (workers):
    availableWorker = -1
    for worker, (_, availableAt) in workers.items():
        if availableAt == 0:
            availableWorker = worker
            break
    return availableWorker

def freeWorkers (workers, currentSecond):
    stepsDone = set()
    for worker, (step, availableAt) in workers.items():
        if availableAt > 0 and availableAt < currentSecond:
            workers[worker] = ('.', 0)
            stepsDone.add(step)
    return workers, stepsDone

def parseStepLine (line):
    result = line.strip().split(" must be finished before step ")
    step1Name = result[0].replace("Step ", "").strip()
    step2Name = result[1].replace(" can begin.", "").strip()
    return step1Name, step2Name