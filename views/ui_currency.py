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
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)
from model.icons import icon_rc

class Ui_currency_mode_widget(object):
    def setupUi(self, currency_mode_widget):
        if not currency_mode_widget.objectName():
            currency_mode_widget.setObjectName(u"currency_mode_widget")
        currency_mode_widget.resize(438, 568)
        currency_mode_widget.setStyleSheet(u"background-color:rgb(68, 68, 68);")
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
"color:skyblue;}\n"
"QLabel:hover{\n"
"color:rgb(0, 85, 127);\n"
"border:2px solid rgb(0, 58, 0);\n"
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
        self.currency_title.setStyleSheet(u"")

        self.horizontalLayout_19.addWidget(self.currency_title, 0, Qt.AlignVCenter)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_7)


        self.gridLayout.addWidget(self.currency_title_frame, 0, 0, 1, 2)

        self.currency_btns_frame = QFrame(currency_mode_widget)
        self.currency_btns_frame.setObjectName(u"currency_btns_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currency_btns_frame.sizePolicy().hasHeightForWidth())
        self.currency_btns_frame.setSizePolicy(sizePolicy)
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
"}\n"
"QPushButton#currency_btn_CE{\n"
"color:red;\n"
"background-color:rgb(34, 34, 34);\n"
"border:none;\n"
"border-color:transparent;\n"
"}\n"
"QPushButton#currency_btn_delete{\n"
"background-color:rgb(6, 6, 6);\n"
"border:none;\n"
"border-color:transparent;\n"
"}\n"
"QPushButton#currency_btn_CE:hover{\n"
"color:rgb(0, 180, 87);\n"
"border:1px solid rgb(206, 206, 206);\n"
"background-color:rgb(6, 6, 6);\n"
"}\n"
"QPushButton#currency_btn_delete:hover{\n"
"color:skyblue;\n"
"border:1px solid rgb(206, 206, 206);\n"
"background-color:rgb(6, 6, 6);\n"
"}\n"
"")
        self.currency_btns_frame.setFrameShape(QFrame.StyledPanel)
        self.currency_btns_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.currency_btns_frame)
        self.gridLayout_8.setSpacing(2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.currency_btn7 = QPushButton(self.currency_btns_frame)
        self.currency_btn7.setObjectName(u"currency_btn7")
        self.currency_btn7.setMinimumSize(QSize(50, 50))
        self.currency_btn7.setMaximumSize(QSize(100, 100))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(14)
        self.currency_btn7.setFont(font)

        self.gridLayout_8.addWidget(self.currency_btn7, 1, 0, 1, 1)

        self.currency_btn4 = QPushButton(self.currency_btns_frame)
        self.currency_btn4.setObjectName(u"currency_btn4")
        self.currency_btn4.setMinimumSize(QSize(50, 50))
        self.currency_btn4.setMaximumSize(QSize(100, 100))
        self.currency_btn4.setFont(font)

        self.gridLayout_8.addWidget(self.currency_btn4, 2, 0, 1, 1)

        self.currency_btn9 = QPushButton(self.currency_btns_frame)
        self.currency_btn9.setObjectName(u"currency_btn9")
        self.currency_btn9.setMinimumSize(QSize(50, 50))
        self.currency_btn9.setMaximumSize(QSize(100, 100))
        self.currency_btn9.setFont(font)

        self.gridLayout_8.addWidget(self.currency_btn9, 1, 3, 1, 1)

        self.currency_btn8 = QPushButton(self.currency_btns_frame)
        self.currency_btn8.setObjectName(u"currency_btn8")
        self.currency_btn8.setMinimumSize(QSize(50, 50))
        self.currency_btn8.setMaximumSize(QSize(100, 100))
        self.currency_btn8.setFont(font)

        self.gridLayout_8.addWidget(self.currency_btn8, 1, 1, 1, 1)

        self.currency_btn3 = QPushButton(self.currency_btns_frame)
        self.currency_btn3.setObjectName(u"currency_btn3")
        self.currency_btn3.setMinimumSize(QSize(50, 50))
        self.currency_btn3.setMaximumSize(QSize(100, 100))
        self.currency_btn3.setFont(font)

        self.gridLayout_8.addWidget(self.currency_btn3, 3, 3, 1, 1)

        self.currency_btn_point = QPushButton(self.currency_btns_frame)
        self.currency_btn_point.setObjectName(u"currency_btn_point")
        self.currency_btn_point.setMinimumSize(QSize(50, 50))
        self.currency_btn_point.setMaximumSize(QSize(100, 100))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.currency_btn_point.setFont(font1)
        self.currency_btn_point.setStyleSheet(u"background-color:rgb(121, 80, 0)")

        self.gridLayout_8.addWidget(self.currency_btn_point, 4, 3, 1, 1)

        self.currency_btn0 = QPushButton(self.currency_btns_frame)
        self.currency_btn0.setObjectName(u"currency_btn0")
        self.currency_btn0.setMinimumSize(QSize(50, 50))
        self.currency_btn0.setMaximumSize(QSize(100, 100))
        self.currency_btn0.setFont(font)

        self.gridLayout_8.addWidget(self.currency_btn0, 4, 1, 1, 1)

        self.currency_btn_delete = QPushButton(self.currency_btns_frame)
        self.currency_btn_delete.setObjectName(u"currency_btn_delete")
        self.currency_btn_delete.setMinimumSize(QSize(50, 50))
        self.currency_btn_delete.setMaximumSize(QSize(100, 100))
        self.currency_btn_delete.setFont(font)
        self.currency_btn_delete.setStyleSheet(u"background-color:rgb(19, 19, 19);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.currency_btn_delete.setIcon(icon1)
        self.currency_btn_delete.setIconSize(QSize(22, 22))

        self.gridLayout_8.addWidget(self.currency_btn_delete, 0, 3, 1, 1)

        self.currency_btn6 = QPushButton(self.currency_btns_frame)
        self.currency_btn6.setObjectName(u"currency_btn6")
        self.currency_btn6.setMinimumSize(QSize(50, 50))
        self.currency_btn6.setMaximumSize(QSize(100, 100))
        self.currency_btn6.setFont(font)

        self.gridLayout_8.addWidget(self.currency_btn6, 2, 3, 1, 1)

        self.currency_btn1 = QPushButton(self.currency_btns_frame)
        self.currency_btn1.setObjectName(u"currency_btn1")
        self.currency_btn1.setMinimumSize(QSize(50, 50))
        self.currency_btn1.setMaximumSize(QSize(100, 100))
        self.currency_btn1.setFont(font)

        self.gridLayout_8.addWidget(self.currency_btn1, 3, 0, 1, 1)

        self.currency_btn2 = QPushButton(self.currency_btns_frame)
        self.currency_btn2.setObjectName(u"currency_btn2")
        self.currency_btn2.setMinimumSize(QSize(50, 50))
        self.currency_btn2.setMaximumSize(QSize(100, 100))
        self.currency_btn2.setFont(font)

        self.gridLayout_8.addWidget(self.currency_btn2, 3, 1, 1, 1)

        self.currency_btn_CE = QPushButton(self.currency_btns_frame)
        self.currency_btn_CE.setObjectName(u"currency_btn_CE")
        self.currency_btn_CE.setMinimumSize(QSize(50, 50))
        self.currency_btn_CE.setMaximumSize(QSize(100, 100))
        self.currency_btn_CE.setFont(font)
        self.currency_btn_CE.setStyleSheet(u"background-color:rgb(19, 19, 19);")

        self.gridLayout_8.addWidget(self.currency_btn_CE, 0, 1, 1, 1)

        self.currency_btn5 = QPushButton(self.currency_btns_frame)
        self.currency_btn5.setObjectName(u"currency_btn5")
        self.currency_btn5.setMinimumSize(QSize(50, 50))
        self.currency_btn5.setMaximumSize(QSize(100, 100))
        self.currency_btn5.setFont(font)

        self.gridLayout_8.addWidget(self.currency_btn5, 2, 1, 1, 1)


        self.gridLayout.addWidget(self.currency_btns_frame, 1, 1, 1, 1)

        self.currency_convertion_frame = QFrame(currency_mode_widget)
        self.currency_convertion_frame.setObjectName(u"currency_convertion_frame")
        sizePolicy.setHeightForWidth(self.currency_convertion_frame.sizePolicy().hasHeightForWidth())
        self.currency_convertion_frame.setSizePolicy(sizePolicy)
        self.currency_convertion_frame.setMaximumSize(QSize(243, 16777215))
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

        self.gridLayout_7.addItem(self.verticalSpacer_20, 3, 0, 1, 1)

        self.verticalSpacer_22 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_22, 7, 0, 1, 1)

        self.currency_country_combo_1 = QComboBox(self.currency_convertion_frame)
        self.currency_country_combo_1.setObjectName(u"currency_country_combo_1")
        self.currency_country_combo_1.setMinimumSize(QSize(0, 30))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(12)
        self.currency_country_combo_1.setFont(font2)

        self.gridLayout_7.addWidget(self.currency_country_combo_1, 2, 0, 1, 3)

        self.currency_symbol_2 = QLabel(self.currency_convertion_frame)
        self.currency_symbol_2.setObjectName(u"currency_symbol_2")
        self.currency_symbol_2.setMaximumSize(QSize(80, 16777215))
        font3 = QFont()
        font3.setPointSize(20)
        self.currency_symbol_2.setFont(font3)
        self.currency_symbol_2.setScaledContents(True)

        self.gridLayout_7.addWidget(self.currency_symbol_2, 4, 0, 1, 1, Qt.AlignLeft)

        self.currency_convertion_rate_label = QLabel(self.currency_convertion_frame)
        self.currency_convertion_rate_label.setObjectName(u"currency_convertion_rate_label")
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(10)
        self.currency_convertion_rate_label.setFont(font4)

        self.gridLayout_7.addWidget(self.currency_convertion_rate_label, 8, 0, 1, 1)

        self.currency_symbol_1 = QLabel(self.currency_convertion_frame)
        self.currency_symbol_1.setObjectName(u"currency_symbol_1")
        self.currency_symbol_1.setMaximumSize(QSize(80, 16777215))
        self.currency_symbol_1.setFont(font3)
        self.currency_symbol_1.setScaledContents(True)

        self.gridLayout_7.addWidget(self.currency_symbol_1, 0, 0, 1, 1, Qt.AlignLeft)

        self.currency_country_combo_2 = QComboBox(self.currency_convertion_frame)
        self.currency_country_combo_2.setObjectName(u"currency_country_combo_2")
        self.currency_country_combo_2.setMinimumSize(QSize(0, 30))
        self.currency_country_combo_2.setFont(font2)

        self.gridLayout_7.addWidget(self.currency_country_combo_2, 6, 0, 1, 3)

        self.convertable_amount = QLineEdit(self.currency_convertion_frame)
        self.convertable_amount.setObjectName(u"convertable_amount")
        self.convertable_amount.setMinimumSize(QSize(0, 40))
        self.convertable_amount.setMaximumSize(QSize(16777215, 50))
        font5 = QFont()
        font5.setFamilies([u"Times New Roman"])
        font5.setPointSize(20)
        font5.setBold(False)
        font5.setItalic(False)
        self.convertable_amount.setFont(font5)
        self.convertable_amount.setStyleSheet(u"font: 20pt \"Times New Roman\";\n"
"color:lightgrey;\n"
"background-color:transparent;\n"
"border:None;")
        self.convertable_amount.setInputMethodHints(Qt.ImhNone)
        self.convertable_amount.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.convertable_amount.setReadOnly(True)

        self.gridLayout_7.addWidget(self.convertable_amount, 1, 0, 1, 1)

        self.converted_amount = QLineEdit(self.currency_convertion_frame)
        self.converted_amount.setObjectName(u"converted_amount")
        self.converted_amount.setMinimumSize(QSize(0, 40))
        self.converted_amount.setMaximumSize(QSize(16777215, 50))
        self.converted_amount.setFont(font5)
        self.converted_amount.setStyleSheet(u"font: 20pt \"Times New Roman\";\n"
"color:lightgrey;\n"
"background-color:transparent;\n"
"border:None;")
        self.converted_amount.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.converted_amount.setReadOnly(True)

        self.gridLayout_7.addWidget(self.converted_amount, 5, 0, 1, 1)


        self.gridLayout.addWidget(self.currency_convertion_frame, 1, 0, 1, 1, Qt.AlignLeft)


        self.retranslateUi(currency_mode_widget)

        QMetaObject.connectSlotsByName(currency_mode_widget)
    # setupUi

    def retranslateUi(self, currency_mode_widget):
        currency_mode_widget.setWindowTitle(QCoreApplication.translate("currency_mode_widget", u"Form", None))
        self.currency_title_icon.setText("")
        self.currency_title.setText(QCoreApplication.translate("currency_mode_widget", u"<html><head/><body><p align=\"right\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Currency Convertion</span></p></body></html>", None))
        self.currency_btn7.setText(QCoreApplication.translate("currency_mode_widget", u"7", None))
        self.currency_btn4.setText(QCoreApplication.translate("currency_mode_widget", u"4", None))
        self.currency_btn9.setText(QCoreApplication.translate("currency_mode_widget", u"9", None))
        self.currency_btn8.setText(QCoreApplication.translate("currency_mode_widget", u"8", None))
        self.currency_btn3.setText(QCoreApplication.translate("currency_mode_widget", u"3", None))
        self.currency_btn_point.setText(QCoreApplication.translate("currency_mode_widget", u".", None))
        self.currency_btn0.setText(QCoreApplication.translate("currency_mode_widget", u"0", None))
        self.currency_btn_delete.setText("")
        self.currency_btn6.setText(QCoreApplication.translate("currency_mode_widget", u"6", None))
        self.currency_btn1.setText(QCoreApplication.translate("currency_mode_widget", u"1", None))
        self.currency_btn2.setText(QCoreApplication.translate("currency_mode_widget", u"2", None))
        self.currency_btn_CE.setText(QCoreApplication.translate("currency_mode_widget", u"CE", None))
        self.currency_btn5.setText(QCoreApplication.translate("currency_mode_widget", u"5", None))
        self.currency_symbol_2.setText(QCoreApplication.translate("currency_mode_widget", u"$", None))
        self.currency_convertion_rate_label.setText(QCoreApplication.translate("currency_mode_widget", u"Convertion Rate", None))
        self.currency_symbol_1.setText(QCoreApplication.translate("currency_mode_widget", u"$", None))
#if QT_CONFIG(tooltip)
        self.convertable_amount.setToolTip(QCoreApplication.translate("currency_mode_widget", u"Enter the amount to convert", None))
#endif // QT_CONFIG(tooltip)
        self.convertable_amount.setText("")
        self.convertable_amount.setPlaceholderText(QCoreApplication.translate("currency_mode_widget", u"0.0", None))
#if QT_CONFIG(tooltip)
        self.converted_amount.setToolTip(QCoreApplication.translate("currency_mode_widget", u"converted amount", None))
#endif // QT_CONFIG(tooltip)
        self.converted_amount.setText("")
        self.converted_amount.setPlaceholderText(QCoreApplication.translate("currency_mode_widget", u"0.0", None))
    # retranslateUi

