class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if not board:
            return
        for i in board:
            print i
        width = len(board[0])
        height = len(board)
        turnover= []
        for i in range(height):
            for j in [0,width-1]:
                if board[i][j]=="O":
                    board[i][j]="D"
                    turnover.append([i,j])
        for i in [0,height-1]:
            for j in range(width):
                if board[i][j]=="O":
                    board[i][j]="D"
                    turnover.append([i,j])
        while turnover:
            i,j = turnover.pop()
            print "%d,%d"%(i,j)
            if i-1>=0:
                if board[i-1][j]=="O":
                    board[i-1][j]="D"
                    turnover.append([i-1,j])
            if i+1<len(board):
                if board[i+1][j]=="O":
                    board[i+1][j]="D"
                    turnover.append([i+1,j])
            if j-1>=0:
                if board[i][j-1]=="O":
                    board[i][j-1]="D"
                    turnover.append([i,j-1])
            if j+1<len(board[0]):
                if board[i][j+1]=="O":
                    board[i][j+1]="D"
                    turnover.append([i,j+1])
        for i in range(height):
            for j in range(width):
                if board[i][j]=="D":
                    board[i][j]="O"
                else:
                    board[i][j]="X"
        print "converted:"
        for i in board:
            print i

    

        
a=Solution()
a.solve([list(i) for i in ["OOO","OOO","OOO"]])