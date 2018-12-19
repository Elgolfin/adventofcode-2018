"""Day 17 puzzle solutions"""

from collections import defaultdict

def initializeGround (inputs):
    """Initialize the garden"""

    ground = defaultdict(set)

    minX = 0
    maxX = 0
    minY = 0
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
        for x in range(minX, maxX + 1 ):
            ground[(x, y)] = '.'

    # Initialize the spring of water
    ground[(500, 0)] = '+'

    # Initialize the clays
    for i, _ in enumerate(clay_x_coordinates):
        ground[(clay_x_coordinates[i], clay_y_coordinates[i])] = '#'
    printGround(ground)

    return ground

def countWaterTiles (ground, startingCell):
    x_coordinates, y_coordinates = zip(*ground.keys())
    minX = min(x_coordinates)
    maxX = max(x_coordinates)
    minY = min(y_coordinates)
    maxY = max(y_coordinates)
    
    i = 1 # for the safeguard mechanism, see below
    max_iterations = 20
    cellQueue = [startingCell]
    print()
    while True:
        print(cellQueue)
        currentCellCoordinate = cellQueue.pop()
        print(currentCellCoordinate)
        currentCellType = ground[currentCellCoordinate]

        if currentCellType == '+' or currentCellType == '|':
            
            nextCellCoordinate = (currentCellCoordinate[0], currentCellCoordinate[1] + 1)
            # Exit mechanism, water cannot propagate anymore below the max y level
            if nextCellCoordinate[1] > maxY:
                break

            # Go down, otherwise go left or right
            if ground[nextCellCoordinate] == '.':
                ground[nextCellCoordinate] = '|'
                cellQueue.append(nextCellCoordinate)
            else:
                if ground[nextCellCoordinate] == '#' or ground[nextCellCoordinate] == '~':
                    cellQueue.extend(settleWater(ground, (currentCellCoordinate)))

        printGround(ground)
        input("")

        if not cellQueue:
            break

        # Safeguard mechanism to prevent infinite loop
        i += 1
        if i >= max_iterations: 
            break

    return 57

def settleWater (ground, origin):
    x_coordinates, _ = zip(*ground.keys())
    minX = min(x_coordinates)
    maxX = max(x_coordinates)
    y = origin[1]
    leftClayCoordinate = set()
    rightClayCoordinate = set()
    newOrigin = list()
    for x in range(origin[0], maxX + 1):
        if ground[(x, y)] == '#':
            rightClayCoordinate = (x, y)
            break
    for x in range(minX, origin[0]):
        if ground[(x, y)] == '#':
            leftClayCoordinate = (x, y)

    print((leftClayCoordinate, rightClayCoordinate))

    if leftClayCoordinate and rightClayCoordinate:
        print("Fill with still water to both sides")
        for x in range(leftClayCoordinate[0] + 1, rightClayCoordinate[0]):
            if ground[(x, y)] == '.' or ground[(x, y)] == '|':
                ground[(x, y)] = '~'
        newOrigin.append((origin[0], origin[1] - 1))
    
    if leftClayCoordinate and not rightClayCoordinate:
        newOrigin.append(fillWaterToTheSide(ground, leftClayCoordinate[0] + 1, maxX + 1, y))
    
    if not leftClayCoordinate and rightClayCoordinate:
        newOrigin.append(fillWaterToTheSide(ground, origin[0], minX - 1, y))
    
    if not leftClayCoordinate and not rightClayCoordinate:
        print("Fill with flowing water to both sides")
        newOrigin.append(fillWaterToTheSide(ground, origin[0], maxX + 1, y))
        newOrigin.append(fillWaterToTheSide(ground, origin[0], minX - 1, y))

    return newOrigin

def fillWaterToTheSide (ground, p_from, p_to, y):
    step = 1

    if p_from > p_to:
        step *= -1
        print("Fill with flowing water to the left")
    else:
        print("Fill with flowing water to the right")

    for x in range(p_from, p_to, step):
        newOrigin = (x, y)
        if ground[(x, y + 1)] == '#' and ground[(x, y)] == '.' or ground[(x, y)] == '|':
            ground[(x, y)] = '|'
        else:
            ground[newOrigin] = '|'
            break
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