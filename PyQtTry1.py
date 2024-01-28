from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from PyQt5 import QtGui
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(400, 150, 1200, 900)
        self.setWindowTitle("workFluent")


        #self.initUI()
    #def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Meet Bee-yonce!")
        self.label.setFont(QtGui.QFont('Helvetica', 24))
        self.label.move(415, 50)
        self.label.adjustSize()

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Direct Translation")
        self.b1.move(360, 150)
        #self.b1.clicked.connect(self.b1clicked)
        #self.b1.adjustSize()

        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("Phrase Suggestion")
        self.b2.move(760, 150)
        #self.b2.clicked.connect(self.b2clicked)
        #self.b2.adjustSize()

        self.entry = QtWidgets.QLineEdit(self) 
        self.entry.setObjectName("name_field")
        #self.entry.setText("Enter your desired language here:")
        self.entry.adjustSize()
        self.entry.move(500, 200)

        self.b3 = QtWidgets.QPushButton(self)
        self.b3.setText("Done")
        self.b3.move(600, 250)


        self.b1.clicked.connect(self.b1clicked)
        self.b1.adjustSize()
        self.b2.clicked.connect(self.b2clicked)
        self.b2.adjustSize()
        self.b3.clicked.connect(self.b3clicked)
        self.b3.adjustSize()
       

    def b1clicked(self):
        self.label.setText("Enter Phrase:")
        self.update()
        print("direct translation")
        #self.entry = QtWidgets.QLineEdit(self) 
        #self.entry.setObjectName("name_field")
        #self.entry.setText("Enter your desired phrase here:")
        #self.entry.adjustSize()
        #self.entry.move(500, 200)
    
    def b2clicked(self):
        self.label.setText("enter topic:")
        self.update()
        print("phrase suggestions")
        #self.entry = QtWidgets.QLineEdit(self) 
        #self.entry.setObjectName("name_field")
        #self.entry.setText("Enter your topic of interest here:")
        #self.entry.adjustSize()
        #self.entry.move(500, 200)

    def b3clicked(self):
        print(f'{self.entry.text()}')
        #resetting entry box
        self.entry.clear()
        #enter language
        self.label.setText("Enter Language:")
        self.label.adjustSize()
        
        #self.label.setText(f'here are phrases in {self.entry.text()}')
        
        #language = self.entry.text()
        #print(f"Language entered: {language}")
        #print("word")


    def update(self):
        self.label.adjustSize()





def window():
    app = QApplication(sys.argv)
    win = MainWindow()
    

    win.show()
    sys. exit(app.exec_())

window()