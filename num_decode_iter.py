from collections import defaultdict

def nun_decodings(s):
	cache = defaultdict(int)
	cache[len(s)] = 1

	for i in reversed(range(len(s))):
		if s[i].startswith('0'):
			cache[i] = 0
		elif i == len(s) -1:
			cache[i] = 1
		else:
			cache[i] = cache[i+1]
			if int(s[i:i+2]) < 27:
				cache[i] += cache[i+2]

	print cache
	return cache[0]

#print nun_decodings("1413")
##print nun_decodings("1123")
#print nun_decodings("100")
print nun_decodings("122216")
