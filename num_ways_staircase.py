# n = num stair cases
# x = list of allowed steps = [1,2,3] => can take 1,2 or, 3 steps at a time.
def num_ways(n, x):
	if n == 0:
		return 1
	result = 0
	for i in x:
		if n - i >= 0:
			result += num_ways(n-i, x)
	return result


def num_ways_bot_up(n, x):
	if n == 0:
		return 1

	nums = [None] *(n+1)
	nums[0] = 1
	for i in range(1, n):
		result = 0
		for j in x:
			if i-j >= 0:
				result += num[i-j]
		nums[i] = total

	return nums[n]
