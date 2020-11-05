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

        # マウスがクリックされているか
        self.isclicked = False

        # 切り取る対象の画像
        self.piece = QtGui.QPixmap('../images/piece_v2_776_636.png')

        #  駒のサイズ
        self.piece_sizex = 97
        self.piece_sizey = 106

        # ９一のマス目の左上の座標
        self.minx = 34
        self.miny = 34

        # 切り取る画像の始点 (先手の王)
        self.crop_posx = self.piece_sizex * 0
        self.crop_posy = self.piece_sizey * 1
        # 切り取る画像の始点 (先手の龍)
        #self.crop_posx = self.piece_sizex * 6
        #self.crop_posy = self.piece_sizey * 4
        # 切り取る画像の範囲
        self.crop_width = self.piece_sizex
        self.crop_height = self.piece_sizey

        # 切り取った画像を表示する
        self.cropImage()

        # 駒の場所を標準出力する
        #print('x:', self.label_2.x())
        #print('y:', self.label_2.y())

    def cropImage(self):
        # 切り取る範囲
        rect = QtCore.QRect(self.crop_posx, self.crop_posy, 
                            self.crop_width, self.crop_height)
        # 切り取った画像
        crop_img = self.piece.copy(rect)
        # 切り取った画像を label_2 に代入
        self.label_2.setPixmap(crop_img)

    def mousePressEvent(self, event):
        # 左クリックした
        if event.button() == QtCore.Qt.LeftButton:
            print('Left Button')

            # マウスカーソルの場所を取得する
            mouseposx = event.pos().x()
            mouseposy = event.pos().y()

            # マウスカーソルが駒の範囲内にあるか判定
            if mouseposx >= self.label_2.x() and \
               mouseposx <= self.label_2.x() + self.piece_sizex - 1 and \
               mouseposy >= self.label_2.y() and \
               mouseposy <= self.label_2.y() + self.piece_sizey - 1:
                   print('駒の範囲内')
                   self.isclicked = True

    def mouseMoveEvent(self, event):
        if self.isclicked:
            print('マウス移動',event.pos())

            # マウスカーソルの場所を取得する
            mousePosX = event.pos().x()
            mousePosY = event.pos().y()

            # 駒の中心をマウスカーソルの場所に指定する
            centerPosX = mousePosX - self.piece_sizex/2
            centerPosY = mousePosY - self.piece_sizey/2

            # 駒を移動する
            self.label_2.move(centerPosX, centerPosY)

    def mouseReleaseEvent(self, event):
        if self.isclicked:
            print('マウスリリース')
            self.isclicked = False

            # 駒の中心位置
            centerPosX = self.label_2.x() + self.piece_sizex/2
            centerPosY = self.label_2.y() + self.piece_sizey/2

            # 駒の中心がどのマスの中にいるか確認する
            # (column, row): ９一の位置を (0,0) としたときの場所
            column = int((centerPosX - self.minx) // self.piece_sizex)
            row = int((centerPosY - self.miny) // self.piece_sizey)
            print(column,row)

            # 5x5マスの外にいる場合、最小値に変更する
            if column < 0:
                column = 0
            elif column > 5 - 1:
                column = 4
            if row < 0:
                row = 0
            elif row > 5 - 1:
                row = 4

            # 駒をマスの中に移動する
            self.label_2.move(column * self.piece_sizex + self.minx, 
                              row * self.piece_sizey + self.miny)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())

