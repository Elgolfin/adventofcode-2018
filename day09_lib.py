"""Day 09 puzzle solutions"""

import collections

def playMarble (numPlayers, lastMarblePoints):
    """Return the high score"""
    gameboard = collections.deque([0])
    players = {p: 0 for p in range(1, numPlayers + 1)}

    for marble in range(1, lastMarblePoints + 1):
        player = marble % numPlayers + 1
        if marble % 23 > 0:
            gameboard.rotate(-1)
            gameboard.append(marble)
        else:
            gameboard.rotate(7)
            players[player] += marble + gameboard.pop()
            gameboard.rotate(-1)

    return max(players.values())