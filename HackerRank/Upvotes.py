N,K = [int(i) for i in raw_input().split()]
ints = [int(i) for i in raw_input().split()]
def nonDecreasing(arr,s,l):
    n_d_list=[]
    start=s
    end=s
    count=0
    while start<l-1:
        while start<l-1 and arr[start]>arr[start+1]:
    		start+=1
        if start<l-1:
    	    end=start+1
        else:
            end=start
    	while end<l-1 and arr[end]<=arr[end+1]:
    		end+=1
    	#r = end-start+1
        #print 'non Decresing start is %d,end is %d' %(start,end)
        if start!=end:
            n_d_list.append((start,end))
    	#count+=r*(r-1)/2
    	start=end+1
    return n_d_list
def nonIncreasing(arr,s,l):
    n_i_list=[]
    start=s
    end=s
    count=0
    while start<l-1:
    	while start<l-1 and arr[start]<arr[start+1]:
    		start+=1
        if start<l-1:
    	    end=start+1
        else:
            end=start
    	while end<l-1 and arr[end]>=arr[end+1]:
    		end+=1
        if start!=end:
            n_i_list.append((start,end))
    	#r = end-start+1
        #print 'non Increasing start is %d,end is %d' %(start,end)
    	#count+=r*(r-1)/2
    	start=end+1
    return n_i_list

n_d_list=nonDecreasing(ints,0,N-1)
n_i_list=nonIncreasing(ints,0,N-1)


d=0
j=0
for i in range(N-K+1):
    #print 'windows is:',i,i+K-1
    n_d=0
    while d<len(n_d_list):
        if n_d_list[d][1]<=i:
            d+=1
        else:
            break
    d_d = d
    while d_d<len(n_d_list):
        if n_d_list[d_d][1]>i and n_d_list[d_d][0]<i+K-1:
            r=min(n_d_list[d_d][1],i+K-1)-max(n_d_list[d_d][0],i)+1
            #print 'range is: ',n_d_list[d_d]
            #print 'radi is: ',r
            n_d+=r*(r-1)/2
            d_d+=1
        else:
            break
    n_i=0
    while j<len(n_i_list):
        if n_i_list[j][1]<=i:
            j+=1
        else:
            break
    j_j=j
    while j_j<len(n_i_list):
        if n_i_list[j_j][1]>=i and n_i_list[j_j][0]<=i+K-1:
            r=min(n_i_list[j_j][1],i+K-1)-max(n_i_list[j_j][0],i)+1
            n_i+=r*(r-1)/2
            j_j+=1
        else:
            break
    print n_d-n_i
