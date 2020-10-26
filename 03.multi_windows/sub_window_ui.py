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
        self.pushButton.setGeometry(QtCore.QRect(130, 75, 124, 44))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(SubWindow)
        QtCore.QMetaObject.connectSlotsByName(SubWindow)

    def retranslateUi(self, SubWindow):
        _translate = QtCore.QCoreApplication.translate
        SubWindow.setWindowTitle(_translate("SubWindow", "サブウィンドウ"))
        self.pushButton.setText(_translate("SubWindow", "閉じる"))

