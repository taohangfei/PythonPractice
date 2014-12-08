def printPar(l,r,s,n,index):
    if l>n or r>n:
        print 'Out of Index'
        return None
    if l==n and r==n:
        print ''.join(s)
    else:
        if l<n:
            s[index]='('
            printPar(l+1,r,s,n,index+1)
        if r<l:
            s[index]=')'
            printPar(l,r+1,s,n,index+1)

if __name__=='__main__':
    while True:
        n=input()
        s=['']*(2*n)
        printPar(0,0,s,n,0)
