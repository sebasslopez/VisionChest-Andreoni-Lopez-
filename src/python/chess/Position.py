class Position:
    def __init__(self, row: int, col: int, width: int):
        self.row = row
        self.col = col
        self.width = width

    @staticmethod
    def getAlgebraicNotation(row: int, col: int):
        return chr(col + 97) + str(8 - row)

    def getXYPosition(self):
        return ((self.col * self.width), (self.row * self.width))

    def getBoundingBox(self):
        Axes = self.getXYPosition()
        return (Axes[0],Axes[1],Axes[0]+self.width,Axes[1]+self.width)