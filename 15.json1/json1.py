#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import os
import json
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget,
                             qApp)
from PyQt5 import QtCore, QtGui
from image_ui import Ui_MainWindow
from setting_ui import Ui_settingWindow

### メインウィンドウ
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 設定値を保存するファイル名
        self.settingJson = './setting.json'

        ### 画像ファイル名 {{{
        # 将棋盤
        self.board_img_v1 = '../images/board_v1.png'
        self.board_img_v2 = '../images/board_v2.png'
        # 駒
        self.pieces_img_v1 = '../images/piece_v1_776_636.png'
        self.pieces_img_v2 = '../images/piece_v2_776_636.png'
        self.pieces_img_v3 = '../images/piece_v3_776_636.png'
        # 筋
        self.column_img_v0 = '../images/number_v0_485_19.png'
        self.column_img_v1 = '../images/number_v1_485_19.png'
        self.column_img_v2 = '../images/number_v2_485_19.png'
        # 段
        self.row_img_v0 = '../images/number_v0_22_530.png'
        self.row_img_v1 = '../images/number_v1_22_530.png'
        self.row_img_v2 = '../images/number_v2_22_530.png'
        # }}}

        if os.path.exists(self.settingJson):
            # self.settingJson が存在する場合、設定を読み出す
            with open(self.settingJson) as f:
                setting = json.load(f)
            # 盤の画像
            self.board_img = setting['board_img']
            # 全ての駒を含む画像
            self.pieces_img = setting['pieces_img']
            # 筋の画像
            self.column_img = setting['column_img']
            # 段の画像
            self.row_img = setting['row_img']
        else:
            # self.settingJson が存在しない場合、デフォルト設定にする
            # 盤の画像
            self.board_img = self.board_img_v1
            # 全ての駒を含む画像
            self.pieces_img = self.pieces_img_v2
            # 筋の画像
            self.column_img = self.column_img_v1
            # 段の画像
            self.row_img = self.row_img_v1

        # 全てのラベルに画像を割り当てる
        self.shogi_setPixmap()

        # ファイル->終了 をクリックしたときの動作
        self.actionExit.triggered.connect(qApp.quit)

        # 設定->表示設定 をクリックしたときの動作
        self.actionSetting.triggered.connect(self.open_setting_window)

        # 表示設定ダイアログを追加 (parent に MainWindow を指定する)
        self.setting_window = SettingWindow(self)

    # def shogi_setPixmap(self): {{{
    def shogi_setPixmap(self):
        # 将棋盤に画像を設定
        self.board.setPixmap(QtGui.QPixmap(self.board_img))

        # 将棋盤に筋の画像を設定
        self.board_column.setPixmap(QtGui.QPixmap(self.column_img))

        # 将棋盤に段の画像を設定
        self.board_row.setPixmap(QtGui.QPixmap(self.row_img))

        ### 先手の駒
        # ラベル"king_black"に駒の画像を設定
        self.king_black.setPixmap(self.cropImage('king_black'))
        # ラベル"gold_black"に駒の画像を設定
        self.gold_black.setPixmap(self.cropImage('gold_black'))
        # ラベル"silver_black"に駒の画像を設定
        self.silver_black.setPixmap(self.cropImage('silver_black'))
        # ラベル"rook_black"に駒の画像を設定
        self.rook_black.setPixmap(self.cropImage('rook_black'))
        # ラベル"bishop_black"に駒の画像を設定
        self.bishop_black.setPixmap(self.cropImage('bishop_black'))
        # ラベル"pawn_black"に駒の画像を設定
        self.pawn_black.setPixmap(self.cropImage('pawn_black'))

        ### 後手の駒
        # ラベル"king_white"に駒の画像を設定
        self.king_white.setPixmap(self.cropImage('king_white'))
        # ラベル"gold_white"に駒の画像を設定
        self.gold_white.setPixmap(self.cropImage('gold_white'))
        # ラベル"silver_white"に駒の画像を設定
        self.silver_white.setPixmap(self.cropImage('silver_white'))
        # ラベル"rook_white"に駒の画像を設定
        self.rook_white.setPixmap(self.cropImage('rook_white'))
        # ラベル"bishop_white"に駒の画像を設定
        self.bishop_white.setPixmap(self.cropImage('bishop_white'))
        # ラベル"pawn_white"に駒の画像を設定
        self.pawn_white.setPixmap(self.cropImage('pawn_white'))
    # }}}

    # def cropImage(self, piece_type): {{{
    def cropImage(self, piece_type):
        # 切り取る画像の範囲
        width = 97
        height = 106

        # 切り取る画像の始点
        if piece_type == 'king_black':
            posx = 97 * 0
            posy = 106 * 1
        elif piece_type == 'gold_black':
            posx = 97 * 7
            posy = 106 * 0
        elif piece_type == 'silver_black':
            posx = 97 * 4
            posy = 106 * 0
        elif piece_type == 'rook_black':
            posx = 97 * 6
            posy = 106 * 0
        elif piece_type == 'bishop_black':
            posx = 97 * 5
            posy = 106 * 0
        elif piece_type == 'pawn_black':
            posx = 97 * 1
            posy = 106 * 0
        elif piece_type == 'king_white':
            posx = 97 * 0
            posy = 106 * 3
        elif piece_type == 'gold_white':
            posx = 97 * 7
            posy = 106 * 2
        elif piece_type == 'silver_white':
            posx = 97 * 4
            posy = 106 * 2
        elif piece_type == 'rook_white':
            posx = 97 * 6
            posy = 106 * 2
        elif piece_type == 'bishop_white':
            posx = 97 * 5
            posy = 106 * 2
        elif piece_type == 'pawn_white':
            posx = 97 * 1
            posy = 106 * 2

        # 切り取る対象の画像
        piece = QtGui.QPixmap(self.pieces_img)

        # 切り取る範囲
        rect = QtCore.QRect(posx, posy, width, height)

        # 切り取った画像
        return piece.copy(rect)
    # }}}

    def open_setting_window(self, checked):
        self.setting_window.show()

