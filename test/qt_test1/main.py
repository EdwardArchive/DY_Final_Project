import sys
import os
import json
from PathInfo import PathInfo
from CodeDialog import CodeDialog
from DragDialog import DragDialog
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import uic

pathinfo = PathInfo()

class MyWindow(QMainWindow, pathinfo.main_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.open_btn.clicked.connect(self.btn_clicked)
        self.open_btn2.clicked.connect(self.btn2_clicked)
        self.serial_btn.clicked.connect(self.serial_clicked)

    def btn_clicked(self):
        mydilog = CodeDialog()
        mydilog.exec_()

    def btn2_clicked(self):
        mydilog2 = DragDialog()
        mydilog2.exec_()

    def serial_clicked(self):
        os.system('sudo putty /dev/ttyACM0 -serial -sercfg 9600,8,n,1,N')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()