"""Day 11 puzzle solutions"""

def getPowerLevel (x, y, serialNumber):
    """Get the power level of a given cell"""

    # - Find the fuel cell's rack ID, which is its X coordinate plus 10.
    rackID = x + 10

     # - Begin with a power level of the rack ID times the Y coordinate.
    powerLevel = rackID * y

    # - Increase the power level by the value of the grid serial number (your puzzle input).
    powerLevel += serialNumber

    # - Set the power level to itself multiplied by the rack ID.
    powerLevel *= rackID

    # - Keep only the hundreds digit of the power level (so 12345 becomes 3; numbers with no hundreds digit become 0).
    if powerLevel > 99:
        powerLevel = int(str(powerLevel)[-3])
    else:
        powerLevel = 0

    # - Subtract 5 from the power level.
    powerLevel -= 5

    return powerLevel

def getLargestTotalPowerArea (serialNumber):
    width = 300
    height = 300
    largestTotalPowerAreaTopLeftCoordinates = (0, 0)
    grid = [[getPowerLevel(x, y, serialNumber) for y in range (1, width + 1)] for x in range(1, height + 1)]
    totalPower = -9999999
    for x in range(300 - 3):
        for y in range(300 - 3):
            currentTotalPower = grid[x][y] + grid[x+1][y] + grid[x+2][y]
            currentTotalPower += grid[x][y+1] + grid[x+1][y+1] + grid[x+2][y+1]
            currentTotalPower += grid[x][y+2] + grid[x+1][y+2] + grid[x+2][y+2]
            if currentTotalPower > totalPower:
                totalPower = currentTotalPower
                largestTotalPowerAreaTopLeftCoordinates = (x + 1, y + 1)
    return largestTotalPowerAreaTopLeftCoordinates