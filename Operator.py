from State import *
from copy import deepcopy

class Operator:
    def placeHorizontal(self, state, i, j):
        state.BOARD[i][j] = 'R'
        state.BOARD[i][j + 1] = 'L'
        state.popTile(state.GRID[i][j], state.GRID[i][j + 1])

    def placeVertical(self, state, i, j):
        state.BOARD[i][j] = 'D'
        state.BOARD[i + 1][j] = 'U'
        state.popTile(state.GRID[i][j], state.GRID[i + 1][j])

    def isApplicableHorizontal(self, state, i, j):
        a = state.GRID[i][j]
        b = state.GRID[i][j + 1]
        return [a, b] in state.TILES and [b, a] in state.TILES and state.BOARD[i][j + 1] == '-'

    def isApplicableVertical(self, state, i, j):
        a = state.GRID[i][j]
        b = state.GRID[i + 1][j]
        return [a, b] in state.TILES and [b, a] in state.TILES and state.BOARD[i+1][j] == '-'

    def applyVertical(self, currentState, i, j):
        newState = State(currentState.size, currentState.puzzle)
        newState.BOARD = deepcopy(currentState.BOARD) # ne módosuljon currentState.BOARD
        newState.TILES = deepcopy(currentState.TILES) # ne módosuljon currentState.TILES
        self.placeVertical(newState, i, j)
        return newState

    def applyHorizontal(self, currentState, i, j):
        newState = State(currentState.size, currentState.puzzle)
        newState.BOARD = deepcopy(currentState.BOARD) # ne módosuljon currentState.BOARD
        newState.TILES = deepcopy(currentState.TILES) # ne módosuljon currentState.TILES
        self.placeHorizontal(newState, i, j)
        return newState

