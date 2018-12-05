"""Day 04 puzzle solutions"""

def getGuardResult(entries):
    """Parse a claim on the format #123 @ 3,2: 5x4"""
    entries.sort()
    records = {}
    previousMinutes = 0
    previousMode = ''
    guardId = -1
    for entry in entries:
        minutes = int(entry[15:17])
        mode = entry[25:].strip().split(' ')[0].strip('#')
        if mode == 'up':
            for m in range(previousMinutes, minutes):
                records[guardId][m] += 1
            # print('Guard wakes up at {0}'.format(minutes))
            previousMode = mode
        else:
            if mode == 'asleep':
                # print('Guard falls asleep at {0}'.format(minutes))
                previousMode = mode
            else:
                if previousMode == 'asleep':
                    for m in range(previousMinutes, 60):
                        records[guardId][m] += 1 # Update the guard previous record
                guardId = mode
                # print('Guard #{0} begins shift'.format(guardId))
                if guardId not in records:
                    guardId = mode
                    records[guardId] = [0 for _ in range(60)]
        previousMinutes = minutes

    if previousMode == 'asleep':
        for m in range(previousMinutes, 60):
            records[guardId][m] += 1 # Update the guard last record
    # print(records)

    resultGuardId = -1
    maxMinutes = 0
    for gid, gminutes in records.items():
        totalMin = sum([m for m in gminutes if m > 0])
        if totalMin > maxMinutes:
            maxMinutes = totalMin
            resultGuardId = gid
    # print(resultGuardId)
    # print(maxMinutes)
    # print(records[resultGuardId].index(max(records[resultGuardId])))
    return int(resultGuardId) * records[resultGuardId].index(max(records[resultGuardId]))