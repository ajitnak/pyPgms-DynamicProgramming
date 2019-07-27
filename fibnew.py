def fib(n):
	fibs = {}
	for k in range(1, n+1):
		if k <= 2:
			fibs[k] = 1
		else:
			fibs[k] = fibs[k-1] + fibs[k-2]
	return fibs 

print "first 20 fibs: {}".format(fib(20))
