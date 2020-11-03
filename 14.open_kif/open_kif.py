#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import os
import cchardet
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

        # カレントディレクトリ
        self.dirname = os.getcwd()

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

    # def openFile(self): {{{
    def openFile(self):
        # ファイルダイアログを表示する
        filename = QFileDialog.getOpenFileName(self, 
                               'ファイルを開く', self.dirname,
                               '棋譜ファイル (*.kif);;全て (*.*)')

        if filename[0]:
            # ファイルの文字コードを判別する
            fileEnc = self.detectEncoding(filename[0])

            if fileEnc == 'UTF-8-SIG' or fileEnc == 'UTF-8':
                enc = 'utf_8'
            # ISO-8859-7 と誤認識された場合、SHIFT-JIS と判断する
            elif fileEnc == 'SHIFT_JIS' or fileEnc == 'ISO-8859-7':
                enc = 'shift_jis'

            # ファイルから棋譜を読み込む
            kif = Parser.parse_file(filename[0], enc)[0]

            # 表のデータを全て消去する
            self.tableWidget.clearContents()
            # 行数を0に設定する
            self.tableWidget.setRowCount(0)

            # 表の各行の値を設定する
            i = 0
            for line in kif:
                # 1列目の値を設定する
                self.insertItem(i, 0, line)
                # 行をインクリメント
                i = i + 1

            # ウィンドウタイトルにファイル名を表示する
            self.setWindowTitle(os.path.basename(filename[0]))

            # カレントディレクトリを開いたファイルの場所に変更する
            self.dirname = os.path.dirname(filename[0])
    # }}}

    def detectEncoding(self, filename):
        # ファイルをバイナリモードで開く
        with open(filename, 'rb') as f:
            b = f.read()
        #print(cchardet.detect(b))

        # 検出した文字コードを返す
        return cchardet.detect(b)['encoding']


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())

