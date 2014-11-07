import Board
class Piece:
    '''
    Piece on board
    '''
    def __init__(self,board,x,y,p_type=''):
        self.ord_x = x
        self.ord_y = y
        self.p_type = p_type
        self.board = board
        self.board.setPiece(x,y,p_type)
    def getPos(self):
        return ord_x,ord_y
    def getType(self):
        return p_type
    def getValidMove(self):
        return
    def move(self,x,y):
        if self.isMoveValid(x,y):
            self.board.movePiece(self,x,y)
            self.ord_x = x
            self.ord_y = y
        else:
            print 'Out of rane'
    def isMoveOnBoard(self,x,y):
        if x<0 or y<0 or x>=self.board.x_range or y>=self.board.y_range:
            return False
        else:
            return True

class Knight(Piece):
    offset = [[+2,-1],[-2,-1],[+2,+1],[+2,-1],[-1,+2],[-1,-2],
            [+1,+2],[+1,-2]]
    '''
    Knight Piece, which extends Piece, with its
    specific move rules
    '''
    def __init__(self,board, x,y):
        Piece.__init__(self,board,x,y,'K')
    '''
    define valid moves by Knight
    '''
    def getValidMoves(self,x,y):
        moves = []
        for off in self.offset:
            move_x = x+off[0]
            move_y = y+off[1]
            if self.isMoveOnBoard(x,y):
                moves.append([move_x,move_y])
        return moves
