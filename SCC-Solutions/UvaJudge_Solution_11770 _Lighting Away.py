import sys
from sys import stdin
from collections import deque
sys.setrecursionlimit(10**6)

def dfs1(u):
 vis[u] = 1
 for v in R[u]:
  if vis[v] == 0:
   dfs1(v)
 d.appendleft(u)
 return
def dfs2(u,G):
 vis[u] = 1
 scc[u] = scc_cnt
 for v in G[u]:
  if vis[v] == 0:
   dfs2(v,G)
 return

def kosaraju(n, G):
 global R, vis, d, scc, scc_cnt, scc_indeg
 ans = 0
 R = [[] for i in range(n)]
 for u in range(n):
  for v in G[u]:
   R[v].append(u)
 d = deque()
 vis = [0 for i in range(n)]
 for u in range(n):
  if vis[u] == 0:
   dfs1(u)
 scc = [-1 for i in range(n)]
 scc_cnt = 0
 vis = [0 for i in range(n)]
 scc_indeg = [0 for i in range(100000)]
 for u in d:
  if vis[u] == 0:
   dfs2(u,G)
   scc_cnt += 1
 for i in range(n):
  for j in G[i]:
   if scc[j] != scc[i]:
    scc_indeg[scc[j]]+=1
 for i in range(scc_cnt):
  if scc_indeg[i] == 0:
   ans+=1
 return ans

def main():
 tc,c = int(sys.stdin.readline()),0
 blank = ""
 while c < tc:
  if blank == "" or blank =="\n":  	 
   nm = sys.stdin.readline().split(" ")
  else:
   nm = blank.split(" ")
  n,m = int(nm[0]),int(nm[1])
  G = [[] for i in range(n)]
  for i in range(m):
   edge = sys.stdin.readline().split(" ")
   a,b = int(edge[0])-1,int(edge[1])-1
   G[a].append(b)
  print("Case "+str(c+1)+":",kosaraju(n,G))
  try:blank = sys.stdin.readline()
  except: break
  c+=1
  
main()