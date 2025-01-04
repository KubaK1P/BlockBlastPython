from config import config


class Shape:
    def __init__(self, shape_id: int):
        self.id = shape_id
        if shape_id < 0:
            self.shape = []
        self.shape = config.get(f"config.shapes.{str(shape_id)}")
        self.height = 0
        self.width = 0

        for row in self.shape:
            try:
                last_index = len(row) - 1 - row[::-1].index(1)
            except ValueError:
                self.height = self.shape.index(row)
            if last_index + 1 > self.width:
                self.width = last_index + 1
