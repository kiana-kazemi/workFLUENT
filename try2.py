from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from PyQt5 import QtGui
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        #set up the GUI
        self.setGeometry(400, 150, 500, 800)
        self.setWindowTitle("workFluent")
        self.setStyleSheet("background-color: lightblue;")

        #set up initial label
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Meet Bee-yonce!")
        self.label.setFont(QtGui.QFont('Cambria', 18))
        self.label.move(50, 50)
        self.label.adjustSize()

        #TODO: add description of bee-yonce

        #bee's first message to the user
        self.q1 = QtWidgets.QLabel(self)
        self.q1.setText("Direct Translation or Phrase Suggestions:")
        #self.q1.setText("Would you like a direct translation \nor phrase suggestions? \nEnter Translation or Phrase below")
        #self.q1.setFont(QtGui.QFont('Helvetica', 12))
        self.q1.adjustSize()
        self.q1.move(25, 150)

        self.enter1 = QtWidgets.QLineEdit(self)
        self.enter1.setObjectName("ans1")
        self.enter1.adjustSize()
        self.enter1.move(300, 150)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Done")
        self.b1.move(300, 180)

        self.q2 = QtWidgets.QLabel(self)
        self.q2.setText("Phrase or Topic:")
        #self.q2.setText("If you selected translation,\nenter the phrase you want translated, \nif you selected Phrase, \nenter the desired topic.")
        #self.q2.setFont(QtGui.QFont('Helvetica', 12))
        self.q2.adjustSize()
        self.q2.move(25, 250)

        self.enter2 = QtWidgets.QLineEdit(self)
        self.enter2.setObjectName("ans2")
        self.enter2.adjustSize()
        self.enter2.move(300, 250)

        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("Done")
        self.b2.move(300, 280)

        self.q3 = QtWidgets.QLabel(self)
        self.q3.setText("Please enter your target language:")
        #self.q3.setFont(QtGui.QFont('Helvetica', 12))
        self.q3.adjustSize()
        self.q3.move(25, 350)

        self.enter3 = QtWidgets.QLineEdit(self)
        self.enter3.setObjectName("ans3")
        self.enter3.adjustSize()
        self.enter3.move(300, 350)

        self.b3 = QtWidgets.QPushButton(self)
        self.b3.setText("Done")
        self.b3.move(300, 380)

        self.b4 = QtWidgets.QPushButton(self)
        self.b4.setText("Reset")
        self.b4.move(210, 450)

        self.b1.clicked.connect(self.b1clicked)
        self.b2.clicked.connect(self.b2clicked)
        self.b3.clicked.connect(self.b3clicked)
        self.b4.clicked.connect(self.b4clicked)



    def b1clicked(self):
        print(f'{self.enter1.text()}')

    def b2clicked(self):
        print(f'{self.enter2.text()}')

    def b3clicked(self):
        print(f'{self.enter3.text()}')

    def b4clicked(self):
        self.enter1.clear()
        self.enter2.clear()
        self.enter3.clear()




def window():
    app = QApplication(sys.argv)
    win = MainWindow()
    

    win.show()
    sys. exit(app.exec_())

window()