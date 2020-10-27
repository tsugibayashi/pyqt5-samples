# table2.py

## 概要

ウィンドウ内に表を表示するサンプルコードです。

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

    $ cd pyqt5-samples/10.table2/

(3) '\_ui' の付いていないPythonのコードを実行します。

    $ python table2.py

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
| 幅 | 280 |
| 高さ | 500 |
| font | Noto Sans CJK JP,9 |
| windowTitle | 表のテスト |

(5) メニューバーを右クリックし、メニューバーを削除します。

(6) ステータスバーを右クリックし、ステータスバーを削除します。

(7) Scroll Area を追加します。

| 項目 | 値 |
----|----
| scrollArea | QScrollArea |
| geometry | - |
| X | 10 |
| Y | 10 |
| 幅 | 260 |
| 高さ | 480 |
| 横方向のポリシー | Fixed |
| 縦方向のポリシー | Expanding |
| font | Noto Sans CJK JP,9 |

(8) Table View を追加します。

| 項目 | 値 |
----|----
| tableView | QTableView |
| geometry | - |
| X | 0 |
| Y | 0 |
| 幅 | 260 |
| 高さ | 4000 |
| verticalScrollBarPolicy | ScrollBarAlwaysOn |

(9) table2.ui という名前で保存します。

(10) pyuic5 を使って、Pythonのコードを生成します。

    $ pyuic5 table2.ui > table2_ui.py

(11) メインのコード table2.py を作成します。

    $ vi table2.py

(12) 作成したメインのコードを実行します。

    $ python table2.py

