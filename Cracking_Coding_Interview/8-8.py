columnForRow = [-1]*8

def check(row):
    for i in range (row):
        diff = abs(columnForRow[row]-columnForRow[i])
        if diff==0 or diff == row-i:
            return False    
    return True

def PlaceQueen(row):
    if row==8:
        print 'queen positon:',columnForRow
    else:
        for i in range(8):
            columnForRow[row]=i
            if check(row):
                PlaceQueen(row+1)

if __name__=='__main__':
    print columnForRow
    PlaceQueen(0)
