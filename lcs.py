def lcs(str_one, str_two,  m, n, memo):
	if memo[m][n]:
		return memo[m][n]
	if m == 0 or n == 0:
		result = 0
	elif str_one[m-1] == str_two[n-1]:
		result = 1 + lcs(str_one, str_two, m - 1, n - 1, memo)
	else:
		result_one = lcs(str_one, str_two, m-1 , n, memo)
		result_two = lcs(str_one, str_two, m, n-1, memo)
		result = max(result_one, result_two)

	memo[m][n] = result
	return result


str_one = "abcdxyz"
str_two = "abcdpxyzl"
memo = [[None for x in range(len(str_two)+1)] for y in range(len(str_one)+1)]
print lcs(str_one, str_two, len(str_one), len(str_two), memo)

