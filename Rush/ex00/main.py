#!/usr/bin/env python3

def create_chessboard(rows, columns):
    for row in range(rows):
        print(".", end = " ")
        for column in range(columns):
            print(".", end = " ")
        print()

create_chessboard(8, 7)
