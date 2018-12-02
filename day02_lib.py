"""Day 02 puzzle solutions"""

def checksum(strings):
    """Returns the checksum"""
    checksum = 0
    twiceCount = 0
    threeTimesCount = 0
    for str in strings:
        twice, threeTimes = countLetters(str)
        if twice > 0:
            twiceCount += 1
        if threeTimes > 0:
            threeTimesCount += 1
    checksum = twiceCount * threeTimesCount
    return checksum

def countLetters(str):
    """Counts the number of times a letter appears twice and three times in a string"""
    twice = 0
    threeTimes = 0
    lettersDict = {}
    for letter in list(str):
        if letter in lettersDict:
            lettersDict[letter] += 1
        else:
            lettersDict[letter] = 1
    for k, v in lettersDict.items():
        if v == 3:
            threeTimes += 1
        else:
            if v == 2:
                twice += 1
    return twice, threeTimes

def getCommonLetters(strings):
    """Returns the common letters between two correct box IDs"""
    # print("")
    result = ""
    while strings and not result:
        currentStr = strings.pop(0)
        # print("Test {0}".format(currentStr))
        for str in strings:
            # print("   against {0}".format(str))
            diffIdx = 0
            idx = 0
            diff = 0
            for letter in currentStr:
                # print("       test letter {0}".format(letter))
                if letter != str[idx]:
                    diff += 1
                    diffIdx = idx
                    if diff > 1:
                        break
                # print("       Index: {0} / Diff: {1}".format(idx, diff))
                idx += 1
            if diff == 1:
                # print("   Found it {0} at index {1}".format(currentStr, diffIdx))
                result = currentStr[:diffIdx] + currentStr[diffIdx+1:]
                # print("   Found it {0}".format(result))
                break
    return result