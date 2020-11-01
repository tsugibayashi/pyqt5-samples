#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, \
                            QTableWidgetItem, QHeaderView
from PyQt5.QtCore import QCoreApplication
from table3_ui import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # ヘッダの追加
        self.tableWidget.setColumnCount(1)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)

        # ヘッダの値を設定
        _translate = QCoreApplication.translate
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "指し手"))

        # ヘッダのデフォルト幅を設定
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)

        # ヘッダのデフォルト高さを設定
        self.tableWidget.verticalHeader().setDefaultSectionSize(32)

        # ヘッダのサイズ調整を無効化する
        self.tableWidget.horizontalHeader().\
                         setSectionResizeMode(QHeaderView.Fixed)

        # 行数を出力 (デバッグ)
        #print(self.tableWidget.rowCount())

        # 1列目の値を設定する
        self.insertItem(0, 0, "▲７六歩")
        self.insertItem(1, 0, "△８四歩")
        self.insertItem(2, 0, "▲６八銀")
        self.insertItem(3, 0, "△３四歩")
        self.insertItem(4, 0, "▲６六歩")
        self.insertItem(5, 0, "△６二銀")
        self.insertItem(6, 0, "▲５六歩")
        self.insertItem(7, 0, "△５四歩")
        self.insertItem(8, 0, "▲４八銀")
        self.insertItem(9, 0, "△４二銀")
        self.insertItem(10, 0, "▲５八金右")
        self.insertItem(11, 0, "△３二金")
        self.insertItem(12, 0, "▲７八金")
        self.insertItem(13, 0, "△４一玉")
        self.insertItem(14, 0, "▲６九玉")
        self.insertItem(15, 0, "△５二金")

    def insertItem(self, row, column, str):
        # 現在の行数を rowCount に代入
        rowCount = self.tableWidget.rowCount()

        # 行を追加する
        self.tableWidget.insertRow(rowCount)

        # 追加した行に値を設定する
        self.tableWidget.setItem(row, column, QTableWidgetItem(str))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())

