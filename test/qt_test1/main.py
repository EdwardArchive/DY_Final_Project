import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import uic

## 차후 Path 설정에 대한것은 리눅스 윈도우 동일한 방법으로 진행할수 있도록 고민이 필요 현제 windows 버전
print(os.getcwd())
pathfile=os.getcwd()
ui_path = os.path.dirname(os.path.abspath("/home/kbj/Project/test/qt_test1/ui/"))
ui_path2 = os.path.join(pathfile,"test\qt_test1")
form_class = uic.loadUiType(os.path.join(ui_path2, "ui\main_window.ui"))[0]
dig_class = uic.loadUiType(os.path.join(ui_path2, "ui\widget.ui"))[0]
drag_class = uic.loadUiType(os.path.join(ui_path2, "ui\dragdrop.ui"))[0]

print(form_class)
print(drag_class)
class Code_dialog(QDialog,dig_class):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class drag_dialog(QDialog,drag_class):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.open_btn.clicked.connect(self.btn_clicked)
        self.open_btn2.clicked.connect(self.btn2_clicked)

    def btn_clicked(self):
        #QMessageBox.about(self,"message","clicked")
        mydilog = Code_dialog()
        mydilog.exec_()

    def btn2_clicked(self):
        mydilog2 = drag_dialog()
        mydilog2.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()