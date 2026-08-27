from chess.pieces.Piece import Piece
from chess.Color import Color
from chess.Position import Position



class Box:
    def __init__(self,piece:Piece | None, color: Color, position: Position):
        self.piece = piece
        self.colorOG = color
        self.colorAC = color
        self.position = position
        pass

    def getColor(self):
        if self.colorAC == Color.WHITE:
            return (255,255,255)
        elif self.colorAC == Color.BLACK:
            return (0,0,0)
        elif self.colorAC == Color.GREEN:
            return (0,255,0)
        elif self.colorAC == Color.BLUE:
            return (0,0,255)
        elif self.colorAC == Color.RED:
            return (255,0,0)
        return (123,23,85)

    
