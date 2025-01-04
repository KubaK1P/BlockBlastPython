from shape import Shape
from shapedisplay import ShapeDisplay
import os
from random import random


class Board:
    def __init__(self, char: str) -> None:
        self.width = 9
        self.height = 9
        self.char = char
        self.board_state = [[char for i in range(self.width)]
                            for j in range(self.height)]
        self.board = [[char for i in range(self.width)]
                      for j in range(self.height)]

    def clear_board(self, char: str):
        self.board_state = [[char for i in range(self.width)]
                            for j in range(self.height)]
        self.board = [[char for i in range(self.width)]
                      for j in range(self.height)]

    def clear_screen(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def show_board(self, force: bool):

        for i in range(self.width + 2):
            print("--", end="\t")

        print("\n")
        if force:
            for i in self.board_state:
                print("|", end="\t")
                for j in i:
                    print(j, end="\t")
                print("|")
        else:
            for i in self.board:
                print("|", end="\t")
                for j in i:
                    print(j, end="\t")
                print("|")

        print("")
        for i in range(self.width + 2):
            print("--", end="\t")
        print("")

    def set_cell_char(self, x: int, y: int, char: str, force=False):
        if x < 0 or y < 0 or x > self.width or y > self.height:
            raise IndexError(f"Values are out of bounds {x} {y}")
        if force:
            self.board_state[y][x] = char
        else:
            self.board[y][x] = char

    def get_cell_char(self, x: int, y: int, force=False) -> str | None:
        if x < 0 or y < 0 or x > self.width or y > self.height:
            raise IndexError(f"Values are out of bounds {x} {y}")
        if force:
            return self.board_state[y][x]
        else:
            return self.board[y][x]

    def fill_board(self, treshold: float):
        for i in range(self.width):
            for j in range(self.height):
                if random() > treshold:
                    self.set_cell_char(i, j, "1", True)
                    self.set_cell_char(i, j, "1", False)

    def show_shape(self, sd: ShapeDisplay, n: int, x: int, y: int):
        # get the chosen Shape object
        chosen_shape: Shape
        match n:
            case 1:
                chosen_shape = sd.left
            case 2:
                chosen_shape = sd.middle
            case 3:
                chosen_shape = sd.right
            case _:
                raise IndexError("Specify value between 1 and 3")
        print(chosen_shape.shape)
        # show the shape on the board at (x, y)
        self.set_cell_char(x, y, "+", False)
        self.show_board(False)
