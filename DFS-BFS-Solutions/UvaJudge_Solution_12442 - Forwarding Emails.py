import sys
from sys import stdin

T,N,m,mu = 0,0,0,0
visited,f,c = [False for _ in range(50000)],[0 for _ in range(50000)],[0 for _ in range(50000)]

def dfs(u):
 global T,N,m,mu,visited,f,c
 v,r = f[u],0
 if visited[v] == False:
  r = dfs(v)+1
 visited[u] = 0
 c[u] = r
 return r
def main():
 global T,N,m,mu,visited,f,c
 t,i,u,v,ci = 0,0,0,0,1
 T = int(sys.stdin.readline())
 while (T > 0):
  N = int(sys.stdin.readline())
  for i in range(N):
   inp = sys.stdin.readline(); inp = inp.split(" ")
   u,v = int(inp[0]),int(inp[1])
   f[u] = v
   visited[u] = False
   c[u] = -1
  m = -1
  for i in range(N):
  	if c[i] == -1:
  	 dfs(i)
  	if c[i] > m:
  	 m=c[i]
  	 mu = i
  print("Case "+str(ci)+": "+str(mu))
  ci+=1
  T-=1

main() 