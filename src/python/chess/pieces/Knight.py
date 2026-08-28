from .Piece import Piece

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .. import Position,Board,Color

class Knight(Piece):
    def __init__(self, color: Color.Color, position: Position.Position):
            super().__init__(color, position)
    
    def getPossibleMoves(self, board: "Board.Board") -> list["Position.Position"]:
        moves:list["Position.Position"] = []
        dirsf = [1,-1,-2,2]
        dirsc = [-2,2,1,-1]
        OGpos = self.position.getXYPosition()
        pos = OGpos
        for i in range(0,2):
            for j in range(0,2):
                pos = Position.Position(OGpos[0]+dirsf[j],OGpos[1]+dirsc[i])
                if pos.isInside():
                    box = board.getBox(pos)
                    if box.isEmpty() or not self.isTeamMate(box.piece):
                        moves.append(pos)
        for i in range(2,4):
            for j in range(2,4):
                pos = Position.Position(OGpos[0]+dirsf[j],OGpos[1]+dirsc[i])
                if pos.isInside():
                    box = board.getBox(pos)
                    if box.isEmpty() or not self.isTeamMate(box.piece):
                        moves.append(pos)
        return moves