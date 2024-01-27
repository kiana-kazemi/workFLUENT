
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(400, 150, 1200, 900)
        self.setWindowTitle("workFluent")
        self.initUI()
    
    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("meet bee-yonce!")
        self.label.setFont(QtGui.QFont('Helvetica', 24))
        self.label.move(415, 50)
        self.label.adjustSize()

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Direct Translation")
        self.b1.move(360, 150)
        self.b1.clicked.connect(self.b1clicked)
        self.b1.adjustSize()

        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("Phrase Suggestion")
        self.b2.move(760, 150)
        self.b2.adjustSize()
        self.b2.clicked.connect(self.b2clicked)

    def b1clicked(self):
        self.label.setText("enter phrase:")
        self.update()
        print("direct translation")
    
    def b2clicked(self):
        self.label.setText("enter topic:")
        self.update
        print("phrase suggestions")

    def update(self):
        self.label.adjustSize()





def b1clicked():
    print("direct translation")

def b2clicked():
    print("phrase suggestions")

def window():
    app = QApplication(sys.argv)
    win = Window()
    

    win.show()
    sys. exit(app.exec_())

window()