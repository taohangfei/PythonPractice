import Piece
import Board
from collections import deque
'''
BFS implementation
Traverse from the starting positon
until find the destination position
'''
def bfs_traverse(piece,start,end):
    parent_dict = {}
    parent_dict [str(start)] = ''
    discovered_q = deque([start])
    if start==end:
        parent_dict[str(end)]=start
        return
    while discovered_q!=[]:
        n = discovered_q.popleft()
        children = piece.getValidMoves(n[0],n[1])
        for child in children:
            if str(child) not in parent_dict.keys():
                parent_dict[str(child)] = n
                if child!=end:
                    discovered_q.append(child)
                else:
                    discovered_q = []
                    break
    printPath(parent_dict,start,end)

'''
according to the parent tree, print the path out
'''
def printPath(p_dict,start,end):
    sen = []
    k = str(end)
    sen.append(num2letter(end))
    while p_dict[k]!=start:
        sen.append(num2letter(p_dict[k]))
        k = str(p_dict[k])
    sen.reverse()
    for i in sen:
        print i,
    print 

'''
transfering from input format to actual ord
'''
def letter2num(s):
    return [ord(s[0])-ord('A'),int(s[1])-1]
'''
transfering from postion ord to output format
'''
def num2letter(n):
    return chr(ord('A')+n[0])+str(n[1]+1)
    


import sys
if __name__ == "__main__":
    b = Board.Board(8,8)
    k = Piece.Knight(b,0,0)
    while(True):
        s_str,e_str = [letter2num(i) for i in sys.stdin.readline().strip().split()]
        bfs_traverse(k,s_str,e_str)
