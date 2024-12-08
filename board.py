from math import floor
import os


class Board:
    def __init__(self, char: str) -> None:
        self.width = 9
        self.height = 9
        self.char = char
        self.board = [[char for i in range(self.width)]
                      for j in range(self.height)]

    def clear_board(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def show_board(self):
        self.clear_board()
        for i in range(self.width + 2):
            print("--", end="\t")

        print("\n")

        for i in self.board:
            print("|", end="\t")
            for j in i:
                print(j, end="\t")
            print("|")

        print("")
        for i in range(self.width + 2):
            print("--", end="\t")

    def change_cell_char(self, x: int, y: int, char: str):
        if x < 0 or y < 0 or x > self.width or y > self.height:
            raise IndexError(f"Values are out of bounds {x} {y}")

        self.board[self.height - floor(y) - 1][round(x)] = char

    def get_cell_char(self, x: int, y: int) -> str | None:
        if x < 0 or y < 0 or x > self.width or y > self.height:
            raise IndexError(f"Values are out of bounds {x} {y}")

        return self.board[self.height - floor(y) - 1][round(x)]
