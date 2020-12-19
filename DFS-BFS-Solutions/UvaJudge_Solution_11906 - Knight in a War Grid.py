import sys
from sys import stdin
from collections import deque

R,C,M,N = 0,0,0,0
visited = [[False for _ in range(110)] for _ in range(110)]
board = [[0 for _ in range(110)] for _ in range(110)]
dr = [1,-1,1,-1]
dc = [1,1,-1,-1]


def bfs(row, col):
 global visited,board
 q = deque()
 q.append((row,col))
 visited[row][col] = True
 while q:
  row,col = q.popleft()
   #check for row_i*M col_i*N
  for i in range(4):
   mi,ni = 0,0
   if   M!=0 and N!=0:
    mi,ni = row+dr[i]*M,col+dc[i]*N
   else:
   	if i < 2:
   	 mi,ni = row+dr[i]*M,col+dr[i]*N
   	else:
   	 mi,ni = row+dr[i]*N,col+dr[i]*M
   if mi >= 0 and mi < R and ni >= 0 and ni < C and board[mi][ni] != -1:
    board[row][col]+=1
    if(visited[mi][ni] == False):
     visited[mi][ni] = True
     q.append((mi,ni))

   #check for row_i*N col_i*N
  if(M!=N and M!=0 and N!=0):
   for i in range(4):
    mi,ni = row+dr[i]*N,col+dc[i]*M
    if mi >= 0 and mi < R and ni >= 0 and ni < C and board[mi][ni] != -1:
     board[row][col]+=1
     if(visited[mi][ni] == False):
      visited[mi][ni] = True
      q.append((mi,ni))
   


def solve():
 even,odd = 0,0
 for i in range(R):
  for j in range(C):
   if board[i][j]%2 == 0 and board[i][j] > 0:
    even+=1
   elif board[i][j]%2 != 0 and board[i][j] > 0:
    odd+=1
 if even == 0 and odd == 0:
 	even = 1
 return even,odd
 

def main():
 global R,C,M,N,visited,board
 tc = int(sys.stdin.readline())
 c = 1
 while tc > 0:
  inp = sys.stdin.readline().split(" ")
  R,C,M,N = int(inp[0]),int(inp[1]),int(inp[2]),int(inp[3])
  W = int(sys.stdin.readline())
  board = [[0 for _ in range(C)] for _ in range(R)]
  visited = [[False for _ in range(C)] for _ in range(R)]
  while W > 0:
   inp = sys.stdin.readline().split(" ")
   i,j = int(inp[0]),int(inp[1])
   board[i][j] = -1
   W-=1
  bfs(0,0)
  e,o = solve()
  print("Case "+str(c)+": "+str(e)+" "+str(o))
  tc-=1
  c+=1 
main()

