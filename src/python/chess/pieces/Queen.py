from .Piece import Piece

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .. import Position,Board,Color

class Queen(Piece):
    def __init__(self, color: Color.Color, position: Position.Position):
            super().__init__(color, position)
    
    def getPossibleMoves(self, board: "Board.Board") -> list["Position.Position"]:
        moves:list["Position.Position"] = []
        dirs = [1,-1]
        OGpos = self.position.getXYPosition()
        pos = Position.Position(OGpos[0],OGpos[1])
        for i in dirs:
            for j in dirs:
                pos = Position.Position(OGpos[0]+i,OGpos[1]+j)
                box = board.getBox(pos)
                while pos.isInside() and box.isEmpty():
                    moves.append(pos)
                    pos = Position.Position(pos.getXYPosition()[0]+i,pos.getXYPosition()[1]+j)
                    box = board.getBox(pos)
                if(pos.isInside() and not self.isTeamMate(box.piece)):
                        moves.append(pos)
        for i in dirs:
            pos = Position.Position(OGpos[0]+i,OGpos[1])
            box = board.getBox(pos)
            while pos.isInside() and box.isEmpty():
                moves.append(pos)
                pos = Position.Position(pos.getXYPosition()[0]+i,OGpos[1])
                box = board.getBox(pos)
            if(pos.isInside() and not self.isTeamMate(box.piece)):
                    moves.append(pos)
        for i in dirs:
            pos = Position.Position(OGpos[0],OGpos[1]+i)
            box = board.getBox(pos)
            while pos.isInside() and box.isEmpty():
                moves.append(pos)
                pos = Position.Position(OGpos[0],pos.getXYPosition()[1]+i)
                box = board.getBox(pos)
            if(pos.isInside() and not self.isTeamMate(box.piece)):
                    moves.append(pos)
        return moves
