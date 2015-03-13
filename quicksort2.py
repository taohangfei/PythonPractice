def quicksort(alist):
    quickSortHelper(alist,0,len(alist)-1)


def quickSortHelper(alist,first,last):
    if first<last:
        splitpoint = partition(alist,first,last)

        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,fist,last):
    pivotvalue = alist[first]
    l_mark = first + 1
    r_mark = last
    done = False
    while not done:
        while l_mark<=r_mark and alist[l_mark]<=pivotvalue:
            l_mark = l_mark +1
        while alist[r_mark]>=pivotvalue and r_mark>=l_mark:
            r_mark = r_mark -1
        
        if r_mark < l_mark:
            done = True
        else:
            temp = alist[l_mark]
            alist[l_mark] = alist[r_mark]
            alist[r_mark] = temp

    temp = alist[first]
    alist[first] = alist[r_mark]
    alist[r_mark] = temp

    return r_mark

def partition2(alist,first,last,pivot):
    l_mark = first
    r_mark = last
    done = False
    pivot_index = first
    left = True
    while not done:
        while l_mark<=r_mark and alist[l_mark]<=pivot:
            if alist[l_mark] == pivot:
                pivot_index = l_mark
            l_mark+=1
        while alist[r_mark]>=pivot and r_mark>=l_mark:
            if alist[r_mark] == pivot:
                left = False
                pivot_index = r_mark
            r_mark+=1
        
        if r_mark < l_mark:
            done = True
        else:
            temp = alist[l_mark]
            alist[l_mark] = alist[r_mark]
            alist[r_mark] = temp
    if left:
        change = r_mark
    else:
        change = l_mark
    alist[pivot_index] = alist[change]
    alist[change] = pivot
    return change

def quicksortHelper2(alist,blist,first,last,s_p):
    if first<last:
        #quicksort alist and blist
        splitpoint = partition2(alist,first,last,blist[s_p])
        partition2(blist,first,last,alist[splitpoint])

        quickSortHelper2(alist,first,splitpoint-1,splitpoint-1)
        quickSortHelper2(alist,splitpoint+1,last,splitpoint+1)
    return True

def quicksort2(alist,blist):
    if len(alist)!=len(blist):
        return False
    return quicksortHelper2(alist,blist,0,len(alist),0)




