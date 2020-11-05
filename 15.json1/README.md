# json1.py

## 概要

設定画面で設定した内容をファイル(JSON形式)に出力し、
再起動時に設定した内容が反映されるサンプルコードです。

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

    $ cd pyqt5-samples/15.json1/

(3) '\_ui' の付いていないPythonのコードを実行します。

    $ python json1.py

## コードの作成手順

### メインウィンドウの作成手順

(1) 画像を ../images/ に格納します。

| ファイル名 | 説明 |
----|----
| board\_v1.png | 5×5の将棋盤の画像(白色) |
| board\_v2.png | 5×5の将棋盤の画像(黄色) |
| piece\_v1\_776\_636.png | 二文字駒の画像 |
| piece\_v2\_776\_636.png | 一文字駒の画像 |
| piece\_v3\_776\_636.png | 英文字駒の画像 |
| number\_v0\_485\_19.png | 5五将棋の筋に使用する画像(空白) |
| number\_v0\_22\_530.png | 5五将棋の段に使用する画像(空白) |
| number\_v1\_485\_19.png | 5五将棋の筋(１から５)に使用する画像 |
| number\_v1\_22\_530.png | 5五将棋の段(一から五)に使用する画像 |
| number\_v2\_485\_19.png | 5五将棋の筋(1から5)に使用する画像 |
| number\_v2\_22\_530.png | 5五将棋の段(aからe)に使用する画像 |

(2) UIを作成するためのツール designer を起動します。

    $ /usr/lib/qt5/bin/designer &

(3) Main Window を選択し、画面サイズを指定します。

| 項目 | 値 |
----|----
| 画面サイズ | デフォルトのサイズ |

(4) [作成]を押下します。

(5) QMainWindow の設定を行います。

| 項目 | 値 |
----|----
| Main Window | QMainWindow |
| geometry | - |
| 幅 | 545 |
| 高さ | 630 |
| font | Noto Sans CJK JP,9 |
| windowTitle | 画像のテスト |

(6) ステータスバーを右クリックし、ステータスバーを削除します。

(7) メニューバーをダブルクリックし、値を設定します。

menubar: QMenuBar に menu: QMenu が追加されます。

| 項目 | 値 |
----|----
| メニューバー | ファイル |
| メニューバー | 設定 |

(8) メニューバーに追加した"ファイル"をクリックし、値を設定します。

actionExit: QAction が追加されます。

| 項目 | 値 |
----|----
| "ファイル"内の項目 | 終了 |

(9) actionExit を選択し、値を設定します。

| 項目 | 値 |
----|----
| font | Noto Sans CJK JP,9 |

(10) メニューバーに追加した"設定"をクリックし、値を設定します。

actionSetting: QAction が追加されます。

| 項目 | 値 |
----|----
| "設定"内の項目 | 表示設定 |

(11) actionSetting を選択し、値を設定します。

| 項目 | 値 |
----|----
| font | Noto Sans CJK JP,9 |

(12) 1個目のラベルを追加します。

| 項目 | 値 |
----|----
| board | QLabel |
| geometry | - |
| X | 10 |
| Y | 10 |
| 幅 | 533 |
| 高さ | 578 |
| font | Noto Sans CJK JP,9 |
| pixmap | images/board\_v1.png |

(13) 2個目のラベルを追加します。

| 項目 | 値 |
----|----
| king\_black | QLabel |
| geometry | - |
| X | 35 |
| Y | 459 |
| 幅 | 97 |
| 高さ | 106 |
| font | Noto Sans CJK JP,9 |
| text | 先手の王 |

(14) 3個目のラベルを追加します。

| 項目 | 値 |
----|----
| king\_white | QLabel |
| geometry | - |
| X | 423 |
| Y | 35 |
| 幅 | 97 |
| 高さ | 106 |
| font | Noto Sans CJK JP,9 |
| text | 後手の王 |

(15) 4個目のラベルを追加します。

| 項目 | 値 |
----|----
| gold\_black | QLabel |
| geometry | - |
| X | 132 |
| Y | 459 |
| 幅 | 97 |
| 高さ | 106 |
| font | Noto Sans CJK JP,9 |
| text | 先手の金 |

(16) 5個目のラベルを追加します。

