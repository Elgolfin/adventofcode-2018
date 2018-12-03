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
    claim["area"] = claim["width"] * claim["height"]
    return claim

def fillSquare(claims, width = 1000, height = 1000):
    """Fills a square from a collection of claims"""
    w, h = width, height
    matrix = [['.' for x in range(w)] for y in range(h)]
    claimsDict = {}
    for claimStr in claims:
        claim = parseClaim(claimStr)
        claimsDict[str(claim["id"])] = claim
        for y in range(claim['top'], claim['top']+claim['height']):
            for x in range(claim['left'], claim['left']+claim['width']):
                if matrix[y][x] == '.':
                    matrix[y][x] = claim['id']
                else:
                    matrix[y][x] = 'X'
    # printSquare(matrix)
    return claimsDict, matrix

def lookForNotVerlappingClaim(claimsDict, square):
    claimsArea = {}
    notVerlappingClaimId = 0
    
    # Calculate all areas (do not count overlapped cells)
    for y in range(0, len(square)):
        for x in range(0, len(square[y])):
            if square[y][x] != 'X' or square[y][x] != '.':
                if str(square[y][x]) in claimsArea:
                    claimsArea[str(square[y][x])] += 1
                else:
                    claimsArea[str(square[y][x])] = 1

    # If there is a claim with the exact area in the dict, this is the one we are looking for
    # Discard any other claim that has an area only composed of 'X' or that has an area that does not fit its expected area
    for _, claim in claimsDict.items():
        claimId = str(claim["id"])
        if claimId in claimsArea and claimsArea[str(claimId)] == claim["area"]:
            notVerlappingClaimId = claim["id"]
    return notVerlappingClaimId


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