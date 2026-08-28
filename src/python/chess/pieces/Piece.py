from abc import ABC, abstractmethod
import pygame
from utils.ResourceLocation import getImage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from chess import Position,Board,Color

class Piece(ABC):
    def __init__(self, color: "Color.Color", position: "Position.Position"):
        self.color:"Color.Color" = color
        self.position = position
        self.hasMoved = False
        self.isCaptured = False
    
    @abstractmethod
    def getPossibleMoves(self, board: "Board.Board") -> list["Position.Position"]:
        return []

    def isMoveValid(self, newPosition: "Position.Position", board: "Board.Board") -> bool:
            moves:list["Position.Position"] = self.getPossibleMoves(board)
            return newPosition in moves
    
    def move(self, newPosition: "Position.Position", board: "Board.Board"):
        self.hasMoved = True
        box = board.getBox(newPosition)
        if(box.isEmpty() or box.piece == None):
            box.setPiece(self)
        else:
            box.piece.capture(board)
            box.setPiece(self)
        pass

    def capture(self,board: "Board.Board"):
        self.isCaptured = True
        board.capturedPieces.append(self)

    def isTeamMate(self, otherPiece: "Piece | None") -> bool:
        if otherPiece == None:
            return False
        return self.color == otherPiece.color

    def getTexture(self) -> pygame.Surface:
        return getImage(f"{self.color}_{self.__class__.__name__.lower()}")

    def getOpositeColor(self) -> Color.Color:
        return Color.Color.WHITE if self.color == Color.Color.BLACK else Color.Color.BLACK