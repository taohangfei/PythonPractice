class Solution:
    # @param grid, a list of list of characters
    # @return an integer
    def numIslands(self, grid):
        if not grid:
            return 0
        width = len(grid[0])
        height = len(grid)
        stop = dict.fromkeys([i for i in range(height)],0)
        result = 0
        for i in range(height):
            print "result is:",result
            printGrid(grid)
            while stop[i]<width:
                j = stop[i]
                if grid[i][j]=="1":
                    result +=1
                    lists = [-1]
                    while j<width and grid[i][j]=="1":
                        lists.append(j)
                        print "%d,%d turn over" %(i,j)
                        grid[i][j] = "0"
                        j+=1
                    stop[i] = j
                    for k in range(i+1,height):
                        if len(lists)<=1:
                            break
                        lists2 = [-2]
                        for l in lists[1:]:
                            if grid[k][l]=="1":
                                print "%d,%d turn over" %(k,l)
                                grid[k][l]="0"
                                lists2.append(l)
                                offset = 1
                                while l-offset>=0 and grid[k][l-offset]=="1":
                                    print "%d,%d turn over" %(k,l-offset)
                                    grid[k][l-offset]="0"
                                    lists2.append(l-offset)
                                    offset +=1
                                offset = 1
                                while l+offset<width and grid[k][l+offset]=="1":
                                    print "%d,%d turn over" %(k,l+offset)
                                    grid[k][l+offset]="0"
                                    lists2.append(l+offset)
                                    offset +=1
                        lists = lists2
                else:
                    stop[i]+=1
        print "result is",result
        printGrid(grid)
        return result

def printGrid(grid):
    for i in grid:
        print i

a = Solution()
print a.numIslands([list(i) for i in ["10111","10101","11101"]])