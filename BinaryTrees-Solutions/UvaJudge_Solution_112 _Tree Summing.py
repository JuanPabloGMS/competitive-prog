#Author: Juan Pablo Giraldo Mosquera
#Problem: 112 Tree Summing
#Link: https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=48

import sys
from sys import stdin
sys.setrecursionlimit(10**6)

INPUT,I = stdin.buffer.read(),0
SPACE,CR,LPAR,RPAR,ZERO,NINE,NEG = ord(' '),ord('\n'),ord('('),ord(')'),ord('0'),ord('9'),ord('-')

class BinTree:
	def __init__(self,num,left=None,right=None):
		self.num = num
		self.l = left
		self.r = right
		return
	def __str__(self):
		str_l = str(self.l) if self.l != None else ''
		str_r = str(self.r) if self.r != None else ''
		s='{} ({}) ({})'.format(self.num,str_l,str_r) 
		return s

def has_next(): return I<len(INPUT)
def is_digit(): return ZERO <= INPUT[I] <= NINE
def is_par(): return INPUT[I] == LPAR or INPUT[I] == RPAR
def is_neg(): return INPUT[I] == NEG
def read_blanks():
	global INPUT,I
	while has_next() and not is_digit() and not is_par() and not is_neg():
		I+=1
def read_par():
	global INPUT,I
	ans,I = chr(INPUT[I]),I+1
	return ans
def read_num():
	global INPUT,I
	ans = 0
	while has_next() and is_digit():
		ans,I = int(chr(INPUT[I]))+ans*10,I+1
	return ans
def read_neg_num():
	global INPUT,I
	ans = 0
	I+=1
	while has_next() and is_digit():
		ans,I = int(chr(INPUT[I]))+ans*10,I+1
	return ans*-1

def next_token():
	global INPUT,I
	ans = None
	read_blanks()
	if I!=len(INPUT):	
		if is_digit(): ans = read_num()
		elif is_neg(): ans = read_neg_num()
		else: ans = read_par()
	return ans

def parse_tree():
	tkn = next_token()
	if tkn == ')':
		return parse_tree()
	elif tkn == '(':
		sig = next_token()
		if type(sig) == int:
			return BinTree(sig,parse_tree(),parse_tree())
		else:
			return
	return 

def DFS (tgt,acum,tree):
	if acum == tgt and tree.l == None and tree.r == None:
		return True
	elif acum != tgt and tree.l == None and tree.r == None:
		return False
	elif tree.l != None and tree.r != None:
		return DFS(tgt,acum+tree.l.num,tree.l) or DFS(tgt,acum+tree.r.num,tree.r)
	elif tree.l != None:
		return DFS(tgt,acum+tree.l.num,tree.l)
	elif tree.r != None:
		return DFS(tgt,acum+tree.r.num,tree.r)
	return

def solve(n,tree):
	if tree != None:
		return DFS(n,tree.num,tree)
	else:
		return False
def main():
	global INPUT, I
	tkn = next_token()
	while tkn != None:
		while tkn == ')':
			tkn = next_token()
		if tkn == None:
			break
		tree = parse_tree()
		print('yes' if solve(tkn,tree) else 'no')
		tkn = next_token()
main()
