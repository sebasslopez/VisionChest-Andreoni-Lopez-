from chess.Box import Box
import pygame
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from chess.pieces.Piece import Piece

class Board:
    def __init__(self):
        self.board:list[list[Box]] = []
        self.Pieces:list["Piece"] = []
        self.capturedPieces:list["Piece"] = []
        self.boxes:list[Box] = []
        self.isUpsideDown = False

    def display(self,window: pygame.Surface):
        for b in self.boxes:
            window.fill(b.getColor(),b.position.getBoundingBox())

    def createBoard(self,flag:bool) -> list[list[Box]]:
        board:list[list[Box]] = []
        for i in range(0,7):
            row:list[Box] = []
            for j in range(0,7):
                if 
                row.append(Box(Piece()))

        return []


        



        