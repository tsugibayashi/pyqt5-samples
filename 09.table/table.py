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
        self.model = QStandardItemModel(8, 2);
        self.model.setHorizontalHeaderLabels(['手数','指し手'])

        # 1列目の値を設定する
        for row in range(4):
            item = QStandardItem(str(row+1))
            self.model.setItem(row, 0, item)

        # 2列目の値を設定する
        self.model.setItem(0, 1, QStandardItem("▲７六歩"))
        self.model.setItem(1, 1, QStandardItem("△８四歩"))
        self.model.setItem(2, 1, QStandardItem("△８四歩"))
        self.model.setItem(3, 1, QStandardItem("▲６八銀"))
        self.model.setItem(4, 1, QStandardItem("▲６六歩"))
        self.model.setItem(5, 1, QStandardItem("△６二銀"))
        self.model.setItem(6, 1, QStandardItem("▲５六歩"))
        self.model.setItem(7, 1, QStandardItem("△５四歩"))

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