| 項目 | 値 |
----|----
| gold\_white | QLabel |
| geometry | - |
| X | 326 |
| Y | 35 |
| 幅 | 97 |
| 高さ | 106 |
| font | Noto Sans CJK JP,9 |
| text | 後手の金 |

(17) 6個目のラベルを追加します。

| 項目 | 値 |
----|----
| silver\_black | QLabel |
| geometry | - |
| X | 229 |
| Y | 459 |
| 幅 | 97 |
| 高さ | 106 |
| font | Noto Sans CJK JP,9 |
| text | 先手の銀 |

(18) 7個目のラベルを追加します。

| 項目 | 値 |
----|----
| silver\_white | QLabel |
| geometry | - |
| X | 229 |
| Y | 35 |
| 幅 | 97 |
| 高さ | 106 |
| font | Noto Sans CJK JP,9 |
| text | 後手の銀 |

(19) 8個目のラベルを追加します。

| 項目 | 値 |
----|----
| bishop\_black | QLabel |
| geometry | - |
| X | 326 |
| Y | 459 |
| 幅 | 97 |
| 高さ | 106 |
| font | Noto Sans CJK JP,9 |
| text | 先手の角 |

(20) 9個目のラベルを追加します。

| 項目 | 値 |
----|----
| bishop\_white | QLabel |
| geometry | - |
| X | 132 |
| Y | 35 |
| 幅 | 97 |
| 高さ | 106 |
| font | Noto Sans CJK JP,9 |
| text | 後手の角 |

(21) 10個目のラベルを追加します。

| 項目 | 値 |
----|----
| rook\_black | QLabel |
| geometry | - |
| X | 423 |
| Y | 459 |
| 幅 | 97 |
| 高さ | 106 |
| font | Noto Sans CJK JP,9 |
| text | 先手の飛 |

(22) 11個目のラベルを追加します。

| 項目 | 値 |
----|----
| rook\_white | QLabel |
| geometry | - |
| X | 35 |
| Y | 35 |
| 幅 | 97 |
| 高さ | 106 |
| font | Noto Sans CJK JP,9 |
| text | 後手の飛 |

(23) 12個目のラベルを追加します。

| 項目 | 値 |
----|----
| pawn\_black | QLabel |
| geometry | - |
| X | 35 |
| Y | 353 |
| 幅 | 97 |
| 高さ | 106 |
| font | Noto Sans CJK JP,9 |
| text | 先手の歩 |

(24) 13個目のラベルを追加します。

| 項目 | 値 |
----|----
| pawn\_white | QLabel |
| geometry | - |
| X | 423 |
| Y | 141|
| 幅 | 97 |
| 高さ | 106 |
| font | Noto Sans CJK JP,9 |
| text | 後手の歩 |

(25) 14個目のラベルを追加します。

| 項目 | 値 |
----|----
| board\_column | QLabel |
| geometry | - |
| X | 35 |
| Y | 12 |
| 幅 | 485 |
| 高さ | 19 |
| font | Noto Sans CJK JP,9 |
| pixmap | images/number\_v1\_485\_19.png |

(26) 15個目のラベルを追加します。

| 項目 | 値 |
----|----
| board\_row | QLabel |
| geometry | - |
| X | 522 |
| Y | 35 |
| 幅 | 22 |
| 高さ | 530 |
| font | Noto Sans CJK JP,9 |
| pixmap | images/number\_v1\_22\_530.png |

(27) image.ui という名前で保存します。

(28) pyuic5 を使って、Pythonのコードを生成します。

    $ pyuic5 image.ui > image_ui.py

### 設定画面の作成手順

(1) 画像を ../images/setting\_dialog/ に格納します。

| ファイル名 | 説明 |
----|----
| board\_image\_ver\_1.png | 盤画像(白色) |
| board\_image\_ver\_2.png | 盤画像(黄色) |
| piece\_image\_ver\_1.png | 二文字駒 |
| piece\_image\_ver\_2.png | 一文字駒 |
| piece\_image\_ver\_3.png | 英文字駒 |
| rank\_style\_0.png | 筋・段の非表示 |
| rank\_style\_1.png | 筋・段の表示(標準) |
| rank\_style\_2.png | 筋・段の表示(Chess式) |

(2) UIを作成するためのツール designer を起動します。

    $ /usr/lib/qt5/bin/designer &

(3) Widget を選択し、画面サイズを指定します。

| 項目 | 値 |
----|----
| 画面サイズ | デフォルトのサイズ |

