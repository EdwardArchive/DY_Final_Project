import sys
import os
import json
from PathInfo import PathInfo
from Convert import Convert 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QMimeData
from PyQt5 import QtGui,QtCore
from PyQt5 import uic

pathinfo = PathInfo()

class DragDialog(QDialog,pathinfo.sketch_ui):
    
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        label_example = QLabel("Select your Command items")
        label_favorite = QLabel("Drag-and-drop above items to below")

        ledon_icon = QIcon("/home/kbj/문서/DY_Final_Project/test/qt_test1/res/PNG/led-off.png")
        ledoff_icon = QIcon("/home/kbj/문서/DY_Final_Project/test/qt_test1/res/PNG/led-on.png")
        sleep_icon = QIcon("./res/PNG/time-to-sleep.png")

        ledon_item = QListWidgetItem(ledon_icon, "LED_ON")
        ledoff_item = QListWidgetItem(ledoff_icon, "LED_OFF")
        sleep_item = QListWidgetItem(sleep_icon, "Sleep")

        self.list_example = QListWidget()
        self.list_example.addItem(ledon_item)
        self.list_example.addItem(ledoff_item)
        self.list_example.addItem(sleep_item)

        self.list_favorite = QListWidget()

        self.list_example.setDragEnabled(True)
        self.list_favorite.setAcceptDrops(True)

        lineedit = QLineEdit()
        button_name_change = QPushButton("Add Option")

        button_remove = QPushButton("Remove")
        button_apply = QPushButton("Apply")

        button_remove.clicked.connect(self.remove_selected_item)
        button_apply.clicked.connect(self.apply)

        button_layout = QHBoxLayout()
        button_layout.addWidget(button_remove)
        button_layout.addWidget(button_apply)

        layout.addWidget(label_favorite)
        layout.addWidget(self.list_favorite)
        layout.addWidget(self.list_example)

        layout.addWidget(label_example)
        layout.addWidget(button_name_change)
        layout.addLayout(button_layout)
        self.setLayout(layout)
        self.resize(300,600)
        self.show()

    def remove_selected_item(self):
        reply = QMessageBox.question(self, "Question", "Are you sure to remove selected item?", QMessageBox.Yes | QMessageBox.No,
                                           QMessageBox.No)
        if reply == QMessageBox.Yes:
            for item in self.list_favorite.selectedItems():
                row = self.list_favorite.row(item)
                self.list_favorite.takeItem(row)
    
    def apply(self):
        lw = self.list_favorite
        # let lw haven elements in it.
        items = []
        for x in range(lw.count()):
            items.append(lw.item(x).text())
        print(items)
        converter = Convert(items)
        print(converter.Converter())

        QMessageBox.about(self,"message","done!")