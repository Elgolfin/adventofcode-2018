"""Day 05 puzzle solutions"""

import string

def scanPolymer (polymer):
    """Solve the day 05 puzzle"""
    polymerLength = len(polymer)
    continueReaction = True
    while continueReaction:
        for letter in range(26):
            reaction1 = string.ascii_letters[letter] + string.ascii_letters[letter + 26]
            reaction2 = reaction1[::-1]
            polymer = polymer.replace(reaction1, "")
            polymer = polymer.replace(reaction2, "")
        if polymerLength > len(polymer):
            polymerLength = len(polymer)
        else:
            continueReaction = False
    return len(polymer)

def scanPolymer2 (polymer):
    """Solve the day 05 puzzle"""
    # print(polymer)
    char = ord(polymer[0])
    previousChar = ord(polymer[0])
    idx = 1
    while True:
        char = ord(polymer[idx])
        # print("{0}{1}".format(chr(previousChar), chr(char)))
        diff = abs(previousChar - char)
        if (diff == 32):
            # print('FOUND REACTION, REMOVING {0}{1}'.format(chr(previousChar), chr(char)))
            # print(polymer[:idx - 1 ])
            # print(polymer[idx + 1:])
            polymer = polymer[:idx - 1 ] + polymer[idx + 1:]
            # print('New polymer: {0}'.format(polymer))
            idx -= 3
            if (idx <= 0):
                idx = 0
            char = ord(polymer[idx])
            # print(idx)

        # end loop
        previousChar = char
        idx += 1
        # print(len(polymer))
        if idx >= len(polymer):
            break
    return len(polymer)