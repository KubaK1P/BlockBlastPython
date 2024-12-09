from board import Board
from shapedisplay import ShapeDisplay
from shape import Shape
from random import randint
board: Board = Board(".")


def populate_choices() -> ShapeDisplay:
    return ShapeDisplay([Shape(randint(0, 7)), Shape(randint(0, 7)), Shape(randint(0, 7))])


shape_display: ShapeDisplay = populate_choices()


def main():
    board.fill_board(0.5)
    board.show_board(True)
    shape_display.print_shapes()
    board.show_shape(shape_display, 1, 3, 5)
    board.show_board(True)


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
