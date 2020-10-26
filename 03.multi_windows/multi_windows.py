#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, qApp
from main_window_ui import Ui_MainWindow
from sub_window_ui import Ui_SubWindow

### メインウィンドウ
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # サブウィンドウを追加
        self.sub_window  = SubWindow()

        # pushButton をクリックしたとら、サブウィンドウを表示する
        self.pushButton.clicked.connect(self.open_sub_window)
        # pushButton_2 をクリックしたら、閉じる
        self.pushButton_2.clicked.connect(qApp.quit)

    # サブウィンドウを表示
    def open_sub_window(self, checked):
        self.sub_window.show()

### サブウィンドウ
class SubWindow(QWidget, Ui_SubWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # pushButton をクリックしたときの動作
        self.pushButton.clicked.connect(self.close_self_window)

    # 自分自身(サブウィンドウ)を閉じる
    def close_self_window(self, checked):
        self.close()

### main routine
if __name__ == '__main__':
    app = QApplication(sys.argv)

    # メインウィンドウを表示する
    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())

