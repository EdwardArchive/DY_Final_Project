import sys
import os
import json
import pyduinocli
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import uic

## Pyduinocli PATH
arduino = pyduinocli.Arduino("/home/kbj/local/bin/arduino-cli")

## UI PATH
print(os.getcwd())
pathfile=os.getcwd()
ui_path = os.path.dirname(os.path.abspath("/home/kbj/Project/test/qt_test1/ui/"))
ui_path2 = os.path.join(pathfile,"test/qt_test1")
form_class = uic.loadUiType(os.path.join(ui_path2, "ui/main_window.ui"))[0]
dig_class = uic.loadUiType(os.path.join(ui_path2, "ui/widget.ui"))[0]
drag_class = uic.loadUiType(os.path.join(ui_path2, "ui/dragdrop.ui"))[0]

print(form_class)
print(drag_class)
class Code_dialog(QDialog,dig_class):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buttonBox.button(QDialogButtonBox.Save).clicked.connect(self.save_clicked)

    def save_clicked(self):
        mytext = self.codetext.toPlainText()
        with open('/home/kbj/Project/test/somefile/somefile.ino', 'w') as f:
            f.write(mytext)
        try:
            res=dict(arduino.compile(sketch="/home/kbj/Project/test/somefile/somefile.ino",fqbn="arduino:avr:uno",port="/dev/ttyACM0",clean=True,verify=True,upload=True))
            if json.loads(res['__stdout'])['success'] == False :
                print(res['__stdout'])
                print(json.loads(res['__stdout'])['success'])
                QMessageBox.about(self,"message","complie Fail!")
                
            elif json.loads(res['__stdout'])['success'] == True :
                QMessageBox.about(self,"message","complie done!")
            else :
                print(json.loads(res['__stdout'])['success'])
                QMessageBox.about(self,"message","complie Non")
        except:
            QMessageBox.about(self,"message","code error!")
        

    def ok_callback(self):
        print("OK")
        self.close()

    def cancel_callback(self):
        print("Cancel")
        self.close()

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
        QMessageBox.about(self,"message","codedialog_open")
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