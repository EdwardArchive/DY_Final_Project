import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import uic

ui_path = os.path.dirname(os.path.abspath("/home/kbj/Project/test/qt_test1/ui/"))
form_class = uic.loadUiType(os.path.join(ui_path, "ui/main_window.ui"))[0]
dig_class = uic.loadUiType(os.path.join(ui_path, "ui/widget.ui"))[0]

print(form_class)
class Code_dialog(QDialog,dig_class):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.open_btn.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        QMessageBox.about(self,"message","clicked")
        mydilog = Code_dialog()
        mydilog.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()