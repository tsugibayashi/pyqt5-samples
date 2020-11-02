# table4.py

## 概要

テキストファイルの内容を表に表示するサンプルコードです。

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

    $ cd pyqt5-samples/13.table4/

(3) '\_ui' の付いていないPythonのコードを実行します。

    $ python table4.py

## コードの作成手順

(1) UIを作成するためのツール designer を起動します。

    $ /usr/lib/qt5/bin/designer &

(2) Main Window を選択し、画面サイズを指定します。

| 項目 | 値 |
----|----
| 画面サイズ | デフォルトのサイズ |

(3) [作成]を押下します。

(4) QMainWindow の設定を行います。

| 項目 | 値 |
----|----
| Main Window | QMainWindow |
| geometry | - |
| 幅 | 240 |
| 高さ | 530 |
| font | Noto Sans CJK JP,9 |
| windowTitle | 表のテスト |

(5) ステータスバーを右クリックし、ステータスバーを削除します。

(6) メニューバーをダブルクリックし、値を設定します。

menubar: QMenuBar に menu: QMenu が追加されます。

| 項目 | 値 |
----|----
| メニューバー | ファイル |

(7) メニューバーに追加した"ファイル"をクリックし、値を設定します。

actionExit: QAction が追加されます。

| 項目 | 値 |
----|----
| "ファイル"内の項目 | Open |
| "ファイル"内の項目 | Exit |

(8) actionOpen と actionExit を選択し、値を設定します。

| 項目 | 値 |
----|----
| font | Noto Sans CJK JP,9 |

(9) table4.ui という名前で保存します。

(10) pyuic5 を使って、Pythonのコードを生成します。

    $ pyuic5 table4.ui > table4_ui.py

(11) メインのコード table4.py を作成します。

    $ vi table4.py

(12) 読み込みに使用するテキストファイルを作成します。

    $ vi kifu.txt

(13) 作成したメインのコードを実行します。

    $ python table4.py

(14) ファイル-\>Open を選択して、kifu.txt を開きます。

