def knapsack(items, capacity, vals):
	n = len(items)-1
	if vals[n][capacity-1]:
		return vals[n][capacity]
	if n == 0 or capacity == 0:
		return 0
	elif items[n].duration >  capacity:
		result =  knapsack(items[:n-1], capacity, vals)
	else:
		temp1 = knapsack(items[:n-1], capacity, vals)
		temp2 = items[n] + knapsack(items[:n-1], capacity - items[n], vals)
		result = max(temp1, temp2)

	vals[n][capacity] = result
	return vals[n][capcaity]



class Meeting:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def __cmp__(self, other):
	return cmp(self.duration, other.duration)


m_3 = Meeting('m1', 40)
m_4 = Meeting('m2', 30)
m_5 = Meeting('m3', 45)
m_2 = Meeting('m4', 75)
m_1 = Meeting('m5', 120)
m_6 = Meeting('m6', 90)
L=[m_1, m_2, m_3, m_4, m_5, m_6]
n = len(L)
c = 240
vals = [[None for x in range(c)] for y in range(n)] 
x = knapsack(L, c, vals)  
print "##############"
for m in x:
	print m.duration, m.name

