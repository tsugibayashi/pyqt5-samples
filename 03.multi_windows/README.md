# multi\_windows.py

## 概要

ウィンドウ内のボタンをクリックすると、別のウィンドウを表示するサンプルコードです。

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

    $ cd pyqt5-samples/03.multi_windows/

(3) '\_ui' の付いていないPythonのコードを実行します。

    $ python multi_windows.py

## コードの作成手順

### メインウィンドウの作成 

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
| 幅 | 300 |
| 高さ | 250 |
| font | Noto Sans CJK JP,9 |
| windowTitle | メインウィンドウ |

(5) メニューバーを右クリックし、メニューバーを削除します。

(6) 1つめのPushButtonを追加します。

| 項目 | 値 |
----|----
| pushButton | QPushButton |
| geometry | - |
| X | 30 |
| Y | 60 |
| 幅 | 231 |
| 高さ | 44 |
| font | Noto Sans CJK JP,9 |
| text | サブウィンドウを開く |

(7) 2つめのPushButtonを追加します。

| 項目 | 値 |
----|----
| pushButton\_2 | QPushButton |
| geometry | - |
| X | 80 |
| Y | 150 |
| 幅 | 128 |
| 高さ | 44 |
| font | Noto Sans CJK JP,9 |
| text | 閉じる |

(8) main\_window.ui という名前で保存します。

(9) pyuic5 を使って、Pythonのコードを生成します。

    $ pyuic5 main_window.ui > main_window_ui.py

### サブウィンドウの作成 

(1) UIを作成するためのツール designer を起動します。

    $ /usr/lib/qt5/bin/designer &

(2) Widget を選択し、画面サイズを指定します。

| 項目 | 値 |
----|----
| 画面サイズ | デフォルトのサイズ |

(3) [作成]を押下します。

(4) QWidget の設定を行います。

| 項目 | 値 |
----|----
| SubWindow | QWidget |
| geometry | - |
| 幅 | 400 |
| 高さ | 200 |
| font | Noto Sans CJK JP,9 |
| windowTitle | サブウィンドウ |

(5) PushButtonを追加します。

| 項目 | 値 |
----|----
| pushButton | QPushButton |
| geometry | - |
| X | 130 |
| Y | 75 |
| 幅 | 124 |
| 高さ | 44 |
| font | Noto Sans CJK JP,9 |
| text | 閉じる |

(6) sub\_window.ui という名前で保存します。

(7) pyuic5 を使って、Pythonのコードを生成します。

    $ pyuic5 sub_window.ui > sub_window_ui.py

### メインのコードを作成

(1) メインのコード multi\_windows.py を作成します。

    $ vi multi_windows.py

(2) 作成したメインのコードを実行します。

    $ python multi_windows.py

(3) メインウィンドウ内の (サブウィンドウを開く)ボタンをクリックし、サブウィンドウが表示されることを確認します。

(4) サブウィンドウ内の(閉じる)ボタンをクリックし、サブウィンドウが閉じられることを確認します。

(5) メインウィンドウ内の (閉じる) をクリックし、アプリが終了することを確認します。

