# menu.py

## 概要

ウィンドウ内にメニューバーを表示するサンプルコードです。
メニューバーにはアプリを終了する項目のみが存在します。

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

    $ cd pyqt5-samples/02.menu/

(3) '\_ui' の付いていないPythonのコードを実行します。

    $ python menu.py

## コードの作成手順

(1) UIを作成するためのツール designer を起動します。

    $ /usr/lib/qt5/bin/designer &

(2) Main Window を選択し、画面サイズを指定します。

| 項目 | 値 |
----|----
| 画面サイズ | デフォルトのサイズ |

(3) [作成]を押下する。

(4) QMainWindow の設定を行う。

| 項目 | 値 |
----|----
| Main Window | QMainWindow |
| geometry | - |
| 幅 | 300 |
| 高さ | 250 |
| font | Noto Sans CJK JP,9 |
| windowTitle | Menuのテスト |

(5) メニューバーをダブルクリックし、値を設定します。

menubar: QMenuBar に menu: QMenu が追加されます。

| 項目 | 値 |
----|----
| メニューバー | ファイル |

(6) メニューバーに追加した”ファイル"をクリックし、値を設定します。

actionExit: QAction が追加されます。

| 項目 | 値 |
----|----
| "ファイル"内の項目 | Exit |

(7) actionExit: QAction 選択し、値を設定します。

| 項目 | 値 |
----|----
| font | Noto Sans CJK JP,9 |
| shortcut | Ctrl+Q |

(8) menu.ui という名前で保存します。

(9) pyuic5 を使って、Pythonのコードを生成します。

    $ pyuic5 menu.ui > menu_ui.py

(10) メインのコード menu.py を作成します。

    $ vi menu.py

(11) 作成したメインのコードを実行します。

    $ python menu.py

(12) ファイル -> Exit をクリックし、アプリが終了することを確認します。

(13) Ctrl+Q を押し、アプリが終了することを確認します。

