from .Piece import Piece

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .. import Position,Board,Color

class Pawn(Piece):
    def __init__(self, color: Color.Color, position: Position.Position):
        super().__init__(color, position)

    def getPossibleMoves(self, board: "Board.Board") -> list["Position.Position"]:
        moves:list["Position.Position"] = []
        dirs = [1,-1]
        dir = dirs[self.color.value]
        OGpos = self.position.getXYPosition()
        pos = Position.Position(OGpos[0]+dir,OGpos[1])
        if(pos.isInside() and board.getBox(pos).isEmpty()):
            moves.append(pos)
            for i in dirs:
                pos = Position.Position(OGpos[0]+dir,OGpos[1]+i)
                box = board.getBox(pos)
                if(pos.isInside() and box.isoccupied() and not self.isTeamMate(box.piece)):
                    moves.append(pos)
            pos = Position.Position(OGpos[0]+dir*2,OGpos[1])
            if(pos.isInside() and board.getBox(pos).isEmpty() and self.hasMoved):
                moves.append(pos)
        else:
            for i in dirs:
                pos = Position.Position(OGpos[0]+dir,OGpos[1]+i)
                box = board.getBox(pos)
                if(pos.isInside() and box.isoccupied() and not self.isTeamMate(box.piece)):
                    moves.append(pos)
        return moves
