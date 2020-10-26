# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sub_window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SubWindow(object):
    def setupUi(self, SubWindow):
        SubWindow.setObjectName("SubWindow")
        SubWindow.resize(400, 200)
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK JP")
        SubWindow.setFont(font)
        self.pushButton = QtWidgets.QPushButton(SubWindow)
        self.pushButton.setGeometry(QtCore.QRect(130, 140, 128, 44))
        self.pushButton.setObjectName("pushButton")
        self.radioButton = QtWidgets.QRadioButton(SubWindow)
        self.radioButton.setGeometry(QtCore.QRect(20, 70, 162, 38))
        self.radioButton.setObjectName("radioButton")
        self.buttonGroup = QtWidgets.QButtonGroup(SubWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(SubWindow)
        self.radioButton_2.setGeometry(QtCore.QRect(155, 70, 162, 38))
        self.radioButton_2.setObjectName("radioButton_2")
        self.buttonGroup.addButton(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(SubWindow)
        self.radioButton_3.setGeometry(QtCore.QRect(290, 70, 162, 38))
        self.radioButton_3.setObjectName("radioButton_3")
        self.buttonGroup.addButton(self.radioButton_3)

        self.retranslateUi(SubWindow)
        QtCore.QMetaObject.connectSlotsByName(SubWindow)

    def retranslateUi(self, SubWindow):
        _translate = QtCore.QCoreApplication.translate
        SubWindow.setWindowTitle(_translate("SubWindow", "選択画面"))
        self.pushButton.setText(_translate("SubWindow", "OK"))
        self.radioButton.setText(_translate("SubWindow", "緑色"))
        self.radioButton_2.setText(_translate("SubWindow", "黄色"))
        self.radioButton_3.setText(_translate("SubWindow", "青色"))