(4) [作成]を押下します。

(5) QWidget の設定を行います。

| 項目 | 値 |
----|----
| settingWindow | QWidget |
| objectName | settingWindow |
| geometry | - |
| 幅 | 520 |
| 高さ | 540 |
| font | Noto Sans CJK JP,9 |
| windowTitle | 表示設定 |

(6) 1個目の Group Box を追加します。

| 項目 | 値 |
----|----
| groupBoxBoard | QGroupBox |
| geometry | - |
| X | 10 |
| Y | 10 |
| 幅 | 340 |
| 高さ | 140 |
| font | Noto Sans CJK JP,9 |
| title | 将棋盤 |

(7) 1個目の Radio Button を追加します。

| 項目 | 値 |
----|----
| radioButtonBoardV1 | QRadioButton |
| geometry | - |
| X | 20 |
| Y | 40 |
| 幅 | 140 |
| 高さ | 38 |
| font | Noto Sans CJK JP,9 |
| text | 将棋盤(白) |

(8) 2個目の Radio Button を追加します。

| 項目 | 値 |
----|----
| radioButtonBoardV2 | QRadioButton |
| geometry | - |
| X | 180 |
| Y | 40 |
| 幅 | 140 |
| 高さ | 38 |
| font | Noto Sans CJK JP,9 |
| text | 将棋盤(黄) |

(9) 1個目のラベルを追加します。

| 項目 | 値 |
----|----
| labelBoardV1 | QLabel |
| geometry | - |
| X | 20 |
| Y | 80 |
| 幅 | 100 |
| 高さ | 50 |
| font | Noto Sans CJK JP,9 |
| pixmap | images/setting\_dialog/board\_image\_ver\_1.png |

(10) 2個目のラベルを追加します。

| 項目 | 値 |
----|----
| labelBoardV2 | QLabel |
| geometry | - |
| X | 180 |
| Y | 80 |
| 幅 | 100 |
| 高さ | 50 |
| font | Noto Sans CJK JP,9 |
| pixmap | images/setting\_dialog/board\_image\_ver\_2.png |

(11) 1個目と2個目のラジオボタンを両方選択して、"ボタングループに割り当て"->"新しいボタングループ"を選択します。

| 項目 | 値 |
----|----
| buttonGroupBoard | QButtonGroup |
| objectName | buttonGroupBoard |

(12) 2個目の Group Box を追加します。

| 項目 | 値 |
----|----
| groupBoxPiece | QGroupBox |
| geometry | - |
| X | 10 |
| Y | 170 |
| 幅 | 490 |
| 高さ | 140 |
| font | Noto Sans CJK JP,9 |
| title | 駒 |

(13) 3個目の Radio Button を追加します。

| 項目 | 値 |
----|----
| radioButtonPieceV1 | QRadioButton |
| geometry | - |
| X | 20 |
| Y | 40 |
| 幅 | 140 |
| 高さ | 38 |
| font | Noto Sans CJK JP,9 |
| text | 二文字駒 |

(14) 4個目の Radio Button を追加します。

| 項目 | 値 |
----|----
| radioButtonPieceV2 | QRadioButton |
| geometry | - |
| X | 180 |
| Y | 40 |
| 幅 | 140 |
| 高さ | 38 |
| font | Noto Sans CJK JP,9 |
| text | 一文字駒 |

(15) 5個目の Radio Button を追加します。

| 項目 | 値 |
----|----
| radioButtonPieceV3 | QRadioButton |
| geometry | - |
| X | 340 |
| Y | 40 |
| 幅 | 140 |
| 高さ | 38 |
| font | Noto Sans CJK JP,9 |
| text | 英文字駒 |

(16) 3個目のラベルを追加します。

| 項目 | 値 |
----|----
| labelPieceV1 | QLabel |
| geometry | - |
| X | 20 |
| Y | 80 |
| 幅 | 100 |
| 高さ | 50 |
| font | Noto Sans CJK JP,9 |
| pixmap | images/setting\_dialog/piece\_image\_ver\_1.png |

(17) 4個目のラベルを追加します。

| 項目 | 値 |
----|----
| labelPieceV2 | QLabel |
| geometry | - |
| X | 180 |
| Y | 80 |
| 幅 | 100 |
| 高さ | 50 |
| font | Noto Sans CJK JP,9 |
| pixmap | images/setting\_dialog/piece\_image\_ver\_2.png |

