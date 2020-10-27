#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
from PyQt5.QtWidgets import (
                             QApplication, 
                             QMainWindow, 
                             QAbstractScrollArea, 
                             QHeaderView
                            )
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from table2_ui import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # モデルの設定
        self.model = QStandardItemModel(200, 1);
        self.model.setHorizontalHeaderLabels(['指し手'])

        # 値を設定する
        self.model.setItem(0, 0, QStandardItem("▲７六歩"))
        self.model.setItem(1, 0, QStandardItem("△８四歩"))
        self.model.setItem(2, 0, QStandardItem("▲６八銀"))
        self.model.setItem(3, 0, QStandardItem("△３四歩"))
        self.model.setItem(4, 0, QStandardItem("▲６六歩"))
        self.model.setItem(5, 0, QStandardItem("△６二銀"))
        self.model.setItem(6, 0, QStandardItem("▲５六歩"))
        self.model.setItem(7, 0, QStandardItem("△５四歩"))
        self.model.setItem(8, 0, QStandardItem("▲４八銀"))
        self.model.setItem(9, 0, QStandardItem("△４二銀"))
        self.model.setItem(10, 0, QStandardItem("▲５八金右"))
        self.model.setItem(11, 0, QStandardItem("△３二金"))
        self.model.setItem(12, 0, QStandardItem("▲７八金"))
        self.model.setItem(13, 0, QStandardItem("△４一玉"))
        self.model.setItem(14, 0, QStandardItem("▲６九玉"))
        self.model.setItem(15, 0, QStandardItem("△５二金"))

        # tableViewにモデルを設定する
        self.tableView.setModel(self.model)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())

