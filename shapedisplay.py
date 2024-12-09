from shape import Shape


class ShapeDisplay:
    def __init__(self, shapes: [Shape]):
        self.shape_left = shapes[0]
        self.shape_middle = shapes[1]
        self.shape_right = shapes[2]

    def change_shapes(self, shapes: [Shape]):
        self.shape_left = shapes[0]
        self.shape_middle = shapes[1]
        self.shape_right = shapes[2]

    # add linijki
    def print_shapes(self):
        for i in range(len(self.shape_left.shape)):
            for j in range(len(self.shape_left.shape[i])):
                if not self.shape_left.shape[i][j]:
                    print(" ", end="\t")
                else:
                    print("+", end="\t")
            print("\n")
        print("-" * 20)
        for i in range(len(self.shape_middle.shape)):
            for j in range(len(self.shape_middle.shape[i])):
                if not self.shape_middle.shape[i][j]:
                    print(" ", end="\t")
                else:
                    print("+", end="\t")
            print("\n")
        print("-" * 20)
        for i in range(len(self.shape_right.shape)):
            for j in range(len(self.shape_right.shape[i])):
                if not self.shape_right.shape[i][j]:
                    print(" ", end="\t")
                else:
                    print("+", end="\t")
            print("\n")
        print("-" * 20)
