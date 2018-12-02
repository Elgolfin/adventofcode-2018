"""Day 01 puzzle solutions"""

def calibrate_frequency(frequencies):
    """Returns the resulting frequency"""
    result = 0
    position = 0
    for frequency in frequencies:
        result += int(frequency)
        position += 1
    return result

def get_first_frequency_reached_twice(frequencies):
    """Returns the first frequency the device reaches twice"""
    foundFrequency = False
    reachedFrequencies = {}
    result = 0
    while foundFrequency is not True:
        for frequency in frequencies:
            result += int(frequency)
            if str(result) in reachedFrequencies:
                foundFrequency = True
                reachedFrequencies[str(result)] = 2
                break
            else:
                reachedFrequencies[str(result)] = 1
    return result