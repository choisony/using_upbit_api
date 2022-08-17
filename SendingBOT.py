import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class upbit_sender(QMainWindow):

    def __init__(self):
        super().__init__()
        self.time = QDateTime.currentDateTime()
        self.initUI()

    def initUI(self):
        label1 = QLabel('Label1', self)
        label1.move(20, 20)
        label2 = QLabel('Label2', self)
        label2.move(20, 60)

        btn1 = QPushButton('Button1', self)
        btn1.move(80, 13)
        btn2 = QPushButton('Button2', self)
        btn2.move(80, 53)


        self.statusBar().showMessage(self.time.toString(Qt.DefaultLocaleLongDate))
        btn = QPushButton("Exit",self)
        btn.move(700,350)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)
        # btn.setToolTip('This is a <b>Exit</b> button')
        # self.statusBar().showMessage('Ready')
        self.setWindowTitle('Upbit Sender')
        self.setGeometry(300,300,800,400) # self.move(300, 300) # self.resize(800, 400)
        self.setWindowIcon(QIcon("upbit.png"))
        self.show()



if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = upbit_sender()
   sys.exit(app.exec_())
