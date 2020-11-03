# open\_kif.py

## 概要

KIF形式の棋譜を表に表示するサンプルコードです。

## 動作確認に使用した環境

- Ubuntu 18.04
- Python 3.6

## 前提作業

(1) 以下のパッケージをインストールして下さい。

    $ sudo apt install python3-pyqt5 pyqt5-dev-tools qttools5-dev-tools fonts-noto

* python3-pyqt5
* pyqt5-dev-tools
* qttools5-dev-tools
* fonts-noto (表示するフォントとして使用します)

(2) ファイルの文字コードを判別するために、cchardet をインストールします。

    $ pip install cchardet

## 使い方

(1) 本レポジトリをクローンします。

    $ git clone https://github.com/tsugibayashi/pyqt5-samples

(2) サンプルの格納されたディレクトリに移動します。

    $ cd pyqt5-samples/14.open_kif/

(3) '\_ui' の付いていないPythonのコードを実行します。

    $ python open_kif.py

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
| 幅 | 260 |
| 高さ | 530 |
| font | Noto Sans CJK JP,9 |
| windowTitle | 棋譜ビューア |

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

(9) Table Widget を追加します。

| 項目 | 値 |
----|----
| tableWidget | QTableWidget |
| geometry | - |
| X | 10 |
| Y | 20 |
| 幅 | 240 |
| 高さ | 460 |
| font | Noto Sans CJK JP,9 |

(10) kifu.ui という名前で保存します。

(11) pyuic5 を使って、Pythonのコードを生成します。

    $ pyuic5 kifu.ui > kifu_ui.py

(12) 棋譜読み込み用のコード parser.py を作成します。

    $ vi parser.py

(13) 読み込みに使用するKIF形式のファイルを作成します。(文字コードはUTF-8にします)

| 項目 | 値 |
----|----
| ファイル名 | MyShogi\_20201017105219.kif |

(14) メインのコード open\_kif.py を作成します。

    $ vi open_kif.py

(15) 作成したメインのコードを実行します。

    $ python open_kif.py

(16) ファイル-\>Open を選択して、MyShogi\_20201017105219.kif を開きます。

