def allFibs(n):
    fibs =  [None] * n
    for i in range(n):
        print "{}th fib {}".format(i+1, fib(i, fibs))

def fib(n, fibs):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif  fibs[n] is not None:
        return fibs[n]

    fibs[n] = fib(n-1, fibs) + fib(n-2, fibs)
    return fibs[n]

allFibs(15)
    


