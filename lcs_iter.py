def lcs(str_one, str_two, len_one, len_two):
	lcs_matrix = [[0 for j in range(len_two+1)] for i in range(len_one+1)]
	print 
	for i in range(len_one+1):
		for j in range(len_two+1):
			if i == 0 or j == 0:
				lcs_matrix[i][j] = 0
			elif str_one[i-1] == str_two[j-1]:
				lcs_matrix[i][j] = lcs_matrix[i-1][j-1]+1
			else:
				lcs_matrix[i][j] = max(lcs_matrix[i-1][j], lcs_matrix[i][j-1])

	max_idx = lcs_matrix[len_one][len_two]
	print "max_idx=",max_idx
	if not max_idx:
		return "", 0
	lcs_str = [""]*(max_idx+1)
	lcs_str[max_idx]=""
	i = len_one
	j = len_two
	while i > 0 and j > 0:
		if str_one[i-1]  == str_two[j-1]:
			lcs_str[max_idx-1]=str_one[i-1]
			i -=1
			j -=1
			max_idx -=1
		elif lcs_matrix[i-1][j] > lcs_matrix[i][j-1]:
			i -= 1
		else: 
			j -=1
	return "".join(lcs_str), lcs_matrix[len_one][len_two]


lcs, lcs_len=lcs("MZJAWXU", "XMJYAUZ", len("MZJAWXU"), len("XMJYAUZ"))
print "lcs for MZJAWXU and XMJYAUZ", lcs, "with len=",lcs_len
