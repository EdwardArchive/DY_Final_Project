from PathInfo import PathInfo
import sys
import os
import json
import pyduinocli
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import uic

pathinfo = PathInfo()


class CodeDialog(QDialog,pathinfo.code_ui):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buttonBox.button(QDialogButtonBox.Save).clicked.connect(self.save_clicked)
        try :
            with open(pathinfo.ino_path, 'r') as f:
                self.codetext.append(f.read())
        except Exception as e:
            print(pathinfo.ino_path,e)
            QMessageBox.about(self,"message","file error!")

    def save_clicked(self):
        mytext = self.codetext.toPlainText()
        with open(pathinfo.ino_path, 'w') as f:
            f.write(mytext)
        try:
            res=dict(pathinfo.arduino.compile(sketch=pathinfo.ino_path,fqbn="arduino:avr:uno",port="/dev/ttyACM0",clean=True,verify=True,upload=True))
            if json.loads(res['__stdout'])['success'] == False :
                print(res['__stdout'])
                print(json.loads(res['__stdout'])['success'])
                QMessageBox.about(self,"message","complie Fail!")
                
            elif json.loads(res['__stdout'])['success'] == True :
                QMessageBox.about(self,"message","complie done!")
            else :
                print(json.loads(res['__stdout'])['success'])
                QMessageBox.about(self,"message","complie Non")

        except Exception as e:
            print(pathinfo.ino_path,e)
            QMessageBox.about(self,"message","code error!")
        

    def ok_callback(self):
        print("OK")
        self.close()

    def cancel_callback(self):
        print("Cancel")
        self.close()
