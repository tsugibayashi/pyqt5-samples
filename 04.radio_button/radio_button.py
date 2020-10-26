#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, qApp
from main_window_ui import Ui_MainWindow
from sub_window_ui import Ui_SubWindow

### メインウィンドウ
class MainWindow(QMainWindow, Ui_MainWindow):
    # 初期化時に parent を渡せるようにしておく
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)

        # サブウィンドウを追加 (parent に MainWindow を指定する)
        self.sub_window  = SubWindow(self)

        # pushButton をクリックしたら、サブウィンドウを表示する
        self.pushButton.clicked.connect(self.open_sub_window)

        # pushButton_2 をクリックしたら、閉じる(アプリ終了)
        self.pushButton_2.clicked.connect(qApp.quit)

    # サブウィンドウを表示
    def open_sub_window(self, checked):
        self.sub_window.show()

### サブウィンドウ
class SubWindow(QWidget, Ui_SubWindow):
    # 初期化時に parent を渡せるようにしておく
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)

        # 色を表すID
        self.green_id = 1
        self.yellow_id = 2
        self.blue_id = 3

        # 色の設定
        self.green  = 'rgb(0, 255, 0)'
        self.yellow = 'rgb(255, 255, 0)'
        self.blue   = 'rgb(0, 100, 255)'

        # parent (本コードの場合、MainWindow) を self.parent に代入
        self.parent = parent

        # 各radioButton のIDを設定する
        self.buttonGroup.setId(self.radioButton, self.green_id)
        self.buttonGroup.setId(self.radioButton_2, self.yellow_id)
        self.buttonGroup.setId(self.radioButton_3, self.blue_id)

        # pushButtonがクリックされたとき、buttonClicked を実行する
        self.pushButton.clicked.connect(self.buttonClicked)

    # pushButtonがクリックされたときの動作
    def buttonClicked(self):
        #print(self.buttonGroup.checkedId())
        # メインウィンドウのラベルの背景色を変更する
        self.changeColor()
        # サブウィンドウを閉じる
        self.close()

    # ラベルの背景色を変更する
    def changeColor(self):
        if self.buttonGroup.checkedId() == self.green_id:
            self.parent.label.setStyleSheet("background-color: " + self.green)
        elif self.buttonGroup.checkedId() == self.yellow_id:
            self.parent.label.setStyleSheet("background-color: " + self.yellow)
        elif self.buttonGroup.checkedId() == self.blue_id:
            self.parent.label.setStyleSheet("background-color: " + self.blue)

### main routine
if __name__ == '__main__':
    app = QApplication(sys.argv)

    # メインウィンドウを表示する
    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())

