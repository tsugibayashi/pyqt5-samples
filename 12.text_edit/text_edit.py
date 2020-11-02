#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, qApp, QFileDialog
from PyQt5 import QtCore
from text_edit_ui import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # デフォルトのファイル名
        self.filename = None

        # ファイル->Exit をクリックしたときの動作
        self.actionExit.triggered.connect(qApp.quit)

        # ファイル->Open をクリックしたときの動作
        self.actionOpen.triggered.connect(self.openFile)

        # ファイル->Save をクリックしたときの動作
        self.actionSave.triggered.connect(self.saveFile)

        # ファイル->Save As をクリックしたときの動作
        self.actionSave_As.triggered.connect(self.saveAsFilename)

    def openFile(self):
        # カレントディレクトリを選択する
        dirname = os.getcwd()

        # ファイルダイアログを表示する
        filename = QFileDialog.getOpenFileName(self, 'ファイルを開く', dirname, 
                               'テキストファイル (*.txt);;全て (*.*)')

        #print(filename)

        # ファイルが指定された場合、ファイルを読み込む
        if filename[0]:
            f = open(filename[0], 'r')
            with f:
                data = f.read()
                self.textEdit.setText(data)
            # ファイルを閉じる
            f.close()

            # 開いたファイル名を self.filename(デフォルトファイル名) に代入する
            self.filename = filename[0]

            # ウィンドウタイトルにファイル名を表示する
            self.setWindowTitle(os.path.basename(self.filename))

    def saveFile(self):
        if self.filename:
            # デフォルトファイル名が設定済みの場合、そのファイル名で保存する
            f = open(self.filename, 'w')
            text = self.textEdit.toPlainText()
            f.write(text)
            # ファイルを閉じる
            f.close()
        else:
            # デフォルトファイル名が未設定の場合、
            # ファイル名を指定するダイアログを表示する
            self.saveAsFilename()

    def saveAsFilename(self):
        # カレントディレクトリを選択する
        dirname = os.getcwd()

        # ファイルダイアログを表示する
        filename = QFileDialog.getSaveFileName(self, 'ファイルに保存', dirname, 
                               'テキストファイル (*.txt);;全て (*.*)')

        # ファイル名+拡張子 を取得する
        basename = os.path.basename(filename[0])
        # 拡張子 を取得する
        extension = os.path.splitext(basename)[1]

        # 保存するファイル名の設定
        if extension:
            filename_and_ext = filename[0]
        else:
            # 指定したファイル名に拡張子がない場合、.txt を付与する
            filename_and_ext = filename[0] + '.txt'

        # テキストをファイルに保存する
        f = open(filename_and_ext, 'w')
        text = self.textEdit.toPlainText()
        f.write(text)

        # ファイルを閉じる
        f.close()

        # 保存したファイル名を self.filename(デフォルトファイル名) に代入する
        self.filename = filename_and_ext

        # ウィンドウタイトルにファイル名を表示する
        self.setWindowTitle(os.path.basename(self.filename))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())

