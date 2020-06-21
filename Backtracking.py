#from State import *
from Operator import *

class Backtracking:
    def search(self):
        class Node:
            def __init__(self, state, parent, operator):
                self.state = state
                self.parent = parent
                self.operator = operator
                self.remainingOperators = ['horizontal', 'vertical']

        currentNode = Node(State(), None, None)
        opr = Operator()

        sor = currentNode.state.size + 1
        oszlop = currentNode.state.size + 2

        while True:
            if currentNode.state.isGoalState():
                break

            i,j = currentNode.state.findNextFreeLocation()

            if j == oszlop - 1:
                if opr.isApplicableVertical(currentNode.state, i, j) and 'vertical' in currentNode.remainingOperators:
                    currentNode.remainingOperators.remove('vertical')
                    newState = opr.applyVertical(currentNode.state, i, j)
                    currentNode = Node(newState, currentNode, 'vertical')
                    continue
                else:
                    if not (currentNode.parent == None):
                        #childNode = currentNode
                        currentNode = currentNode.parent
                        #currentNode.child = childNode
                        continue
                    else:
                        print("No solution")
                        break

            if i == sor - 1:
                if opr.isApplicableHorizontal(currentNode.state, i, j) and 'horizontal' in currentNode.remainingOperators:
                    currentNode.remainingOperators.remove('horizontal')
                    newState = opr.applyHorizontal(currentNode.state, i, j)
                    currentNode = Node(newState, currentNode, 'horizontal')
                    continue
                else:
                    if not(currentNode.parent == None):
                        #childNode = currentNode
                        currentNode = currentNode.parent
                        #currentNode.child = childNode
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
                    #childNode = currentNode
                    currentNode = currentNode.parent
                    #currentNode.child = childNode
                else:
                    print("No solution")
                    break

        solution = []

        if currentNode.state.isGoalState():
            while not(currentNode.parent == None):
                solution.append(currentNode.operator)
                currentNode = currentNode.parent

        for i in range(len(solution)-1, -1, -1):
            print(len(solution) - i, '. ', solution[i])

def main():
    b = Backtracking()
    b.search()

if __name__== '__main__':
    main()