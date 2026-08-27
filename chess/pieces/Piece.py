from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from chess import Position,Board,Color

class Piece(ABC):
    def __init__(self, color: "Color.Color", position: "Position.Position"):
        self.color:"Color.Color" = color
        self.position = position
        self.hasMoved = False
        self.isCaptured = False
        self.boxColor = 0xFFFFFF #llamaria a un metodo que devuelva el color del cuadro de una posicion del tablero, segun si el mapa está al reves o no.

    @abstractmethod
    def canMove(self, newPosition: "Position.Position", board: "Board.Board") -> bool:
        return False

    @abstractmethod
    def getPossibleMoves(self, board: "Board.Board") -> list["Position.Position"]:
        return []

    @abstractmethod
    def isMoveValid(self, newPosition: "Position.Position", board: "Board.Board") -> bool:
        return False

    @abstractmethod
    def move(self, newPosition: "Position.Position", board: "Board.Board"):
        self.hasMoved = True
        pass

    def capture(self):
        self.isCaptured = True

    def isTeamMate(self, otherPiece: "Piece") -> bool:
        return self.color == otherPiece.color

    def getTexture(self) -> str:
        return f"{self.color}_{self.__class__.__name__.lower()}.png"