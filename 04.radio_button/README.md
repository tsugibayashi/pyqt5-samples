# radio\_button.py

## 概要

ウィンドウ内のボタンをクリックすると、ラジオボタンの選択画面が表示されるサンプルコードです。

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

    $ cd pyqt5-samples/04.radio_button/

(3) '\_ui' の付いていないPythonのコードを実行します。

    $ python radio_button.py

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
| 幅 | 350 |
| 高さ | 250 |
| font | Noto Sans CJK JP,9 |
| windowTitle | メインウィンドウ |

(5) メニューバーを右クリックし、メニューバーを削除します。

(6) 1つめのPushButtonを追加します。

| 項目 | 値 |
----|----
| pushButton | QPushButton |
| geometry | - |
| X | 80 |
| Y | 100 |
| 幅 | 180 |
| 高さ | 44 |
| font | Noto Sans CJK JP,9 |
| text | 選択画面を開く |

(7) 2つめのPushButtonを追加します。

| 項目 | 値 |
----|----
| pushButton\_2 | QPushButton |
| geometry | - |
| X | 110 |
| Y | 160 |
| 幅 | 128 |
| 高さ | 44 |
| font | Noto Sans CJK JP,9 |
| text | 閉じる |

(8) ラベルを追加します。

| 項目 | 値 |
----|----
| label | QLabel |
| geometry | - |
| X | 20 |
| Y | 40 |
| 幅 | 300 |
| 高さ | 32 |
| font | Noto Sans CJK JP,9 |
| styleSheet | background-color: rgb(0, 255, 0) |
| text | 設定値に応じて背景色が変わる |

(9) main\_window.ui という名前で保存します。

(10) pyuic5 を使って、Pythonのコードを生成します。

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
| objectName | SubWindow |
| geometry | - |
| 幅 | 400 |
| 高さ | 200 |
| font | Noto Sans CJK JP,9 |
| windowTitle | 選択画面 |

(5) 1つめのRadioButtonを追加します。

| 項目 | 値 |
----|----
| radioButton | QRadioButton |
| geometry | - |
| X | 20 |
| Y | 70 |
| 幅 | 162 |
| 高さ | 38 |
| font | Noto Sans CJK JP,9 |
| text | 緑色 |

(6) 2つめのRadioButtonを追加します。

| 項目 | 値 |
----|----
| radioButton\_2 | QRadioButton |
| geometry | - |
| X | 155 |
| Y | 70 |
| 幅 | 162 |
| 高さ | 38 |
| font | Noto Sans CJK JP,9 |
| text | 黄色 |

(7) 3つめのRadioButtonを追加します。

| 項目 | 値 |
----|----
| radioButton\_3 | QRadioButton |
| geometry | - |
| X | 290 |
| Y | 70 |
| 幅 | 162 |
| 高さ | 38 |
| font | Noto Sans CJK JP,9 |
| text | 青色 |

(8) Ctrlを押しながら3つのRadioButtonをクリックします。

(9) radioButtonを右クリックし、ボタングループに割り当て->新しいボタングループ を選択します。

(10) PushButtonを追加します。

| 項目 | 値 |
----|----
| pushButton | QPushButton |
| geometry | - |
| X | 130 |
| Y | 140 |
| 幅 | 128 |
| 高さ | 44 |
| font | Noto Sans CJK JP,9 |
| text | OK |

(11) sub\_window.ui という名前で保存します。

(12) pyuic5 を使って、Pythonのコードを生成します。

    $ pyuic5 sub_window.ui > sub_window_ui.py

### メインのコードを作成

(1) メインのコード radio\_button.py を作成します。

    $ vi radio_button.py

(2) 作成したメインのコードを実行します。

    $ python radio_button.py

(3) メインウィンドウ内の (選択画面を開く)ボタンをクリックし、サブウィンドウが表示されることを確認します。

(4) サブウィンドウ内の 緑色、黄色、または、青色 のラジオボタンをクリックします。

(5) サブウィンドウの (OK) をクリックし、サブウィンドウが閉じられることを確認します。

(6) ラベル"設定値に応じて背景色が変わる" の背景色が変わることを確認します。

(7) メインウィンドウ内の (閉じる) をクリックし、アプリが終了することを確認します。

