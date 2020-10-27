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
        self.piece = QtGui.QPixmap('../images/piece_v2_776_636.png')

        #  駒のサイズ
        piece_sizex = 97
        piece_sizey = 106

        # 切り取る画像の始点 (先手の王)
        self.crop_posx = piece_sizex * 0
        self.crop_posy = piece_sizey * 1
        # 切り取る画像の始点 (先手の龍)
        #self.crop_posx = piece_sizex * 6
        #self.crop_posy = piece_sizey * 4
        # 切り取る画像の範囲
        self.crop_width = piece_sizex
        self.crop_height = piece_sizey

        # 切り取った画像を表示する
        self.cropImage()

        # 切り取った画像の場所を標準出力する
        label2_posx = self.label_2.x()
        label2_posy = self.label_2.y()
        print('x:', label2_posx)
        print('y:', label2_posy)

        # 切り取った画像を上に1マス移動する
        self.label_2.move(label2_posx, label2_posy - piece_sizey * 1 - 1)

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

