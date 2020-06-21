from UI import *

class State:
    def __init__(self):
        self.size = 7#UI.lineEditSetSize.text()
        self.GRID = self.generateGrid(self.size, '457143714462730512277567551503407626606503620164257511364234330322047011')
        self.TILES = self.generateTiles(self.size)
        self.BOARD = self.initialState()

    def initialState(self):
        state = self.generateGrid(self.size)
        return state

    def isGoalState(self):
        return not any('-' in row for row in self.BOARD)

    def generateGrid(self, size, character='-'):
        if len(character) == 1:
            return [[character for j in range(size + 2)] for i in range(size + 1)]
        else:
            return [[int(character[i * (size + 2) + j]) for j in range(size + 2)] for i in range(size + 1)]

    def generateTiles(self, n):
        tiles = []

        for i in range(0, n + 1):
            for j in range(0, n + 1):
                if (i, j) not in tiles:
                    tiles.append([i, j])

        return tiles

    def appendTile(self, a, b):
        self.TILES.append([a, b])
        if a != b:
            self.TILES.append([b, a])

    def popTile(self, a, b):
        self.TILES.pop(self.TILES.index([a, b]))
        if a != b:
            self.TILES.pop(self.TILES.index([b, a]))

    def isItSame(self, a, b, c, d):  # két tile ugyanaz-e?
        return ((a == c) and (b == d)) or ((a == d) and (b == c))

    def findNextFreeLocation(self):
        for i in range(self.size + 1):
            for j in range(self.size + 2):
                if self.BOARD[i][j] == '-':
                    return i,j
        return None, None