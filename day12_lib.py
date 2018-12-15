"""Day 12 puzzle solutions"""

def initializeGarden (inputs):
    """Initialize the garden"""

    initialState = ""
    spreadTable = {}
    for line in inputs:
        if len(line) <= 0:
            continue
        if line[0] == 'i':
            initialState = line.replace("initial state: ", "").strip()
        if line[0] == '.' or line[0] == '#':
            spread, result = line.split(" => ")
            spreadTable[spread] = result.strip()

    return initialState, spreadTable

def growNextGeneration (state, spreadTable):
    "Grow the next generation of the plants based on a table of spreads"
    state = "...." + state + "...."
    newState = ""
    idx = 0
    for i in range(2, len(state) - 2):
        currentSpread = state[i-2:i+3]
        if currentSpread in spreadTable:
            if (i == 2 or i == 3) and spreadTable[currentSpread] == '#':
                newState = newState + spreadTable[currentSpread]
                idx += 1
                continue
            if (i == 2 or i == 3) and spreadTable[currentSpread] == '.':
                continue
            newState = newState + spreadTable[currentSpread]
        else:
            if (i == 2 or i == 3):
                continue
            newState = newState + '.'
    return newState.rstrip('.'), idx

def sumPotNumbersAfterNGenerations(initialState, spreadTable, n):
    newState, index = initialState, 0
    sumPotNumbers = 0
    for _ in range(1, n + 1):
        newState, newIndex = growNextGeneration(newState, spreadTable)
        index += newIndex
    currentIndex = index * -1
    for pot in newState:
        if pot == '#':
            sumPotNumbers += currentIndex
        currentIndex += 1
    return sumPotNumbers