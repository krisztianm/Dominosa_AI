from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Backtracking import *
from State import *

import sys

class UI:
    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1200, 600)
        MainWindow.setWindowTitle("Dominosa")
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.framePuzzle = QtWidgets.QFrame(self.centralwidget)

        self.font = QtGui.QFont()
        self.font.setFamily("Arial Black")
        self.font.setPointSize(16)

        self.frameSolution = QtWidgets.QFrame(self.centralwidget)

        self.labelPuzzle = QtWidgets.QLabel(self.centralwidget)
        self.labelPuzzle.setText("Puzzle")
        self.labelPuzzle.setFont(self.font)
        self.labelPuzzle.setGeometry(QtCore.QRect(25,10,150,50))

        self.labelSolution = QtWidgets.QLabel(self.centralwidget)
        self.labelSolution.setText("Solution")
        self.labelSolution.setFont(self.font)
        self.labelSolution.setGeometry(QtCore.QRect(625,10,150,50))

        self.labelCreatePuzzle = QtWidgets.QLabel(self.centralwidget)
        self.labelCreatePuzzle.setText("Puzzle")
        self.labelCreatePuzzle.setFont(self.font)
        self.labelCreatePuzzle.setGeometry(QtCore.QRect(25, 550, 100, 50))

        self.lineEditCreatePuzzle = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditCreatePuzzle.setGeometry(QtCore.QRect(130, 565, 440, 25))

        self.labelSetSize = QtWidgets.QLabel(self.centralwidget)
        self.labelSetSize.setText("Size")
        self.labelSetSize.setFont(self.font)
        self.labelSetSize.setGeometry(QtCore.QRect(625, 550, 70, 50))

        self.lineEditSetSize = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSetSize.setGeometry(QtCore.QRect(695, 565, 50, 25))

        self.buttonCreatePuzzle = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCreatePuzzle.setGeometry(QtCore.QRect(760, 565, 140, 25))
        self.buttonCreatePuzzle.setText("Create Puzzle")

        self.buttonSolvePuzzle = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSolvePuzzle.setGeometry(QtCore.QRect(920, 565, 140, 25))
        self.buttonSolvePuzzle.setText("Solve Puzzle")
        self.buttonSolvePuzzle.setDisabled(True)        # tiltva marad a gomb, amíg helyes inputot nem adunk

        self.buttonSamplePuzzle = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSamplePuzzle.setGeometry(QtCore.QRect(1070, 565, 70, 25))
        self.buttonSamplePuzzle.setText("Samples")

        self.buttonGetHelp = QtWidgets.QPushButton(self.centralwidget)
        self.buttonGetHelp.setGeometry(QtCore.QRect(1150, 565, 40, 25))
        self.buttonGetHelp.setText("Help")

        self.buttonCreatePuzzle.clicked.connect(self.fill)
        self.buttonSolvePuzzle.clicked.connect(self.solve)
        self.buttonSamplePuzzle.clicked.connect(self.showSamples)
        self.buttonGetHelp.clicked.connect(self.popupGetHelp)

        MainWindow.setCentralWidget(self.centralwidget)


    def fill(self):
        self.size = self.lineEditSetSize.text()
        self.char = self.lineEditCreatePuzzle.text()

        if self.size == '' or self.char == '': # üres bemenet esetén előugrik egy ablak
            self.popupWrongInput("No input", "Missing size or puzzle")
            return

        try:
            self.size = int(self.size)        # ValueError amennyiben nem csak számjegyet tartalmaz
            int(self.char)                  # ValueError amennyiben nem csak számjegyet tartalmaz
        except ValueError:
            self.popupWrongInput("Wrong input type", "Puzzle and size input must contain only digits")
            return


        if len(self.char) != (self.size + 1)*(self.size + 2):       # nem megfelelő méret esetén előugrik egy ablak
            self.popupWrongInput("Wrong input", "Wrong input size or puzzle length")
            return

        self.buttonSolvePuzzle.setDisabled(False)       # ha helyes az input, elérhetővé válik a megoldás gomb

        self.framePuzzle.setGeometry(QtCore.QRect((600 - 50*(self.size+2))/2, (600 - 50*(self.size+1))/2, 50*(self.size+2), 50*(self.size+1)))
        #bal oldalra közepére helyezzük el a frame-et, oszlop+2 darab 50 pixel széles és oszlop+1 darab 50 pixel magas mérettel
        while(self.framePuzzle.children()):
            self.framePuzzle.children()[0].setParent(None)

        self.framePuzzle.hide()
        for i in range(self.size + 1): # bal oldali frame-et töltjük fel a számokkal
            for j in range(self.size + 2):
                self.label = QtWidgets.QLabel(self.framePuzzle)
                self.label.setText(self.char[i * (self.size + 2) + j])
                self.label.setGeometry(QtCore.QRect(j * 50, i * 50, 50, 50))
                self.label.setFont(self.font)
                self.label.setStyleSheet(
                        ".QLabel {border: 2px solid #cccccc;border-radius: 25px;background-color: #cccccc;}")
                self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.framePuzzle.show()


    def solve(self):
        solution = Backtracking().search(State(int(self.size), self.char))

        self.frameSolution.setGeometry(QtCore.QRect(600+(600 - 50*(self.size+2))/2, (600 - 50*(self.size+1))/2, 50*(self.size+2), 50*(self.size+1)))
        # jobb oldalra közepére helyezzük el a frame-et, oszlop+2 darab 50 pixel széles és oszlop+1 darab 50 pixel magas mérettel
        while (self.frameSolution.children()):
            self.frameSolution.children()[0].setParent(None)

        self.frameSolution.hide()

        if solution.isGoalState():
            for i in range(self.size + 1):  # jobb oldali fram-et töltjük fel a megoldással
                for j in range(self.size + 2):
                    self.label = QtWidgets.QLabel(self.frameSolution)
                    self.label.setText(self.char[i * (self.size + 2) + j])
                    self.label.setAlignment(QtCore.Qt.AlignCenter)
                    self.label.setFont(self.font)
                    self.label.setGeometry(QtCore.QRect(j * 50, i * 50, 50, 50))
                    if solution.BOARD[i][j] == 'L':  # balra tőle a párja, jobb oldali borderek lekerekítettek
                        self.label.setStyleSheet(
                            ".QLabel {border: 2px solid;border-top-right-radius: 15px;border-bottom-right-radius: 15px;background-color: red;}")
                        #self.label.setText('L')
                    if solution.BOARD[i][j] == 'R':  # jobbre tőle a párja, bal oldali borderek lekerekítettek
                        self.label.setStyleSheet(
                            ".QLabel {border: 2px solid;border-top-left-radius: 15px;border-bottom-left-radius: 15px;background-color: red;}")
                        #self.label.setText('R')
                    if solution.BOARD[i][j] == 'D':  # alatta a párja, felső borderek lekerekítettek
                        self.label.setStyleSheet(
                            ".QLabel {border: 2px solid;border-top-left-radius: 15px;border-top-right-radius: 15px;background-color: red;}")
                        #self.label.setText('D')
                    if solution.BOARD[i][j] == 'U':  # felette a párja, alsó borderek lekerekítettek
                        self.label.setStyleSheet(
                            ".QLabel {border: 2px solid;border-bottom-left-radius: 15px;border-bottom-right-radius: 15px;background-color: red;}")
                        #self.label.setText('U')
        else:
            self.popupNoSolution()
        self.frameSolution.show()
        self.buttonSolvePuzzle.setDisabled(True) #letiltjuk a gombot, hogy ne lehessen spammelni

    def popupNoSolution(self):
        msgbox = QMessageBox()
        msgbox.setWindowTitle("No solution")
        msgbox.setText("No solution found for the given puzzle")
        msgbox.setIcon(QMessageBox.Warning)
        msgbox.setStandardButtons(QMessageBox.Close)
        msgbox.exec_()

    def popupWrongInput(self, title, text):
        msgbox = QMessageBox()
        msgbox.setWindowTitle(title)
        msgbox.setText(text)
        msgbox.setIcon(QMessageBox.Critical)
        msgbox.setInformativeText("See help in the lower right corner")
        msgbox.setStandardButtons(QMessageBox.Close)
        msgbox.exec_()

    def popupGetHelp(self):
        msgbox = QMessageBox()
        msgbox.setWindowTitle("Help")
        msgbox.setText("The application returns a solution (if there is any) for a\nvalid input combination.\n\nAn input combination is valid, when both input field\ncontains only digits (no input is invalid), and the length\nof the puzzle is equal to the following formula:\n\n\t PUZZLE = (SIZE+1) * (SIZE+2)\n\nWhen the inputs are correct, 'Create puzzle' button will\ncreate the puzzle, and the 'Solve puzzle' button will be\nenabled to find a solution (if there is any).\n\nSample puzzles can be accessed after pressing\n'Samples' button.")
        msgbox.setStandardButtons(QMessageBox.Close)
        msgbox.setStyleSheet("QLabel{min-width: 300px;min-height: 400px;}")
        msgbox.exec_()

    def showSamples(self):
        msgbox = QMessageBox()
        msgbox.setWindowTitle("Samples")
        msgbox.setStandardButtons(QMessageBox.Close)
        msgbox.setStyleSheet("QLabel{min-width: 700px;min-height: 400px;}")
        textLabel = QtWidgets.QLabel(msgbox)
        textLabel.setText("You can copy any of the following puzzles and paste it into the 'Puzzle' input field on the main screen. Don't forget to specify the puzzle's size!")
        textLabel.setGeometry(QtCore.QRect(10, 15, 10, 100))
        textLabel.setAlignment(QtCore.Qt.AlignTop)
        textBrowser = QtWidgets.QTextBrowser(msgbox)
        textBrowser.setGeometry(QtCore.QRect(10, 40, 720, 370))
        textBrowser.setText("Size 1: \n110100\n")
        textBrowser.append("Size 2: \n222010211001\n")
        textBrowser.append("Size 3: \n23011002310331222031\n")
        textBrowser.append("Size 4: \n442143204010331203111403032422\n")
        textBrowser.append("Size 5: \n101025242443314315500445450253021123520331\n")
        textBrowser.append("Size 6: \n35066204314543061200436565613630252524212152634411400351\n")
        textBrowser.append("Size 7: \n431117274256062207417300353423366632627151475007032575704163554512664401\n")
        textBrowser.append("Size 8: \n553845366848211624483527800373771603261164752000338711558481222556047147314536402708662780\n")
        textBrowser.append("Size 9: \n07143609705004420450893718599318316683156643579821761537966747296619342183447922062295230814803259547885518072\n")
        msgbox.exec_()


def main():
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = UI(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())


if __name__ == '__main__':
    main()