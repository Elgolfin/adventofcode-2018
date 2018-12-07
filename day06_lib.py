"""Day 06 puzzle solutions"""

import string
from collections import defaultdict

def getManhattanDist (p1, p2):
    """Gets the manhattan distance between two points"""
    dist = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    return dist

def getClosestManhattanDist (p1, coordinates):
    """Gets the closest manhattan distance of a point from a list of coordinates"""
    closestDist = 1000
    closestDistPointName = ''
    for point, coordinate in coordinates.items():
        dist = abs(p1[0] - coordinate[0]) + abs(p1[1] - coordinate[1])
        if dist < closestDist:
            closestDist = dist
            closestDistPointName = point
        else:
            if dist == closestDist:
                closestDistPointName = '.'
    return closestDistPointName

def getSumAllManhattanDist (p1, coordinates):
    """Gets the sum pf all manhattan distances of a point from a list of coordinates"""
    sumManhattanDist = 0
    for _, coordinate in coordinates.items():
        dist = abs(p1[0] - coordinate[0]) + abs(p1[1] - coordinate[1])
        sumManhattanDist += dist
    return sumManhattanDist

def initializeGrid (entries):
    """Initialize the grid by drawing each point coordinates"""
    currentIdx = 0
    coordinates = {}
    height = 0
    width = 0
    # Get the coordinates
    for point in entries:
        x = int(point.strip().split(", ")[0])
        y = int(point.strip().split(", ")[1])
        coordinates[string.ascii_letters[currentIdx]] = (x, y)
        currentIdx += 1
        if x > width:
            width = x
        if y > height:
            height = y

    # Initialize the grid
    grid = [ ['.' for y in range(height + 1)] for x in range(width + 1)]

    # Draw the coordinates
    for point, coordinate in coordinates.items():
        grid[coordinate[0]][coordinate[1]] = point
    
    return coordinates, grid

def determineClosestCoordinate (coordinates, grid):
    """Fill the grid with each location's closest coordinate"""
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == '.':
                grid[x][y] = getClosestManhattanDist((x, y), coordinates)
    return grid

def getLargestArea (coordinates, grid):
    """Get the grid largest finite area"""
    areas = defaultdict(lambda: 0)
    infinite_areas = set()
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == '.':
                continue
            areas[grid[x][y]] += 1
            if x == 0 or x == len(grid) - 1 or y == 0 or y == len(grid[x]) - 1:
                infinite_areas = infinite_areas | { grid[x][y] }

    for point in infinite_areas:
        del areas[point]

    return max(areas.values())

def getSizeOfAllLocationsWithinLimit (coordinates, grid, limit):
    """Get the size of all locations which have a total distance to all given coordinates of less than 10000"""
    areaSize = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            sumDist = getSumAllManhattanDist((x, y), coordinates)
            if sumDist < limit:
                areaSize += 1
    return areaSize