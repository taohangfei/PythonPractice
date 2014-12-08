N = input()
tasks=[]
for i in range(N):
    s=raw_input().strip().split()
    task = (int(s[0]),float(s[1]))
    tasks.append(task)
def compare(i,j):
	if i[0]*(1-j[1])+j[0]*(i[1]-1)>0:
		return 1
	else:
		return -1
tasks.sort(cmp=compare)
#print tasks
def timeExpect(tasks):
    time = 0
    N = len(tasks)
    for i in range(N):
        T=tasks[i][0]
        P=1
        for j in range(i):
            P*=tasks[j][1]
        time+=T*P
    return time
time=timeExpect(tasks)
print time
