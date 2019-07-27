def decode_str(s):
	memo = [None]*(len(s) + 1)
	return decode_helper(s, len(s), memo)

def decode_helper(str, k, memo):
	if k == 0:
		return 1
	s = len(str) - k
	if str[s] == '0':
		return 0
	if memo[k] is not None:
		return memo[k]
	result = decode_helper(str, k-1, memo)
	if k>=2 and int(str[s:s+2]) < 27:
		result += decode_helper(str, k-2, memo)
	memo[k] = result
	return result

#print decode_str("1413")
#print decode_str("1123")
#print decode_str("100")
print decode_str("123416")

