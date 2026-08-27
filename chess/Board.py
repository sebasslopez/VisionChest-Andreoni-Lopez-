from chess.Box import Box
import pygame
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from chess.pieces.Piece import Piece

class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.Pieces:list["Piece"] = []
        self.capturedPieces:list["Piece"] = []
        self.boxes:list[Box] = []
        self.isUpsideDown = False

    def display(self,window: pygame.Surface):
        for b in self.boxes:
            window.fill(b.getColor(),b.position.getBoundingBox())
        



        