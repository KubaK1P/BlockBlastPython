from board import Board
from shapedisplay import ShapeDisplay
from shape import Shape
from random import randint
board: Board = Board(".")


def populate_choices() -> ShapeDisplay:
    return ShapeDisplay([Shape(randint(0, 7)) for n in range(3)])


def main():
    shape_display: ShapeDisplay = populate_choices()
    board.fill_board(0.9)
    for i in range(1, 7):
        board.show_board(False)
        shape_display.print_shapes()
        chosen_shape_no = int(input("Choose your shape (1, 2 or 3)"))
        board.show_shape(shape_display, chosen_shape_no)
        pos_x = int(input("Move the shape (x)"))
        pos_y = int(input("Move the shape (y)"))
        board.shape_x = pos_x
        board.shape_y = pos_y
        board.show_shape(shape_display, chosen_shape_no)
        confirm = int(input("Enter 1 to confirm, 0 to cancel"))
        if not confirm:
            board.sync_boards(False)
        else:
            board.place_shape(shape_display, chosen_shape_no)
            board.shape_x, board.shape_y = 0, 0
            shape_display.remove_shape(chosen_shape_no)
        if i % 3 == 0:
            shape_display = populate_choices()


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