# 表示設定ダイアログ
class SettingWindow(QWidget, Ui_settingWindow):
    # 初期化時に parent を渡せるようにしておく
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)

        # 将棋盤の種類を表すID
        self.board_v1_id = 1
        self.board_v2_id = 2

        # 駒の種類を表すID
        self.piece_v1_id = 1
        self.piece_v2_id = 2
        self.piece_v3_id = 3

        # 筋・段の種類を表すID
        self.rank_v0_id = 1
        self.rank_v1_id = 2
        self.rank_v2_id = 3

        # buttonGroupBoard のIDを設定する
        self.buttonGroupBoard.setId(self.radioButtonBoardV1, self.board_v1_id)
        self.buttonGroupBoard.setId(self.radioButtonBoardV2, self.board_v2_id)

        # buttonGroupPiece のIDを設定する
        self.buttonGroupPiece.setId(self.radioButtonPieceV1, self.piece_v1_id)
        self.buttonGroupPiece.setId(self.radioButtonPieceV2, self.piece_v2_id)
        self.buttonGroupPiece.setId(self.radioButtonPieceV3, self.piece_v3_id)

        # buttonGroupRank のIDを設定する
        self.buttonGroupRank.setId(self.radioButtonRankV0, self.rank_v0_id)
        self.buttonGroupRank.setId(self.radioButtonRankV1, self.rank_v1_id)
        self.buttonGroupRank.setId(self.radioButtonRankV2, self.rank_v2_id)

        # parent (本コードの場合、MainWindow) を self.parent に代入
        self.parent = parent

        # 設定画面のラジオボタンにチェックを入れる
        if self.parent.board_img == self.parent.board_img_v1:
            self.radioButtonBoardV1.setChecked(True)
            self.radioButtonBoardV2.setChecked(False)
        elif self.parent.board_img == self.parent.board_img_v2:
            self.radioButtonBoardV1.setChecked(False)
            self.radioButtonBoardV2.setChecked(True)

        if self.parent.pieces_img == self.parent.pieces_img_v1:
            self.radioButtonPieceV1.setChecked(True)
            self.radioButtonPieceV2.setChecked(False)
            self.radioButtonPieceV3.setChecked(False)
        elif self.parent.pieces_img == self.parent.pieces_img_v2:
            self.radioButtonPieceV1.setChecked(False)
            self.radioButtonPieceV2.setChecked(True)
            self.radioButtonPieceV3.setChecked(False)
        elif self.parent.pieces_img == self.parent.pieces_img_v3:
            self.radioButtonPieceV1.setChecked(False)
            self.radioButtonPieceV2.setChecked(False)
            self.radioButtonPieceV3.setChecked(True)

        if self.parent.column_img == self.parent.column_img_v0:
            self.radioButtonRankV0.setChecked(True)
            self.radioButtonRankV1.setChecked(False)
            self.radioButtonRankV2.setChecked(False)
        elif self.parent.column_img == self.parent.column_img_v1:
            self.radioButtonRankV0.setChecked(False)
            self.radioButtonRankV1.setChecked(True)
            self.radioButtonRankV2.setChecked(False)
        elif self.parent.column_img == self.parent.column_img_v2:
            self.radioButtonRankV0.setChecked(False)
            self.radioButtonRankV1.setChecked(False)
            self.radioButtonRankV2.setChecked(True)

        # pushButtonCancelがクリックされたとき、cancelButtonClicked を実行する
        self.pushButtonCancel.clicked.connect(self.cancelButtonClicked)

        # pushButtonOKがクリックされたとき、okButtonClicked を実行する
        self.pushButtonOK.clicked.connect(self.okButtonClicked)

    # pushButtonCancel がクリックされたときの動作
    def cancelButtonClicked(self):
        # サブウィンドウを閉じる
        self.close()

    # pushButtonOK がクリックされたときの動作
    def okButtonClicked(self):
        # 表示設定の変更を行う
        # 盤の画像
        if self.buttonGroupBoard.checkedId() == self.board_v1_id:
            self.parent.board_img = self.parent.board_img_v1
        elif self.buttonGroupBoard.checkedId() == self.board_v2_id:
            self.parent.board_img = self.parent.board_img_v2

        # 全ての駒を含む画像
        if self.buttonGroupPiece.checkedId() == self.piece_v1_id:
            self.parent.pieces_img = self.parent.pieces_img_v1
        elif self.buttonGroupPiece.checkedId() == self.piece_v2_id:
            self.parent.pieces_img = self.parent.pieces_img_v2
        elif self.buttonGroupPiece.checkedId() == self.piece_v3_id:
            self.parent.pieces_img = self.parent.pieces_img_v3

        # 筋と段の画像
        if self.buttonGroupRank.checkedId() == self.rank_v0_id:
            self.parent.column_img = self.parent.column_img_v0
            self.parent.row_img = self.parent.row_img_v0
        elif self.buttonGroupRank.checkedId() == self.rank_v1_id:
            self.parent.column_img = self.parent.column_img_v1
            self.parent.row_img = self.parent.row_img_v1
        elif self.buttonGroupRank.checkedId() == self.rank_v2_id:
            self.parent.column_img = self.parent.column_img_v2
            self.parent.row_img = self.parent.row_img_v2

        # 全てのラベルに画像を割り当てる
        self.parent.shogi_setPixmap()

        # 設定値をjsonファイルに保存する
        setting = {
                      "board_img" : self.parent.board_img,
                      "pieces_img" : self.parent.pieces_img,
                      "column_img" : self.parent.column_img,
                      "row_img" : self.parent.row_img
                  }
        with open(self.parent.settingJson, 'w') as f:
            json.dump(setting, f, ensure_ascii=False, indent=4)

        # サブウィンドウを閉じる
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())

