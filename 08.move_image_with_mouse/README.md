# move\_image\_with\_mouse.py

## 概要

ウィンドウ内の駒の画像を移動するサンプルコードです。
(マウス操作で移動できます)

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

    $ cd pyqt5-samples/09.move_image_with_mouse/

(3) '\_ui' の付いていないPythonのコードを実行します。

    $ python move_image_with_mouse.py

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
| 幅 | 545 |
| 高さ | 590 |
| font | Noto Sans CJK JP,9 |
| windowTitle | 画像のテスト |

(5) メニューバーを右クリックし、メニューバーを削除します。

(6) ステータスバーを右クリックし、ステータスバーを削除します。

(7) 1つ目のラベルを追加します。

| 項目 | 値 |
----|----
| label | QLabel |
| geometry | - |
| X | 10 |
| Y | 10 |
| 幅 | 525 |
| 高さ | 570 |
| font | Noto Sans CJK JP,9 |
| pixmap | images/board.png |

(8) 2つ目のラベルを追加します。

| 項目 | 値 |
----|----
| label\_2 | QLabel |
| geometry | - |
| X | 225 |
| Y | 455 |
| 幅 | 97 |
| 高さ | 106 |
| font | Noto Sans CJK JP,9 |
| text | 駒の画像 |

(9) image.ui という名前で保存します。

(10) pyuic5 を使って、Pythonのコードを生成します。

    $ pyuic5 image.ui > image_ui.py

(11) 画像を ../images/ に格納します。

| ファイル名 | 説明 |
----|----
| board.png | 5×5の将棋盤の画像 |
| piece\_v2\_776\_636.png | 駒の画像 |

(12) メインのコード move\_image\_with\_mouse.py を作成します。

    $ vi move_image_with_mouse.py

(13) 作成したメインのコードを実行します。

    $ python move_image_with_mouse.py

