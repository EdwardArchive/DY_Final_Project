import sys
import os
import json
from PathInfo import PathInfo
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import uic

pathinfo = PathInfo()

class DragDialog(QDialog,pathinfo.drag_class):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)