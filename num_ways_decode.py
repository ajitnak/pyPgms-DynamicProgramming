def num_ways(data):
	memo = [None] * (len(data)+1)
	return num_ways_helper(data, len(data), memo)

def num_ways_helper(data, k, memo):
	#print "single digit : k={}".format(k)
	if k == 0:
		return 1
	s = len(data) - k
	if data[s] == '0':
		return 0
	if memo[k] != None:
		print "using stored val at idx={} result={}".format(k, memo[k])
		return memo[k]
	result = num_ways_helper(data, k-1, memo)
	if k>=2 and int(data[s:s+2]) <= 26:
		#print "loop start idx = {} num={} result={}".format(s, data[s:s+2], result)
		result += num_ways_helper(data, k-2, memo)
		print "double digit: result = {}".format(result)
	print "saving at idx={} result={}".format(k, result)
	memo[k] = result
	return result
	

n = num_ways("110")
print n


#"1110" => [1,1,10] amd [11, 10] => 2
#"1113" => [1,1,1,3] , [1,1, 13]  [1, 11, 3] [11,1,3], [11,13] => 5