(18) 5個目のラベルを追加します。

| 項目 | 値 |
----|----
| labelPieceV3 | QLabel |
| geometry | - |
| X | 340 |
| Y | 80 |
| 幅 | 100 |
| 高さ | 50 |
| font | Noto Sans CJK JP,9 |
| pixmap | images/setting\_dialog/piece\_image\_ver\_3.png |

(19) 3個目, 4個目, 5個目のラジオボタンを選択して、"ボタングループに割り当て"->"新しいボタングループ"を選択します。

| 項目 | 値 |
----|----
| buttonGroupPiece | QButtonGroup |
| objectName | buttonGroupPiece |

(20) 3個目の Group Box を追加します。

| 項目 | 値 |
----|----
| groupBoxRank | QGroupBox |
| geometry | - |
| X | 10 |
| Y | 330 |
| 幅 | 490 |
| 高さ | 140 |
| font | Noto Sans CJK JP,9 |
| title | 筋・段 |

(21) 6個目の Radio Button を追加します。

| 項目 | 値 |
----|----
| radioButtonRankV0 | QRadioButton |
| geometry | - |
| X | 20 |
| Y | 40 |
| 幅 | 140 |
| 高さ | 38 |
| font | Noto Sans CJK JP,9 |
| text | 非表示 |

(22) 7個目の Radio Button を追加します。

| 項目 | 値 |
----|----
| radioButtonRankV1 | QRadioButton |
| geometry | - |
| X | 180 |
| Y | 40 |
| 幅 | 140 |
| 高さ | 38 |
| font | Noto Sans CJK JP,9 |
| text | 標準 |

(23) 8個目の Radio Button を追加します。

| 項目 | 値 |
----|----
| radioButtonRankV2 | QRadioButton |
| geometry | - |
| X | 340 |
| Y | 40 |
| 幅 | 140 |
| 高さ | 38 |
| font | Noto Sans CJK JP,9 |
| text | Chess式 |

(24) 6個目のラベルを追加します。

| 項目 | 値 |
----|----
| labelRankV0 | QLabel |
| geometry | - |
| X | 20 |
| Y | 80 |
| 幅 | 100 |
| 高さ | 50 |
| font | Noto Sans CJK JP,9 |
| pixmap | images/setting\_dialog/rank\_style\_0.png |

(25) 7個目のラベルを追加します。

| 項目 | 値 |
----|----
| labelRankV1 | QLabel |
| geometry | - |
| X | 180 |
| Y | 80 |
| 幅 | 100 |
| 高さ | 50 |
| font | Noto Sans CJK JP,9 |
| pixmap | images/setting\_dialog/rank\_style\_1.png |

(26) 8個目のラベルを追加します。

| 項目 | 値 |
----|----
| labelRankV2 | QLabel |
| geometry | - |
| X | 340 |
| Y | 80 |
| 幅 | 100 |
| 高さ | 50 |
| font | Noto Sans CJK JP,9 |
| pixmap | images/setting\_dialog/rank\_style\_2.png |

(27) 6個目, 7個目, 8個目のラジオボタンを選択して、"ボタングループに割り当て"->"新しいボタングループ"を選択します。

| 項目 | 値 |
----|----
| buttonGroupRank | QButtonGroup |
| objectName | buttonGroupRank |

(28) 1個目の Push Button を追加します。

| 項目 | 値 |
----|----
| pushButtonOK | QLabel |
| geometry | - |
| X | 80 |
| Y | 490 |
| 幅 | 128 |
| 高さ | 44 |
| font | Noto Sans CJK JP,9 |
| text | OK |

(29) 2個目の Push Button を追加します。

| 項目 | 値 |
----|----
| pushButtonCancel | QLabel |
| geometry | - |
| X | 270 |
| Y | 490 |
| 幅 | 128 |
| 高さ | 44 |
| font | Noto Sans CJK JP,9 |
| text | Cancel |

(30) setting.ui という名前で保存します。

(31) pyuic5 を使って、Pythonのコードを生成します。

    $ pyuic5 setting.ui > setting_ui.py

### メインコードの作成手順

(1) メインのコード json1.py を作成します。

    $ vi json1.py

(2) 作成したメインのコードを実行します。

    $ python json1.py

