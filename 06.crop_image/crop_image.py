#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui
from image_ui import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 切り取る対象の画像
        self.piece = QtGui.QPixmap('./images/piece_v2_776_636.png')

        # 切り取る画像の始点 (先手の王)
        self.crop_posx = 97 * 0
        self.crop_posy = 106 * 1
        # 切り取る画像の始点 (先手の龍)
        #self.crop_posx = 97 * 6
        #self.crop_posy = 106 * 4
        # 切り取る画像の範囲
        self.crop_width = 97
        self.crop_height = 106

        # 切り取った画像を表示する
        self.cropImage()

    def cropImage(self):
        # 切り取る範囲
        rect = QtCore.QRect(self.crop_posx, self.crop_posy, 
                            self.crop_width, self.crop_height)
        # 切り取った画像
        crop_img = self.piece.copy(rect)
        # 切り取った画像を label_2 に代入
        self.label_2.setPixmap(crop_img)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())

