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
    history = set({})
    newState, index = initialState, 0
    sumPotNumbers = 0
    currentSumPotNumbers = 0
    diff = 0
    history.add(initialState)
    count = 1
    for i in range(1, n + 1):
        count = i
        newState, newIndex = growNextGeneration(newState, spreadTable)
        index += newIndex
        currentSumPotNumbers = sumPots(newState, index)
        diff = currentSumPotNumbers - sumPotNumbers
        if newState.strip('.') in history:
            break
        history.add(newState.strip('.'))
        sumPotNumbers = currentSumPotNumbers
    sumPotNumbers = sumPots(newState, index)
    if count < n:
        sumPotNumbers = sumPotNumbers + (n - count) * diff
    return sumPotNumbers

def sumPots(state, index):
    sumPotNumbers = 0
    currentIndex = index * -1
    for pot in state:
        if pot == '#':
            sumPotNumbers += currentIndex
        currentIndex += 1
    return sumPotNumbers