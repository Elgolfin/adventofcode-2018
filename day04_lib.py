"""Day 04 puzzle solutions"""

def getGuardResult(entries):
    """Solve the day 04 puzzle"""
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

    resultGuardId1 = -1
    resultGuardId2 = -1
    maxMinutesAsleep = 0
    mostFrequentlyAsleepMinute = -1
    for gid, gminutes in records.items():
        totalMin = sum([m for m in gminutes if m > 0])
        frequentlyMin = max(gminutes)
        if totalMin > maxMinutesAsleep:
            maxMinutesAsleep = totalMin
            resultGuardId1 = gid
        if frequentlyMin > mostFrequentlyAsleepMinute:
            mostFrequentlyAsleepMinute = frequentlyMin
            resultGuardId2 = gid
    # print(resultGuardId1)
    # print(maxMinutesAsleep)
    # print(records[resultGuardId].index(max(records[resultGuardId])))
    # print(resultGuardId2)
    # print(records[resultGuardId2].index(mostFrequentlyAsleepMinute))

    result1 = int(resultGuardId1) * records[resultGuardId1].index(max(records[resultGuardId1]))
    result2 = int(resultGuardId2) * records[resultGuardId2].index(mostFrequentlyAsleepMinute)

    return result1, result2