import sys
from sys import stdin 
from collections import deque

def solve(initial, target, visited, instructions):
	queue = deque()
	if visited[initial] or visited[target]:
		return -1
	queue.append(initial)
	is_posible = False
	act = 0
	while queue and is_posible == False:
		act = queue.popleft()
		if visited[act] == False:
			visited[act] = True
			if act != target:
				act1 = 0
				#up arrow pressed
				if act//1000 != 9:
				 act1=act+1000
				else:
				 act1=act-9000
				if act1 == target:
				  return instructions[act]+1
				if visited[act1] == False:
				 queue.append(act1)
				instructions[act1] = instructions[act]+1
				if act%10 != 9:
				 act1 = act+1
				else:
				 act1 = act-9
				if act1 == target:
				  return instructions[act]+1
				if visited[act1] == False:
				 queue.append(act1)
				instructions[act1] = instructions[act]+1				  
				if (act%100)//10 != 9:
				 act1 = act + 10
				else:
				 act1 = act - 90
				if act1 == target:
				  return instructions[act]+1
				if visited[act1] == False:
				 queue.append(act1)
				instructions[act1] = instructions[act]+1
				if (act%1000)//100 != 9:
				 act1 = act + 100
				else:
				 act1 = act - 900
				if act1 == target:
				  return instructions[act]+1
				if visited[act1] == False:
				 queue.append(act1)
				instructions[act1] = instructions[act]+1
				#down arrow pressed
				if act//1000 != 0:
				 act1=act-1000
				else:
				 act1=act+9000
				if act1 == target:
				  return instructions[act]+1
				if visited[act1] == False:
				 queue.append(act1)
				instructions[act1] = instructions[act]+1
				if act%10 != 0:
				 act1 = act-1
				else:
				 act1 = act+9
				if act1 == target:
				  return instructions[act]+1
				if visited[act1] == False:
				 queue.append(act1)
				instructions[act1] = instructions[act]+1
				if (act%100)//10 != 0:
				 act1 = act - 10
				else:
				 act1 = act + 90
				if act1 == target:
				  return instructions[act]+1
				if visited[act1] == False:
				 queue.append(act1)
				instructions[act1] = instructions[act]+1
				if (act%1000)//100 != 0:
				 act1 = act - 100
				else:
				 act1 = act + 900
				if act1 == target:
				  return instructions[act]+1
				if visited[act1] == False:
				 queue.append(act1)
				instructions[act1] = instructions[act]+1	
			else:
			    is_posible = True

	if is_posible:
		return instructions[target]
	else:
		return -1


def main():
 global visited,instructions
 tc = int(sys.stdin.readline())
 blank = sys.stdin.readline()
 while tc > 0:
  visited = [False]*10000
  instructions = [0]*10000
  comb = sys.stdin.readline(); comb = int(comb.replace(" ","").rstrip())
  target = sys.stdin.readline(); target = int(target.replace(" ","").rstrip())
  f = int(sys.stdin.readline())
  for i in range(f):
     aux_forbidden = sys.stdin.readline(); aux_forbidden = int(aux_forbidden.replace(" ","").rstrip())
     visited[aux_forbidden] = True
  print(solve(comb,target,visited,instructions))
  tc-=1
  if(tc >0):
   blank = stdin.readline()

main()