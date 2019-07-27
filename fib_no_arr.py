def fib(n):
	a = 1
	b = 1
	if n == 1 or n == 2:
		return a
	else:
		for i in range (3, n+1):
			c = a+b
			a = b
			b = c
	return b


print fib(9)
