'''
Board class, a square displaying the pieces on board
'''
class Board:
    def __init__(self,x=8,y=8):
        self.x_range = x
        self.y_range = y
        self.initBoard()
    def initBoard(self):
        self.board = [['*']*self.x_range for i in range(self.y_range)]
    def getPiece(self,x,y):
        if(x>=0 and x<self.x_range and y>=0 and y<self.y_range):
            return self.board[x][y]
        else:
            print 'Out of range'
            return None
    def movePiece(self,piece,x,y):
        self.board[piece.ord_x][piece.ord_y] = '*'
        self.board[x][y] = piece.p_type

    def setPiece(self,x,y,p_type):
        self.board[x][y] = p_type

    def printBoard():
        for r in self.board:
            for e in r:
                print e,
            print
