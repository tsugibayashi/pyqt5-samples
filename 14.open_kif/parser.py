#!/usr/bin/python3
# -*- coding: utf8 -*-
import codecs

class Parser:
    # consts
    [BLACK, WHITE] = range(2)

    # staticmethod はインスタンス化せずに直接呼び出すことができる
    @staticmethod
    def parse_file(filename, enc):
        with codecs.open(filename, 'r', enc) as f:
            return Parser.parse_str(f.read())

    # staticmethod はインスタンス化せずに直接呼び出すことができる
    @staticmethod
    def parse_str(kif_str):
        turn = Parser.BLACK

        moves = []
        line_num = 1
        # 読み込んだデータを改行文字で分割する
        for line in kif_str.split('\n'):
            # 空行、BOM (U+FEFF) のある行、または、コメント行のとき、処理しない
            if len(line) == 0 or line[0] == "\ufeff" or line[0] == "#":
                pass
            # ヘッダ行のとき、処理しない
            elif line[0:6] == "手数----":
                pass
            # '：' のある行は手数割や棋士名などが記載されるが、処理しない
            elif '：' in line:
                pass
            # それ以外の行には、指し手が書かれている
            else:
                # 半角スペースで分割し、指し手を取得する
                move = line.split(' ')

                # 投了と千日手のときは、指し手の先頭に記号を付けない
                if move[1] == '投了' or move[1] == '千日手':
                    moves.append(move[1])
                else:
                    # moves に指し手を追加する
                    if turn == Parser.BLACK:
                        moves.append('▲' + move[1])
                    else:
                        moves.append('△' + move[1])

                # 手番を切り替える
                turn = turn ^ 1

            line_num += 1
        
        return [moves]


### main routine
if __name__ == '__main__':
    filename = 'MyShogi_20201017105219.kif'

    kif = Parser.parse_file(filename, 'utf-8')[0]
    print(kif)

