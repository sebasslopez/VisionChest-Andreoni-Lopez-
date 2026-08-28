from .Box import Box
from .Color import Color
from .Position import Position
import pygame
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .pieces import Piece,Pawn#,King,Knight,Rook,Bishop,Queen

class Board:
    def __init__(self):
        self.board:list[list[Box]] = self.createBoard(False)
        self.boxes:list[Box] = []
        self.Pieces:list["Piece.Piece"] = []
        self.capturedPieces:list["Piece.Piece"] = []
        self.isUpsideDown = False

    def display(self,window: pygame.Surface):
        for b in self.boxes:
            b.display(window)

    def createBoard(self,flag:bool) -> list[list[Box]]:
        board:list[list[Box]] = []
        for i in range(0,7):
            row:list[Box] = []
            for j in range(0,7):
                p: Piece.Piece = self.createPiece(i,j,flag)
                b: Box = Box(p,self.getBoxColor(i,j),Position(i,j))
                row.append(b)
                self.boxes.append(b)
                self.Pieces.append(p)

            board.append(row)
        return board

    @staticmethod
    def getBoxColor(row:int,column:int) -> Color:
        return Color.WHITE if (row * 8 + column) % 2 == 0 else Color.BLACK

    def getBox(self,position: Position) -> Box:
        pos = position.getXYPosition()
        return self.board[pos[0]][pos[1]]

    def getOpositePieces(self,color:Color) -> list[Piece.Piece]:
        l:list[Piece.Piece] = []
        for p in self.Pieces:
            if(p.color != color):
                l.append(p)
        return l
    


    @staticmethod
    def createPiece(row: int,column:int,flag:bool)-> Piece.Piece:
        color: Color = Color.WHITE if flag else Color.BLACK
        if(row * 8 + column <= 32):
            return Pawn.Pawn(color,Position(row,column))  
        color = Color.BLACK if flag else Color.WHITE
        return Pawn.Pawn(color,Position(row,column))