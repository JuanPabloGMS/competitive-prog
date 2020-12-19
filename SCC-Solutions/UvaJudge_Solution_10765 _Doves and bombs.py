import sys
from sys import stdin
sys.setrecursionlimit(10**6)

def dfs_tarjan(u):
 low[u] = depth[u]
 for v in G[u]:
  if depth[v] == -1:
   depth[v] = depth[u]+1
   papa[v] = u
   dfs_tarjan(v)
   low[u] = min(low[u],low[v])
   if low[v] >= depth[u]:
    comps[u] +=1
  elif  v == papa[u]:
   pass # u is in G[v] and depth[v]<depth[u]
  else: 
   low[u] = min(low[u],depth[v])
 return 

def main():
 global low, depth, papa, G, comps
 nm = sys.stdin.readline().split(" ")
 n,m = int(nm[0]),int(nm[1])
 while n != 0 and m!=0:
  G = [[] for _ in range(n)]
  edge = sys.stdin.readline().split(" ")
  x,y = int(edge[0]),int(edge[1])
  while x != -1 and y != -1:
   G[x].append(y)
   G[y].append(x)
   edge = sys.stdin.readline().split(" ")
   x,y = int(edge[0]),int(edge[1])
  low = [-1 for i in range(n)]
  depth = [-1 for i in range(n)]
  papa = [-1 for i in range(n)]
  comps = [1 for i in range(n)]
  comps[0] = 0
  for u in range(n):
   if depth[u] == -1:
    depth[u] = 0
    dfs_tarjan(u)
  maxim = max(comps)
  while m > 0 and maxim >= 1:
   for j in range(n):
    if comps[j] == maxim:
     print(j,maxim)
     m-=1
    if m <= 0:
     print("")
     break
   maxim-=1
  nm = sys.stdin.readline().split(" ")
  n,m = int(nm[0]),int(nm[1])
 

   
main()