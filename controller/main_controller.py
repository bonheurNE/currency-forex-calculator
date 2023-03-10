from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6 import QtGui, QtCore

from views.ui_currency import *
from model import main_model

import json
import re

class MainController(QWidget):
    def __init__(self, tempDire):
        super().__init__()
        self.ui = Ui_currency_mode_widget()
        self.ui.setupUi(self)