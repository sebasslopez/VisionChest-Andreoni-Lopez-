from chess.pieces.Piece import Piece
from chess.Color import Color
from chess.Position import Position
import pygame



class Box:
    def __init__(self,piece:Piece | None, color: Color, position: Position):
        self.piece = piece
        self.COLOROG = color
        self.colorAC = color
        self.position = position
        pass

    def display(self,window:pygame.Surface):
        window.fill(self.getColor(),self.position.getBoundingBox())
        if self.piece != None:
            window.blit(self.piece.getTexture(),self.position.getXYPosition(),self.position.getBoundingBox())
    
    def isoccupied(self) -> bool:
        return self.piece != None

    def isEmpty(self) -> bool:
        return not self.isoccupied()

    def clearPiece(self):
        self.colorAC = self.COLOROG
        self.piece = None

    def setPiece(self, piece: Piece):
        self.clearPiece()
        self.piece = piece

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

    
