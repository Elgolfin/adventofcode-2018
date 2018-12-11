"""Day 10 puzzle solutions"""

from sys import stdout
from time import sleep

def getMessage (entries):
    """Display the message when the time is right"""

    points = []
    for entry in entries:
        entry = entry.replace("position=<", "").replace("velocity=<","").replace("> ", ";").replace(">", "").strip().split(";")
        px, py = [int(i.strip()) for i in entry[0].split(", ")]
        vx, vy = [int(i.strip()) for i in entry[1].split(", ")]
        points.append([(px, py),(vx, vy)])

    print()
    duration = 1
    maxY = -999999
    minY = 999999
    maxX = -999999
    minX = 999999
    previousDiff = 999999
    for second in range(1,10500):
        tmpPoints = list()
        for point in points:
            newPx = point[0][0] + point[1][0]
            newPy = point[0][1] + point[1][1]
            if newPy > maxY:
                maxY = newPy
            if newPy < minY:
                minY = newPy
            if newPx > maxX:
                maxX = newPx
            if newPx < minX:
                minX = newPx
            tmpPoints.append([(newPx, newPy), point[1]])
        # Look for the height difference between the lowest point and  highest poiny on the y axis
        diff = abs(maxY - minY)
        if diff < previousDiff:
            points = tmpPoints
            previousDiff = diff
            maxY = -999999
            minY = 999999
            maxX = -999999
            minX = 999999
        # When the diff do not decrease anymore, then we know that we have find the message
        # Beware, we will have to move the message on the X axis to make it appear properly
        else:
            duration = second - 1
            break

    # Initialize an empty grid
    grid =[[' ' for x in range(minX, maxX)] for y in range(minY, maxY)]

    # Fill the grid with the points
    for point in points:
        grid[point[0][1] - minY][point[0][0] - minX] = "#"

    # Draw the grid
    print()
    print()
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            print(grid[y][x], sep=' ', end='', flush=True)
        print()
    print()

    return duration



# for i in range(1,20):
#     stdout.write("\r%d" % i)
#     stdout.write("\n")
#     stdout.flush()
#     sleep(1)