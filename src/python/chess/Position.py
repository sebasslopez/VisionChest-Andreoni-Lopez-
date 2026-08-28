class Position:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self.WIDTH = 100

    @staticmethod
    def getAlgebraicNotation(row: int, col: int):
        return chr(col + 97) + str(8 - row)

    def isInside(self) -> bool:
        return self.row < 8 and self.row > -1 and self.col < 8 and self.col > -1

    def getXYPosition(self):
        return ((self.col * self.WIDTH), (self.row * self.WIDTH))

    def getBoundingBox(self):
        Axes = self.getXYPosition()
        return (Axes[0],Axes[1],Axes[0]+self.WIDTH,Axes[1]+self.WIDTH)

    def isTheSame(self,pos: "Position") -> bool:
        return pos.getXYPosition()[0] == self.getXYPosition()[0] and pos.getXYPosition()[1] == self.getXYPosition()[1]