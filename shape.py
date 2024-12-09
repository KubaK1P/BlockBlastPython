class Shape:
    def __init__(self, shape_id: int):
        self.id = shape_id
        match shape_id:
            case 0:
                self.shape = [[1]]
            case 1:
                self.shape = [[1, 1], [1, 1]]
            case 2:
                self.shape = [[1, 0], [1, 1], [0, 1]]
            case 3:
                self.shape = [[0, 1], [1, 1], [1, 0]]
            case 4:
                self.shape = [[0, 1, 1], [1, 1, 0]]
            case 5:
                self.shape = [[1, 1, 0], [0, 1, 1]]
            case 6:
                self.shape = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
