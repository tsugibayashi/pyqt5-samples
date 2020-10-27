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
from table_ui import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # モデルの設定
        self.model = QStandardItemModel(20, 2);
        self.model.setHorizontalHeaderLabels(['手数','指し手'])

        # 1列目の値を設定する
        for row in range(20):
            item = QStandardItem(str(row+1))
            self.model.setItem(row, 0, item)

        # 2列目の値を設定する
        self.model.setItem(0, 1, QStandardItem("▲７六歩"))
        self.model.setItem(1, 1, QStandardItem("△８四歩"))
        self.model.setItem(2, 1, QStandardItem("▲６八銀"))
        self.model.setItem(3, 1, QStandardItem("△３四歩"))
        self.model.setItem(4, 1, QStandardItem("▲６六歩"))
        self.model.setItem(5, 1, QStandardItem("△６二銀"))
        self.model.setItem(6, 1, QStandardItem("▲５六歩"))
        self.model.setItem(7, 1, QStandardItem("△５四歩"))
        self.model.setItem(8, 1, QStandardItem("▲４八銀"))
        self.model.setItem(9, 1, QStandardItem("△４二銀"))
        self.model.setItem(10, 1, QStandardItem("▲５八金右"))
        self.model.setItem(11, 1, QStandardItem("△３二金"))
        self.model.setItem(12, 1, QStandardItem("▲７八金"))
        self.model.setItem(13, 1, QStandardItem("△４一玉"))
        self.model.setItem(14, 1, QStandardItem("▲６九玉"))
        self.model.setItem(15, 1, QStandardItem("△５二金"))

        # tableViewにモデルを設定する
        self.tableView.setModel(self.model)

        # 各列の幅を適切に変更する
        self.tableView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableView.horizontalHeader().\
             setSectionResizeMode(QHeaderView.ResizeToContents)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())

