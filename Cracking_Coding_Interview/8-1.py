fib = [0,1]
def Fibo(n,fib):
    if n<=len(fib):
        return fib[n-1]
    else:
        value = Fibo(n-1,fib)+Fibo(n-2,fib)
        fib.append(value)
        return value

if __name__=='__main__':
    while True:
        n=input()
        print 'The nth Fibo num is :', Fibo(n,fib)
