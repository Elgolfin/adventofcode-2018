"""Day 17 puzzle solutions"""

from collections import defaultdict

def initializeGround (inputs):
    """Initialize the garden"""

    ground = defaultdict(set)

    minX = 0
    maxX = 0
    maxY = 0
    clay_x_coordinates = list()
    clay_y_coordinates = list()
    for line in inputs:
        p1, p2 = line.split(", ")
        p1_axis, p1_coordinate = p1.split("=")
        if p1_axis == 'x':
            y_range = p2.replace("y=","").split("..")
            x = int(p1_coordinate)
            for y in range(int(y_range[0]), int(y_range[1]) + 1):
                clay_y_coordinates.append(y)
                clay_x_coordinates.append(x)
        else:
            x_range = p2.replace("x=","").split("..")
            y = int(p1_coordinate)
            for x in range(int(x_range[0]), int(x_range[1]) + 1):
                clay_x_coordinates.append(x)
                clay_y_coordinates.append(y)

    minX = min(clay_x_coordinates)
    maxX = max(clay_x_coordinates)
    minY = min(clay_y_coordinates)
    maxY = max(clay_y_coordinates)
    
    # Initialize a ground full of sand
    for y in range(0, maxY + 1):
        # In case there is an overflow on the left or on the right (x-axis is infintie)
        # Add 1 unit on each side
        for x in range(minX - 1, maxX + 1 + 1):
            ground[(x, y)] = '.'

    # Initialize the spring of water
    ground[(500, 0)] = '+'

    # Initialize the clays
    for i, _ in enumerate(clay_x_coordinates):
        ground[(clay_x_coordinates[i], clay_y_coordinates[i])] = '#'
    # printGround(ground)

    ground[(-1, -1)] = (minY, maxY)

    return ground

def countWaterTiles (ground, startingCell, debug = False):
    minY = ground[(-1, -1)][0]
    maxY = ground[(-1, -1)][1]
    ground.pop((-1, -1))
    x_coordinates, _ = zip(*ground.keys())
    minX = min(x_coordinates)
    maxX = max(x_coordinates)
    
    if debug:
        print("minx x/ max x/ max y: {0}/{1}/{2}".format(minX, maxX, maxY))

    flowingWaterHistory = []

    i = 1 # for the safeguard mechanism, see below
    max_iterations = 10000000
    cellQueue = [startingCell]
    lastFlowingWaterCellCoordinate = set()
    if debug:
        print()
    while True:
        if debug:
            print("___")
            print("Flowing water history: {0}".format(flowingWaterHistory))
            print("Queue to process: {0}".format(cellQueue))
        if not cellQueue:
            break
        currentCellCoordinate = cellQueue.pop()
        currentCellType = ground[currentCellCoordinate]
        if debug:
            print("Current cell: {0} / {1}".format(currentCellCoordinate, currentCellType))

        if currentCellType == '+' or currentCellType == '|':
            
            nextBottomCellCoordinate = (currentCellCoordinate[0], currentCellCoordinate[1] + 1)
            if debug:
                print("Next bottom cell: {0} / {1}".format(nextBottomCellCoordinate, ground[nextBottomCellCoordinate]))

            # Exit mechanism, water cannot propagate anymore below the max y level
            if nextBottomCellCoordinate[1] > maxY:
                continue

            # Go down, otherwise go left or right
            if ground[nextBottomCellCoordinate] == '.':
                if debug:
                    print("Going down")
                ground[nextBottomCellCoordinate] = '|'
                flowingWaterHistory.append(nextBottomCellCoordinate)
                cellQueue.append(nextBottomCellCoordinate)
            else:
                if ground[nextBottomCellCoordinate] == '#' or ground[nextBottomCellCoordinate] == '~':
                    nextLeftCellCoordinate = (currentCellCoordinate[0] - 1, currentCellCoordinate[1])
                    nextRightCellCoordinate = (currentCellCoordinate[0] + 1, currentCellCoordinate[1])
                    nextLeftCellType, nextRightCellType = '', ''
                    if nextLeftCellCoordinate[0] >= minX:
                        nextLeftCellType = ground[nextLeftCellCoordinate]
                    if nextRightCellCoordinate[0] <= maxX:
                        nextRightCellType = ground[nextRightCellCoordinate]
                    if debug:
                        print("Next left cell: {0} / {1}".format(nextLeftCellCoordinate, nextLeftCellType))
                        print("Next right cell: {0} / {1}".format(nextRightCellCoordinate, nextRightCellType))
                    if nextLeftCellType == '.' or nextRightCellType == '.' :
                        cellQueue.extend(settleWater(ground, currentCellCoordinate, flowingWaterHistory, debug))
                    if nextLeftCellType == '#' and nextRightCellType == '#' :
                        ground[currentCellCoordinate] = '~'
                        if debug:
                            print("Going up")
                        if currentCellCoordinate in flowingWaterHistory :
                            flowingWaterHistory.remove((currentCellCoordinate))
                            cellQueue.append((currentCellCoordinate[0], currentCellCoordinate[1] - 1))

        if debug:
            printGroundPart(ground, currentCellCoordinate[0], currentCellCoordinate[1])
        # input("")

        if not cellQueue:
            if debug:
                print("Queue is empty")
            if currentCellCoordinate != lastFlowingWaterCellCoordinate:
                if flowingWaterHistory:
                    lastFlowingWaterCellCoordinate = flowingWaterHistory.pop()
                    cellQueue.append(lastFlowingWaterCellCoordinate)
                if debug:
                    print("Last flowing water cell: {0}".format(lastFlowingWaterCellCoordinate))
                continue
            else:
                if debug:
                    print()
                    print("__FINAL__")
                    printGroundPart(ground, currentCellCoordinate[0], currentCellCoordinate[1])
                break

        # Safeguard mechanism to prevent infinite loop
        i += 1
        if i >= max_iterations: 
            break
    
    # printGround(ground)
    return sum(1 for (x, y), c in ground.items() if (y >= minY and y <= maxY) and (c == '~' or c =='|')), sum(1 for c in ground.values() if c == '~')

