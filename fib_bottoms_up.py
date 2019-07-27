def fib(n):
	if n==1 or n==2:
		return 1
	fibs = [None]*(n+1)
	fibs[1] = 1	
	fibs[2] = 1	
	for i in range(3,n+1):
		fibs[i] = fibs[i-1] + fibs[i-2]

	return fib[n]
