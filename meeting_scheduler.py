class Meeting:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def __cmp__(self, other):
	return cmp(self.duration, other.duration)



def sched_meetings(l, mins):
	#l.sort(key = lambda x: x.duration)
	ls = sorted(l, key = lambda x: x.duration)
	s_m = []
	for m in ls:
		print m.name, m.duration
		if mins < m.duration:
			return s_m
		mins -= m.duration
		s_m.append(m)
	
	

m_3 = Meeting('m1', 40)
m_4 = Meeting('m2', 30)
m_5 = Meeting('m3', 45)
m_2 = Meeting('m4', 75)
m_1 = Meeting('m5', 120)
m_6 = Meeting('m6', 90)

L=[m_1, m_2, m_3, m_4, m_5, m_6]
x =  sched_meetings(L, 240)
print "##############"
for m in x:
	print m.duration, m.name


