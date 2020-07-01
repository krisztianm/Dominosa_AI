from Operator import *

class Backtracking:
    def search(self, initialState):
        class Node:
            def __init__(self, state, parent, operator):
                self.state = state
                self.parent = parent
                self.operator = operator
                self.remainingOperators = ['horizontal', 'vertical']

        currentNode = Node(initialState, None, None)
        opr = Operator()

        row = currentNode.state.size + 1
        column = currentNode.state.size + 2

        while True:
            if currentNode.state.isGoalState():
                break

            i,j = currentNode.state.findNextFreeLocation()

            if j == column - 1:
                if opr.isApplicableVertical(currentNode.state, i, j) and 'vertical' in currentNode.remainingOperators:
                    currentNode.remainingOperators.remove('vertical')
                    newState = opr.applyVertical(currentNode.state, i, j)
                    currentNode = Node(newState, currentNode, 'vertical')
                    continue
                else:
                    if not (currentNode.parent == None):
                        currentNode = currentNode.parent
                        continue
                    else:
                        print("No solution")
                        break

            if i == row - 1:
                if opr.isApplicableHorizontal(currentNode.state, i, j) and 'horizontal' in currentNode.remainingOperators:
                    currentNode.remainingOperators.remove('horizontal')
                    newState = opr.applyHorizontal(currentNode.state, i, j)
                    currentNode = Node(newState, currentNode, 'horizontal')
                    continue
                else:
                    if not(currentNode.parent == None):
                        currentNode = currentNode.parent
                        continue
                    else:
                        print("No solution")
                        break

            if opr.isApplicableHorizontal(currentNode.state, i, j) and 'horizontal' in currentNode.remainingOperators:
                currentNode.remainingOperators.remove('horizontal')
                newState = opr.applyHorizontal(currentNode.state, i, j)
                currentNode = Node(newState, currentNode, 'horizontal')
            elif opr.isApplicableVertical(currentNode.state, i, j) and 'vertical' in currentNode.remainingOperators:
                currentNode.remainingOperators.remove('vertical')
                newState = opr.applyVertical(currentNode.state, i, j)
                currentNode = Node(newState, currentNode, 'vertical')
            else:
                if not (currentNode.parent == None):
                    currentNode = currentNode.parent
                else:
                    print("No solution")
                    break

        return currentNode.state