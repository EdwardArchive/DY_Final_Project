import os
from PyQt5 import uic
import pyduinocli

class PathInfo :
    ## UI PATH
    pathfile=os.getcwd()
    ui_path = os.path.dirname(os.path.abspath("/home/kbj/Project/test/qt_test1/ui/"))
    ui_path2 = os.path.join(pathfile,"test/qt_test1")
    main_ui = uic.loadUiType(os.path.join(ui_path2, "ui/main_window.ui"))[0]
    code_ui = uic.loadUiType(os.path.join(ui_path2, "ui/widget.ui"))[0]
    sketch_ui = uic.loadUiType(os.path.join(ui_path2, "ui/dragdrop.ui"))[0]

    ## Pyduinocli PATH
    arduino = pyduinocli.Arduino("/home/kbj/Program/arduino-cli")

    ##Arduino
    ino_path=os.path.join(pathfile,"test/somefile/somefile.ino")
