from board import Board
from random import random

board: Board = Board(".")


def fill_board(board_inst: Board, treshold: float):
    for i in range(board_inst.width):
        for j in range(board_inst.height):
            if random() > treshold:
                board_inst.change_cell_char(i, j, "1")


def main():
    fill_board(board, 0.5)
    board.show_board()


if __name__ == "__main__":
    print("Block Blast\n")
    try:
        choice: int = int(input("Play --\t--1\n\nQuit --\t--0\n"))
    except ValueError:
        choice = "invalid"

    match choice:
        case 0:
            print("GoodBye")
        case 1:
            main()
        case _:
            print("invalid choice")
