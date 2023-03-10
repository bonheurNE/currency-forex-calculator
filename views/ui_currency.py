# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'currency.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)
from model.icons import icon_rc

class Ui_currency_mode_widget(object):
    def setupUi(self, currency_mode_widget):
        if not currency_mode_widget.objectName():
            currency_mode_widget.setObjectName(u"currency_mode_widget")
            currency_mode_widget.setStyleSheet(u"background-color:#2c2f32;")
        currency_mode_widget.resize(457, 568)
        self.gridLayout = QGridLayout(currency_mode_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.currency_title_frame = QFrame(currency_mode_widget)
        self.currency_title_frame.setObjectName(u"currency_title_frame")
        self.currency_title_frame.setStyleSheet(u"QPushButton{\n"
"background-color:transparent;\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:transparent;\n"
"border:1px solid darkgrey;\n"
"}\n"
"QLabel{\n"
"color:#00ffff;}\n"
"QLabel:hover{\n"
"color:rgb(0, 85, 127);\n"
"border:2px solid #ff8000;\n"
"	border-top-color: transparent;\n"
"border-right-color: transparent;\n"
"border-left-color: transparent;\n"
"}")
        self.currency_title_frame.setFrameShape(QFrame.StyledPanel)
        self.currency_title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.currency_title_frame)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.currency_title_icon = QPushButton(self.currency_title_frame)
        self.currency_title_icon.setObjectName(u"currency_title_icon")
        icon = QIcon()
        icon.addFile(u":/icons/MANAS_ICON.png", QSize(), QIcon.Normal, QIcon.Off)
        self.currency_title_icon.setIcon(icon)
        self.currency_title_icon.setIconSize(QSize(80, 80))

        self.horizontalLayout_19.addWidget(self.currency_title_icon)

        self.currency_title = QLabel(self.currency_title_frame)
        self.currency_title.setObjectName(u"currency_title")
        self.currency_title.setStyleSheet(u"\n"
"color:skyblue;")

        self.horizontalLayout_19.addWidget(self.currency_title, 0, Qt.AlignVCenter)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_7)


        self.gridLayout.addWidget(self.currency_title_frame, 0, 0, 1, 2)

        self.currency_convertion_frame = QFrame(currency_mode_widget)
        self.currency_convertion_frame.setObjectName(u"currency_convertion_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currency_convertion_frame.sizePolicy().hasHeightForWidth())
        self.currency_convertion_frame.setSizePolicy(sizePolicy)
        self.currency_convertion_frame.setMaximumSize(QSize(16777215, 16777215))
        self.currency_convertion_frame.setStyleSheet(u"QLabel{\n"
"background-color:transparent;\n"
"color:rgb(122, 122, 122);}\n"
"\n"
"QLabel:hover{\n"
"background-color:transparent;\n"
"color:rgb(255, 255, 255);}\n"
"QComboBox{\n"
"background-color:transparent;\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"")
        self.currency_convertion_frame.setFrameShape(QFrame.StyledPanel)
        self.currency_convertion_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.currency_convertion_frame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(2)
        self.gridLayout_7.setVerticalSpacing(13)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_20 = QSpacerItem(20, 56, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_20, 2, 0, 1, 1)

        self.verticalSpacer_22 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_22, 5, 0, 1, 1)

        self.currency_country_combo_2 = QComboBox(self.currency_convertion_frame)
        self.currency_country_combo_2.setObjectName(u"currency_country_combo_2")
        self.currency_country_combo_2.setStyleSheet(u"color:lightgrey;")
        self.currency_country_combo_2.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        self.currency_country_combo_2.setFont(font)

        self.gridLayout_7.addWidget(self.currency_country_combo_2, 4, 0, 1, 2)

        self.second_devise_label = QLabel(self.currency_convertion_frame)
        self.second_devise_label.setObjectName(u"second_devise_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.second_devise_label.sizePolicy().hasHeightForWidth())
        self.second_devise_label.setSizePolicy(sizePolicy1)
        self.second_devise_label.setMinimumSize(QSize(0, 60))
        font1 = QFont()
        font1.setPointSize(40)
        font1.setBold(False)
        self.second_devise_label.setFont(font1)

        self.gridLayout_7.addWidget(self.second_devise_label, 3, 1, 1, 1)

        self.currency_convertion_rate_label = QLabel(self.currency_convertion_frame)
        self.currency_convertion_rate_label.setObjectName(u"currency_convertion_rate_label")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(10)
        self.currency_convertion_rate_label.setFont(font2)

        self.gridLayout_7.addWidget(self.currency_convertion_rate_label, 6, 0, 1, 1)

        self.currency_symbol_1 = QLabel(self.currency_convertion_frame)
        self.currency_symbol_1.setObjectName(u"currency_symbol_1")
        font3 = QFont()
        font3.setPointSize(20)
        self.currency_symbol_1.setFont(font3)
        self.currency_symbol_1.setScaledContents(True)

        self.gridLayout_7.addWidget(self.currency_symbol_1, 0, 0, 1, 1)

        self.currency_symbol_2 = QLabel(self.currency_convertion_frame)
        self.currency_symbol_2.setObjectName(u"currency_symbol_2")
        self.currency_symbol_2.setFont(font3)
        self.currency_symbol_2.setScaledContents(True)

        self.gridLayout_7.addWidget(self.currency_symbol_2, 3, 0, 1, 1)

        self.first_devise_label = QLabel(self.currency_convertion_frame)
        self.first_devise_label.setObjectName(u"first_devise_label")
        self.first_devise_label.setMinimumSize(QSize(0, 60))
        self.first_devise_label.setFont(font1)

        self.gridLayout_7.addWidget(self.first_devise_label, 0, 1, 1, 1, Qt.AlignLeft)

        self.currency_country_combo_1 = QComboBox(self.currency_convertion_frame)
        self.currency_country_combo_1.setObjectName(u"currency_country_combo_1")
        self.currency_country_combo_1.setStyleSheet(u"color:lightgrey;")
        self.currency_country_combo_1.setMinimumSize(QSize(0, 30))
        self.currency_country_combo_1.setFont(font)

        self.gridLayout_7.addWidget(self.currency_country_combo_1, 1, 0, 1, 2)


        self.gridLayout.addWidget(self.currency_convertion_frame, 1, 0, 1, 1)

        self.currency_btns_frame = QFrame(currency_mode_widget)
        self.currency_btns_frame.setObjectName(u"currency_btns_frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.currency_btns_frame.sizePolicy().hasHeightForWidth())
        self.currency_btns_frame.setSizePolicy(sizePolicy2)
        self.currency_btns_frame.setMinimumSize(QSize(0, 0))
        self.currency_btns_frame.setStyleSheet(u"QPushButton{\n"
"color:skyblue;\n"
"background-color:rgb(6, 6, 6);\n"
"border:none;\n"
"border-color:transparent;\n"
"}\n"
"QPushButton:hover{\n"
"color:skyblue;\n"
"border:1px solid rgb(206, 206, 206);\n"
"background-color:rgb(73, 73, 73);\n"
"}")
        self.currency_btns_frame.setFrameShape(QFrame.StyledPanel)
        self.currency_btns_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.currency_btns_frame)
        self.gridLayout_8.setSpacing(2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.currency_btn4 = QPushButton(self.currency_btns_frame)
        self.currency_btn4.setObjectName(u"currency_btn4")
        self.currency_btn4.setMinimumSize(QSize(50, 50))
        self.currency_btn4.setMaximumSize(QSize(100, 100))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(14)
        self.currency_btn4.setFont(font4)

        self.gridLayout_8.addWidget(self.currency_btn4, 2, 0, 1, 1)

        self.currency_btn7 = QPushButton(self.currency_btns_frame)
        self.currency_btn7.setObjectName(u"currency_btn7")
        self.currency_btn7.setMinimumSize(QSize(50, 50))
        self.currency_btn7.setMaximumSize(QSize(100, 100))
        self.currency_btn7.setFont(font4)

        self.gridLayout_8.addWidget(self.currency_btn7, 1, 0, 1, 1)

        self.currency_btn9 = QPushButton(self.currency_btns_frame)
        self.currency_btn9.setObjectName(u"currency_btn9")
        self.currency_btn9.setMinimumSize(QSize(50, 50))
        self.currency_btn9.setMaximumSize(QSize(100, 100))
        self.currency_btn9.setFont(font4)

        self.gridLayout_8.addWidget(self.currency_btn9, 1, 3, 1, 1)

        self.currency_btn8 = QPushButton(self.currency_btns_frame)
        self.currency_btn8.setObjectName(u"currency_btn8")
        self.currency_btn8.setMinimumSize(QSize(50, 50))
        self.currency_btn8.setMaximumSize(QSize(100, 100))
        self.currency_btn8.setFont(font4)

        self.gridLayout_8.addWidget(self.currency_btn8, 1, 1, 1, 1)

        self.currency_btn3 = QPushButton(self.currency_btns_frame)
        self.currency_btn3.setObjectName(u"currency_btn3")
        self.currency_btn3.setMinimumSize(QSize(50, 50))
        self.currency_btn3.setMaximumSize(QSize(100, 100))
        self.currency_btn3.setFont(font4)

        self.gridLayout_8.addWidget(self.currency_btn3, 3, 3, 1, 1)

        self.currenct_btn_point = QPushButton(self.currency_btns_frame)
        self.currenct_btn_point.setObjectName(u"currenct_btn_point")
        self.currenct_btn_point.setMinimumSize(QSize(50, 50))
        self.currenct_btn_point.setMaximumSize(QSize(100, 100))
        self.currenct_btn_point.setFont(font4)

        self.gridLayout_8.addWidget(self.currenct_btn_point, 4, 3, 1, 1)

        self.currency_btn_delete = QPushButton(self.currency_btns_frame)
        self.currency_btn_delete.setObjectName(u"currency_btn_delete")
        self.currency_btn_delete.setMinimumSize(QSize(50, 50))
        self.currency_btn_delete.setMaximumSize(QSize(100, 100))
        self.currency_btn_delete.setFont(font4)
        self.currency_btn_delete.setStyleSheet(u"background-color:rgb(19, 19, 19);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.currency_btn_delete.setIcon(icon1)
        self.currency_btn_delete.setIconSize(QSize(22, 22))

        self.gridLayout_8.addWidget(self.currency_btn_delete, 0, 3, 1, 1)

        self.currency_btn0 = QPushButton(self.currency_btns_frame)
        self.currency_btn0.setObjectName(u"currency_btn0")
        self.currency_btn0.setMinimumSize(QSize(50, 50))
        self.currency_btn0.setMaximumSize(QSize(100, 100))
        self.currency_btn0.setFont(font4)

        self.gridLayout_8.addWidget(self.currency_btn0, 4, 1, 1, 1)

        self.currency_btn_CE = QPushButton(self.currency_btns_frame)
        self.currency_btn_CE.setObjectName(u"currency_btn_CE")
        self.currency_btn_CE.setMinimumSize(QSize(50, 50))
        self.currency_btn_CE.setMaximumSize(QSize(100, 100))
        self.currency_btn_CE.setFont(font4)
        self.currency_btn_CE.setStyleSheet(u"background-color:rgb(19, 19, 19);")

        self.gridLayout_8.addWidget(self.currency_btn_CE, 0, 1, 1, 1)

        self.currency_btn6 = QPushButton(self.currency_btns_frame)
        self.currency_btn6.setObjectName(u"currency_btn6")
        self.currency_btn6.setMinimumSize(QSize(50, 50))
        self.currency_btn6.setMaximumSize(QSize(100, 100))
        self.currency_btn6.setFont(font4)

        self.gridLayout_8.addWidget(self.currency_btn6, 2, 3, 1, 1)

        self.currency_btn2 = QPushButton(self.currency_btns_frame)
        self.currency_btn2.setObjectName(u"currency_btn2")
        self.currency_btn2.setMinimumSize(QSize(50, 50))
        self.currency_btn2.setMaximumSize(QSize(100, 100))
        self.currency_btn2.setFont(font4)

        self.gridLayout_8.addWidget(self.currency_btn2, 3, 1, 1, 1)

        self.currency_btn1 = QPushButton(self.currency_btns_frame)
        self.currency_btn1.setObjectName(u"currency_btn1")
        self.currency_btn1.setMinimumSize(QSize(50, 50))
        self.currency_btn1.setMaximumSize(QSize(100, 100))
        self.currency_btn1.setFont(font4)

        self.gridLayout_8.addWidget(self.currency_btn1, 3, 0, 1, 1)

        self.currency_btn5 = QPushButton(self.currency_btns_frame)
        self.currency_btn5.setObjectName(u"currency_btn5")
        self.currency_btn5.setMinimumSize(QSize(50, 50))
        self.currency_btn5.setMaximumSize(QSize(100, 100))
        self.currency_btn5.setFont(font4)

        self.gridLayout_8.addWidget(self.currency_btn5, 2, 1, 1, 1)


        self.gridLayout.addWidget(self.currency_btns_frame, 1, 1, 1, 1)


        self.retranslateUi(currency_mode_widget)

        QMetaObject.connectSlotsByName(currency_mode_widget)
    # setupUi

    def retranslateUi(self, currency_mode_widget):
        currency_mode_widget.setWindowTitle(QCoreApplication.translate("currency_mode_widget", u"Form", None))
        self.currency_title_icon.setText("")
        self.currency_title.setText(QCoreApplication.translate("currency_mode_widget", u"<html><head/><body><p align=\"right\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Currency Convertion</span></p></body></html>", None))
        self.second_devise_label.setText(QCoreApplication.translate("currency_mode_widget", u"0", None))
        self.currency_convertion_rate_label.setText(QCoreApplication.translate("currency_mode_widget", u"Convertion Rate", None))
        self.currency_symbol_1.setText(QCoreApplication.translate("currency_mode_widget", u"$", None))
        self.currency_symbol_2.setText(QCoreApplication.translate("currency_mode_widget", u"$", None))
        self.first_devise_label.setText(QCoreApplication.translate("currency_mode_widget", u"0", None))
        self.currency_btn4.setText(QCoreApplication.translate("currency_mode_widget", u"4", None))
        self.currency_btn7.setText(QCoreApplication.translate("currency_mode_widget", u"7", None))
        self.currency_btn9.setText(QCoreApplication.translate("currency_mode_widget", u"9", None))
        self.currency_btn8.setText(QCoreApplication.translate("currency_mode_widget", u"8", None))
        self.currency_btn3.setText(QCoreApplication.translate("currency_mode_widget", u"3", None))
        self.currenct_btn_point.setText(QCoreApplication.translate("currency_mode_widget", u".", None))
        self.currency_btn_delete.setText("")
        self.currency_btn0.setText(QCoreApplication.translate("currency_mode_widget", u"0", None))
        self.currency_btn_CE.setText(QCoreApplication.translate("currency_mode_widget", u"CE", None))
        self.currency_btn6.setText(QCoreApplication.translate("currency_mode_widget", u"6", None))
        self.currency_btn2.setText(QCoreApplication.translate("currency_mode_widget", u"2", None))
        self.currency_btn1.setText(QCoreApplication.translate("currency_mode_widget", u"1", None))
        self.currency_btn5.setText(QCoreApplication.translate("currency_mode_widget", u"5", None))
    # retranslateUi

