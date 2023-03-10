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
        
        self._temp_dir = tempDire
        
        # initialise all variable ww will use
        self.initializeVariables()
        # setup the widget
        self.setUpWidget()
        # manage models
        self.modelManager()
        
        # manage combobox completion
        self.manageComboBoxCompletion()
        
        
    def initializeVariables(self):
        self._availableCountriesCurrencies = {}
        
    def setUpWidget(self):
        self.ui.currency_country_combo_1.setFixedWidth(150)
        self.ui.currency_country_combo_2.setFixedWidth(150)
        
    def modelManager(self):
        # create the currency calculator folder for external data
        main_model.softwareFolderCreation()
        
        # create the json files for avaiable currencies code and counrty 
        main_model.createAvailableCurrencyFiles(self._temp_dir)
        
        self._availableCountriesCurrencies = main_model.getCurrenciesData(self._temp_dir)
        
    
    def calculateForex(self):
        # get the current text on the first and second combo 
        current_text_1 = self.ui.currency_country_combo_1.currentText()
        current_text_2 = self.ui.currency_country_combo_2.currentText()
        
        current_currency_1 = current_text_1[:3]
        current_currency_1 = current_currency_1.strip()
        
        current_currency_2 = current_text_2[:3]
        current_currency_2 = current_currency_2.strip()
        
        # set the currency code to the currency_symbol_1
        self.ui.currency_symbol_1.setText(current_currency_1)
        # set the currency code to the currency_symbol_2
        self.ui.currency_symbol_2.setText(current_currency_2)
        pass
    
    def manageComboBoxCompletion(self):
        # organise currency data
        data = []
        # get a list of all values on the json dict
        values__ = list(self._availableCountriesCurrencies.values())
        
        # link country and currency code 
        for value_ in values__:
            # form string containing currency_code currency_name county_name 
            currency_str = f"{value_['currency']} {value_['currency_name']} {value_['currency_country']}" 
            # appending the str into the data list
            data.append(currency_str)
            
            
        
        # complet comboboxes
        self.ui.currency_country_combo_1.addItems(data)
        self.ui.currency_country_combo_2.addItems(data)
        
        
        # get the currency selected
        self.ui.currency_country_combo_1.currentIndexChanged.connect(lambda:self.calculateForex())
        self.ui.currency_country_combo_2.currentIndexChanged.connect(lambda:self.calculateForex())
    