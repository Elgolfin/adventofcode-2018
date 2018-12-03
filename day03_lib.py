"""Day 03 puzzle solutions"""

import re

def parseClaim(claimStr):
    """Parse a claim on the format #123 @ 3,2: 5x4"""
    claim = {}
    matchObj = re.match( r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', claimStr, re.M|re.I)
    claim["id"] = int(matchObj.group(1))
    claim["left"] = int(matchObj.group(2))
    claim["top"] = int(matchObj.group(3))
    claim["width"] = int(matchObj.group(4))
    claim["height"] = int(matchObj.group(5))
    return claim

def fillSquare(claims, width = 1000, height = 1000):
    """Fills a square from a collection of claims"""
    w, h = width, height
    matrix = [['.' for x in range(w)] for y in range(h)]
    for claimStr in claims:
        claim = parseClaim(claimStr)
        for y in range(claim['top'], claim['top']+claim['height']):
            for x in range(claim['left'], claim['left']+claim['width']):
                if matrix[y][x] == '.':
                    matrix[y][x] = claim['id']
                else:
                    matrix[y][x] = 'X'
    # printSquare(matrix)
    return matrix

def countOverlappingInches(matrix):
    result = 0
    for y in range(0, len(matrix)):
        for x in range(0, len(matrix[y])):
            if matrix[y][x] == 'X':
                result += 1
    return result

def printSquare(square):
    """Prints the square"""
    print()
    for y in range(0, len(square)):
        printLine = ''
        for x in range(0, len(square[y])):
            printLine += str(square[y][x])
        print(printLine)
    return