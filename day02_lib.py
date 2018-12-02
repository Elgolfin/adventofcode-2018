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

def countLetters (str):
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