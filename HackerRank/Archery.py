def findIndex(arr,start,end,ele):
    if arr[start]>ele:
        return start
    if arr[end]<ele:
        return end+1
    mid = (start+end)/2
    if arr[mid]<ele:
        return findIndex(arr,mid+1,end,ele)
    else:
        return findIndex(arr,start,mid-1,ele)


N = input()
radi_list = [int(i)**2 for i in raw_input().strip().split()]
radi_list.sort()
M = input()
count=0
for i in range(M):
    s=[int(j) for j in raw_input().strip().split()]
    s_distance = s[0]**2+s[1]**2
    e_distance = s[2]**2+s[3]**2
    s_index = findIndex(radi_list,0,N-1,s_distance)
    e_index = findIndex(radi_list,0,N-1,e_distance)
    count+=abs(s_index-e_index)
print count


