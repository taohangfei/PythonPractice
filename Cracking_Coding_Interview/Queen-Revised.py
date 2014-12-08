colForRow=[-1]*1000

def PlaceQueue(row,N):
    if row==N:
        print [i+1 for i in colForRow[:N]]
    else:
        for i in range(N):
            colForRow[row]=i
            if check(row):
                PlaceQueue(row+1,N)

def check(row):
    diffangel = set()
    for i in range(row):
        diff=abs(colForRow[i]-colForRow[row])
        if diff == 0 or diff == row - i:
            return False
    return True

if __name__=='__main__':
    import sys
    PlaceQueue(0,int(sys.argv[1]))
