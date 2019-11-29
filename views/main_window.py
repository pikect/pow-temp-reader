# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.ApplicationModal)
        Form.setFixedSize(352, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/resources/Netico-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.push_close = QtWidgets.QPushButton(Form)
        self.push_close.setGeometry(QtCore.QRect(250, 240, 91, 28))
        self.push_close.setObjectName("push_close")
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 60, 331, 141))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setKerning(True)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(5)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber.setProperty("value", "-12.1")
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_logo = QtWidgets.QLabel(Form)
        self.label_logo.setGeometry(QtCore.QRect(10, 220, 211, 61))
        self.label_logo.setObjectName("label_logo")
        self.label_temp_value = QtWidgets.QLabel(Form)
        self.label_temp_value.setGeometry(QtCore.QRect(10, 20, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_temp_value.setFont(font)
        self.label_temp_value.setObjectName("label_temp_value")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Point on Wave Temperature Sensor"))
        self.push_close.setText(_translate("Form", "Close"))
        self.label_logo.setText(_translate("Form", "<html><head/><body><p><img src=\"./resources/Netico-Group-Logo.png\"/></p></body></html>"))
        self.label_temp_value.setText(_translate("Form", "Temperature value:"))
