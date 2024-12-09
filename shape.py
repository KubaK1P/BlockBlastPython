from config import config


class Shape:
    def __init__(self, shape_id: int):
        self.id = shape_id
        if shape_id < 0:
            self.shape = []
        self.shape = config.get(f"config.shapes.{str(shape_id)}")
