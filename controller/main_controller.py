from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6 import QtGui, QtCore
from PySide6.QtGui import QDoubleValidator

from views.ui_currency import *
from model import main_model

import json
import re
import time

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
        #self.setFixedWidth(400)
        # manage combobox completion
        self.manageComboBoxCompletion()
        # manage buttons action on entries
        self.manageButtonsAction()
        
        
    def initializeVariables(self):
        self._availableCountriesCurrencies = {}
        self._preview_amount = 0.0
        
    def setUpWidget(self):
        self.ui.currency_country_combo_1.setFixedWidth(150)
        self.ui.currency_country_combo_2.setFixedWidth(150)
        
        # manage validation for entries
        # create validator 
        double_validator = QDoubleValidator()
        
        # set validator to entries
        self.ui.convertable_amount.setValidator(double_validator)
        self.ui.converted_amount.setValidator(double_validator)
        
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
        
        
        # get different data entered
        current_first_value = self.ui.convertable_amount.text()
        current_first_value = current_first_value.strip()
        current_first_value = float(current_first_value)
        
        # convert
        returned_value = main_model.convertForex(amount=current_first_value, from_c=current_currency_1, to_c=current_currency_2)
        
        amount_str = returned_value[2] 
        
        amount = str(amount_str)
        
        # create the string to use for printing the rate change
        rate = f"{returned_value[0]}\n{returned_value[1]}"
        # print the str in the specific label
        self.ui.currency_convertion_rate_label.setText(rate)
        # set the converted amount to the label
        self.ui.converted_amount.setText(amount)
        self._preview_amount = current_first_value
        print(f"preview on forex {self._preview_amount}")
        pass
    
    def completEntry(self, number:int=0) -> None:
        # convert the bnt into text
        btn_number_text = str(number)
        # get the current text on the entry
        current_text = self.ui.convertable_amount.text()
        current_text = current_text.strip()
        
        print(f"preview on button {self._preview_amount}")
        
        print(f"current text on button {current_text}")
        
        
        if current_text == "0.0" or current_text == "":
            # clear the entry
            self.ui.convertable_amount.setText(f"{btn_number_text}")
             
            pass
        elif float(current_text) == float(self._preview_amount):
            # clear and set the clicked button value to the entry
            print("check")
            self.ui.convertable_amount.clear()
            self.ui.convertable_amount.setText(f"{btn_number_text}")
        
        else:
            new_text = f"{current_text}{btn_number_text}"
            self.ui.convertable_amount.setText(new_text)
        
    def completEntrySpecial(self,btn:str="")->None:
        button_value = btn
        
        # get the current value of the entry
        current_text = self.ui.convertable_amount.text()
        current_text = current_text.strip()
        
        if button_value == "point":
            if current_text == "":
                # if the entry is empty set 0. to the entry
                new_text = "0."
                self.ui.convertable_amount.setText(new_text)
                pass
            elif "." in current_text:
                pass
            else:
                new_text = f"{current_text}."
                self.ui.convertable_amount.setText(new_text)
                pass
        elif button_value == "CE":
            # clear the entry and reset the preview number variable
            self.ui.convertable_amount.clear()
            self.ui.converted_amount.clear()
            self._preview_amount = 0.0
            
            pass
        elif button_value == "delete":
            # check if the current text is not empty
            if current_text == "":
                pass
            else:
                # remove the last character from the current text on the entry
                new_text = current_text[:-1]
                # set the new text to the entry
                self.ui.convertable_amount.setText(new_text)
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
    
    def manageButtonsAction(self):
        
        ###########################
        # NUMBERS BUTTONS ACTIONS #
        ###########################
        self.ui.currency_btn0.clicked.connect(lambda:self.completEntry(number=0))
        self.ui.currency_btn1.clicked.connect(lambda:self.completEntry(number=1))
        self.ui.currency_btn2.clicked.connect(lambda:self.completEntry(number=2))
        self.ui.currency_btn3.clicked.connect(lambda:self.completEntry(number=3))
        self.ui.currency_btn4.clicked.connect(lambda:self.completEntry(number=4))
        self.ui.currency_btn5.clicked.connect(lambda:self.completEntry(number=5))
        self.ui.currency_btn6.clicked.connect(lambda:self.completEntry(number=6))
        self.ui.currency_btn7.clicked.connect(lambda:self.completEntry(number=7))
        self.ui.currency_btn8.clicked.connect(lambda:self.completEntry(number=8))
        self.ui.currency_btn9.clicked.connect(lambda:self.completEntry(number=9))
        
        ############################
        # SPECIALS BUTTONS ACTIONS #
        ############################
        self.ui.currency_btn_point.clicked.connect(lambda:self.completEntrySpecial(btn="point"))
        self.ui.currency_btn_CE.clicked.connect(lambda:self.completEntrySpecial(btn="CE"))
        self.ui.currency_btn_delete.clicked.connect(lambda:self.completEntrySpecial(btn="delete"))
        
    ############################
    # KEYS EVENTS      ACTIONS #
    ############################
    def keyPressEvent(self, event) -> None:
        ###########################
        # NUMBERS BUTTONS ACTIONS #
        ###########################
        
        if event.key() == Qt.Key.Key_0:
            self.completEntry(number=0)
        elif event.key() == Qt.Key.Key_1:
            self.completEntry(number=1)
        elif event.key() == Qt.Key.Key_2:
            self.completEntry(number=2)
        elif event.key() == Qt.Key.Key_3:
            self.completEntry(number=3)
        elif event.key() == Qt.Key.Key_4:
            self.completEntry(number=4)
        elif event.key() == Qt.Key.Key_5:
            self.completEntry(number=5)
        elif event.key() == Qt.Key.Key_6:
            self.completEntry(number=6)
        elif event.key() == Qt.Key.Key_7:
            self.completEntry(number=7)
        elif event.key() == Qt.Key.Key_8:
            self.completEntry(number=8)
        elif event.key() == Qt.Key.Key_9:
            self.completEntry(number=9)
        
        ############################
        # SPECIALS BUTTONS ACTIONS #
        ############################
        elif event.key() == Qt.Key.Key_Period or event.key() == Qt.Key.Key_Comma:
            self.completEntrySpecial(btn="point")
        elif event.key() == Qt.Key.Key_Delete or event.key() == Qt.Key.Key_C:
            self.completEntrySpecial(btn="CE")
        elif event.key() == Qt.Key.Key_Backspace:
            self.completEntrySpecial(btn="delete")
           