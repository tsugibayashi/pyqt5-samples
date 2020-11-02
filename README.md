# PyQT5-samples

## 概要

PyQT5のサンプルコードです。

## 動作確認に使用した環境

- Ubuntu 18.04
- Python 3.6

## 前提作業

以下のパッケージをインストールして下さい。

    $ sudo apt install python3-pyqt5 pyqt5-dev-tools qttools5-dev-tools fonts-noto

* python3-pyqt5
* pyqt5-dev-tools
* qttools5-dev-tools
* fonts-noto (表示するフォントとして使用します)

## 使い方

(1) 本レポジトリをクローンします。

    $ git clone https://github.com/tsugibayashi/pyqt5-samples

(2) サンプルの格納されたディレクトリに移動します。

    $ cd pyqt5-samples/<ディレクトリ名>

| ディレクトリ名 | 説明 |
----|----
| 01.hello | Hello World (最初のプログラム) |
| 02.menu | メニューを表示する |
| 03.multi\_windows | 複数のウィンドウ(メインウィンドウとサブウィンドウ)を表示する |
| 04.radio\_button | サブウィンドウのラジオボタンを選択すると、メインウィンドウのラベルの背景色が変わる |
| 05.image | 5×5将棋盤の画像を表示する |
| 06.crop\_image | 5×5将棋盤の上に、大きな画像の一部を切り抜いた画像を表示する |
| 07.move\_image | 5×5将棋盤の上に置かれた駒を1マス移動する (マウス操作には非対応) |
| 08.move\_image\_with\_mouse | 5×5将棋盤の上に置かれた駒を移動する (マウス操作に対応) |
| 09.table | 表(QTableView)を表示する |
| 10.table2 | QScrollArea内に表(QTableView)を表示する |
| 11.table3 | 表(QTableWidget)を表示する |
| 12.text\_edit | 簡易のテキストエディタを表示する |

(3) '\_ui' の付いていないPythonのコードを実行します。

    例.
    $ python hello.py

## ライセンス

GPL v3


以上
