"""Day 01 puzzle solutions"""

def calibrate_frequency(frequencies):
    """Returns the resulting frequency"""
    result = 0
    position = 0
    for frequency in frequencies:
        result += int(frequency)
        position += 1
    return result
