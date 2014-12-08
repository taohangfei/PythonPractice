def by5cent(n):
    return n/5+1

def by10cent(n):
    return sum([by5cent(n-10*i) for i in range(n/10+1)])

def by25cent(n):
    return sum([by10cent(n-25*i) for i in range(n/25+1)])




def makeChange(n,denom,changes):
    next_d = nextDenom(changes,denom)
    if next_d ==0:
        return 1
    ways = 0
    for i in range(n/denom+1):
        ways+=makeChange(n-i*denom,next_d,changes)
    return ways

def nextDenom(changes,denom):
    index = changes.index(denom)
    return changes[index-1] if index>0 else 0

if __name__=='__main__':
    while True:
        n=input('n cents:')
        print 'The ways to represent:', by25cent(n)
        n=input('n cents:')
        changes=[int(i) for i in raw_input('change numbers:').strip().split()]
        print 'MakeChange ways:', makeChange(n,changes[-1],changes)
