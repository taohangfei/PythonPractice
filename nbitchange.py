def nbitchange(n):
    if n == 0:
        print "n can't be zero"
        return
    else:
        result = [0b0,0b1]
    for i in range(2,n+1):
        offset = 0b1<<(i-1)
        s_index = len(result) -1
        for k in range(s_index+1):
            result.append(result[s_index-k]+offset)
    for i in range(len(result)):
        print '0b'+bin(result[i])[2:].zfill(n)

n = int(raw_input())
nbitchange(n)
