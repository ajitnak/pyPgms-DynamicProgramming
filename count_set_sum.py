#find the number of subsets in an array which can add up to a given number.
def count_subsets(arr, sum):
	memo = {}
	return count_subsets_helper(arr, sum, len(arr) - 1, memo)


def count_subsets_helper(arr, sum, idx, memo):
	key = str(sum)+ ":" + str(idx)
	if memo.get(key):
		return memo.get(key)
	if sum == 0: # empty subset {}
		return 1
	if sum < 0:
		return 0
	if idx < 0:
		return 0

	if sum < arr[idx]:
		result = count_subsets_helper(arr, sum, idx - 1, memo)
	else:
		result = count_subsets_helper(arr, sum-arr[idx], idx - 1, memo) +  count_subsets_helper(arr, sum, idx - 1, memo)
	memo[key] = result
	return result

print count_subsets([2,7,10,8,4], 14)
