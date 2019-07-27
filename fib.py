def fib(n, memo = {}):
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
        return memo[n]
        

print "120th fib {}".format(fib(120))
    
