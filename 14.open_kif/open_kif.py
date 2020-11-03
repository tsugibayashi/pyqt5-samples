#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                            QTableWidgetItem, QHeaderView, 
                            qApp, QFileDialog)
from PyQt5.QtCore import QCoreApplication
from kifu_ui import Ui_MainWindow
from parser import Parser

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # ヘッダの設定
        self.configureHeader()

        # 行数を出力 (デバッグ)
        #print(self.tableWidget.rowCount())

        # ファイル->Exit をクリックしたときの動作
        self.actionExit.triggered.connect(qApp.quit)

        # ファイル->Open をクリックしたときの動作
        self.actionOpen.triggered.connect(self.openFile)

    # def configureHeader(self): {{{
    def configureHeader(self):
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
    # }}}

    # def insertItem(self, row, column, str): {{{
    def insertItem(self, row, column, str):
        # 現在の行数を rowCount に代入
        rowCount = self.tableWidget.rowCount()

        # 行を追加する
        self.tableWidget.insertRow(rowCount)

        # 追加した行に値を設定する
        self.tableWidget.setItem(row, column, QTableWidgetItem(str))
    # }}}

    def openFile(self):
        # カレントディレクトリを選択する
        dirname = os.getcwd()

        # ファイルダイアログを表示する
        filename = QFileDialog.getOpenFileName(self, 'ファイルを開く', dirname,
                               '棋譜ファイル (*.kif);;全て (*.*)')

        # ファイルが指定された場合、ファイルを読み込む
        if filename[0]:
            kif = Parser.parse_file(filename[0], 'utf-8')[0]

            # 表の各行の値を設定する
            i = 0
            for line in kif:
                # 1列目の値を設定する
                self.insertItem(i, 0, line)
                # 行をインクリメント
                i = i + 1

            # ウィンドウタイトルにファイル名を表示する
            self.setWindowTitle(os.path.basename(filename[0]))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())

