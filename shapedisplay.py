from shape import Shape


class ShapeDisplay:
    def __init__(self, shapes: [Shape]):
        self.left = shapes[0]
        self.middle = shapes[1]
        self.right = shapes[2]

    def change_shapes(self, shapes: [Shape]):
        self.left = shapes[0]
        self.middle = shapes[1]
        self.right = shapes[2]

    # add linijki
    def print_shapes(self):
        lines: [str] = ["" for i in range(6)]
        lines[0] = lines[-1] = "-" * 100
        for i in range(1, 5):
            lines[i] += "".join(["+\t" if b ==
                                 1 else " \t" for b in self.left.shape[i - 1]])
            lines[i] += "|\t"
            lines[i] += "".join(["+\t" if b == 1
                                 else " \t" for b in self.middle.shape[i - 1]])
            lines[i] += "|\t"
            lines[i] += "".join(["+\t" if b == 1
                                 else " \t" for b in self.right.shape[i - 1]])
        for line in lines:
            print(line)

    def remove_shape(self, n: int):
        match n:
            case 1:
                self.left = Shape(-1)
            case 2:
                self.middle = Shape(-1)
            case 3:
                self.right = Shape(-1)
            case _:
                print("Provide a value between 1 and 3")