def settleWater (ground, origin, flowingWaterHistory, debug = False):
    x_coordinates, _ = zip(*ground.keys())
    minX = min(x_coordinates)
    maxX = max(x_coordinates)
    y = origin[1]
    leftStopCoordinate = set()
    rightStopCoordinate = set()
    newOrigin = list()
    for x in range(origin[0], maxX + 1):
        if ground[(x, y + 1)] != '#' and ground[(x, y + 1)] != '~':
            break
        if ground[(x, y)] == '#':
            if debug:
                print("  found right stop")
            rightStopCoordinate = (x, y)
            break
    for x in range(origin[0], minX - 1, -1):
        if ground[(x, y + 1)] != '#' and ground[(x, y + 1)] != '~':
            break
        if ground[(x, y)] == '#':
            if debug:
                print("  found left stop")
            leftStopCoordinate = (x, y)
            break

    if leftStopCoordinate and rightStopCoordinate:
        if debug:
            print("Fill with still water to both sides")
        for x in range(leftStopCoordinate[0] + 1, rightStopCoordinate[0]):
            if ground[(x, y)] == '.' or ground[(x, y)] == '|':
                if ground[(x, y)] == '|' and (x, y) in flowingWaterHistory :
                    flowingWaterHistory.remove((x,y))
                ground[(x, y)] = '~'
        if ground[(origin[0], origin[1] - 1)] == '|':
            newOrigin.append((origin[0], origin[1] - 1))
        else:
            if flowingWaterHistory:
                newOrigin.append(flowingWaterHistory.pop())
    
    if leftStopCoordinate and not rightStopCoordinate:
        newOrigin.append(fillWaterToTheSide(ground, leftStopCoordinate[0] + 1, maxX + 1, y, debug))
    
    if not leftStopCoordinate and rightStopCoordinate:
        newOrigin.append(fillWaterToTheSide(ground, rightStopCoordinate[0] - 1, minX - 1, y, debug))
    
    if not leftStopCoordinate and not rightStopCoordinate:
        newOrigin.append(fillWaterToTheSide(ground, origin[0], maxX + 1, y, debug))
        newOrigin.append(fillWaterToTheSide(ground, origin[0], minX - 1, y, debug))

    return newOrigin

def fillWaterToTheSide (ground, p_from, p_to, y, debug = False):
    step = 1

    if p_from > p_to:
        step *= -1
        if debug:
            print("Fill with flowing water from {0} to {1}".format(p_from, p_to))
        pass
    else:
        if debug:
            print("Fill with flowing water from {0} to {1}".format(p_from, p_to))
        pass

    for x in range(p_from, p_to, step):
        newOrigin = (x, y)
        if (ground[(x, y + 1)] == '#' or ground[(x, y + 1)] == '~') and (ground[(x, y)] == '.' or ground[(x, y)] == '|'):
            if debug:
                print('Fill cell {0} with flowing water and continue'.format((x, y)))
            ground[(x, y)] = '|'
        else:
            if debug:
                print('Fill cell {0} with flowing water and stop'.format((x, y)))
            # newOrigin = (x - step, y)
            ground[newOrigin] = '|'
            break
    if debug:
        print("{0} will be added to the queue".format(newOrigin))
    return newOrigin

def printGround (ground):
    """https://stackoverflow.com/questions/12974474/how-to-unzip-a-list-of-tuples-into-individual-lists#12974504"""
    x_coordinates, y_coordinates = zip(*ground.keys())
    minX = min(x_coordinates)
    maxX = max(x_coordinates)
    minY = min(y_coordinates)
    maxY = max(y_coordinates)

    print()
    for y in range(minY, maxY + 1):
        for x in range(minX, maxX + 1 ):
            print(ground[(x, y)], sep=' ', end='', flush=True)
        print()
    return

def printGroundPart (ground, x, y):
    """https://stackoverflow.com/questions/12974474/how-to-unzip-a-list-of-tuples-into-individual-lists#12974504"""
    x_coordinates, y_coordinates = zip(*ground.keys())
    minX = max(min(x_coordinates), x - 20)
    maxX = min(max(x_coordinates), x + 20)
    minY = max(min(y_coordinates), y - 10)
    maxY = min(max(y_coordinates), y + 10)

    print()
    for y in range(minY, maxY + 1):
        for x in range(minX, maxX + 1 ):
            print(ground[(x, y)], sep=' ', end='', flush=True)
        print()
    print()
    return