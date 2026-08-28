from .Piece import Piece

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .. import Position,Board,Color

class King(Piece):
    def __init__(self, color: Color.Color, position: Position.Position):
            super().__init__(color, position)
    
    def getPossibleMoves(self, board: "Board.Board") -> list["Position.Position"]:
        moves:list["Position.Position"] = []
        dirs = [-1,0,1]
        OGpos = self.position.getXYPosition()
        pos = Position.Position(OGpos[0],OGpos[1])
        for i in dirs:
             for j in dirs:
                pos = Position.Position(OGpos[0]+i,OGpos[1]+j)
                box = board.getBox(pos)
                if pos.isInside() and not pos.isTheSame(self.position) and (not self.check(pos,board,self.color)) and not self.isTeamMate(box.piece):
                    moves.append(pos)
        return moves

    def isCheckMate(self,board: "Board.Board"):
        return self.check(self.position,board,self.color) and not self.getPossibleMoves(board)

    @staticmethod
    def check(position:"Position.Position",board: "Board.Board",color:Color.Color) -> bool:
        for piece in board.getOpositePieces(color):
             for pos in piece.getPossibleMoves(board):
                if pos.isTheSame(position):
                    return False
        return True

    