class State:
    def __init__(self, size, puzzle):
        self.size = size
        self.puzzle = puzzle
        self.GRID = self.generateGrid(self.size, self.puzzle)
        self.TILES = self.generateTiles(self.size)
        self.BOARD = self.generateGrid(self.size)

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

    def popTile(self, a, b):
        self.TILES.pop(self.TILES.index([a, b]))
        if a != b:
            self.TILES.pop(self.TILES.index([b, a]))

    def findNextFreeLocation(self):
        for i in range(self.size + 1):
            for j in range(self.size + 2):
                if self.BOARD[i][j] == '-':
                    return i,j
        return None, None