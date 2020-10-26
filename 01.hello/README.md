# hello.py

## 概要

ウィンドウ内に 'Hello, PyQT5 application' を表示するサンプルコードです。

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

    $ cd pyqt5-samples/hello/

(3) '\_ui' の付いていないPythonのコードを実行します。

    $ python hello.py

## コードの作成手順

(1) UIを作成するためのツール designer を起動します。

    $ /usr/lib/qt5/bin/designer &

(2) Main Window を選択し、画面サイズを指定する。

| 項目 | 値 |
----|----
| 画面サイズ | デフォルトのサイズ |

(3) [作成]を押下する。

(4) QMainWindow の設定を行う。

| 項目 | 値 |
----|----
| Main Window | QMainWindow |
| geometry | - |
| 幅 | 250 |
| 高さ | 230 |
| font | Noto Sans CJK JP,9 |
| windowTitle | Hello, PyQT5 |

(5) メニューバーを右クリックし、メニューバーを削除する。

(6) ラベルを追加する。

| 項目 | 値 |
----|----
| label | QLabel |
| geometry | - |
| X | 0 |
| Y | 100 |
| 幅 | 250 |
| 高さ | 32 |
| font | Noto Sans CJK JP,9 |
| text | Hello, PyQT5 application |

(7) hello.ui という名前で保存する。

(8) pyuic5 を使って、Pythonのコードを生成する。

    $ pyuic5 hello.ui > hello_ui.py

(9) メインのコード hello.py を作成する。

    $ vi hello.py

(10) 作成したメインのコードを実行する。

    $ python hello.py


