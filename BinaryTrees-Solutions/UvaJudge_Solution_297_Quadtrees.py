import sys
from sys import stdin

class QuadTree:
	def __init__ (self,num,s1=None,s2=None,s3=None,s4 = None):
		self.num = num
		self.s1 = s1
		self.s2 = s2
		self.s3 = s3
		self.s4 = s4
	def __str__(self):
		str_s1 = str(self.s1) if self.s1 != None else ''
		str_s2 = str(self.s2) if self.s2 != None else ''
		str_s3 = str(self.s3) if self.s3 != None else ''
		str_s4 = str(self.s4) if self.s4 != None else ''
		s = '{} ({}) ({}) ({}) ({})'.format(self.num,str_s1,str_s2,str_s3,str_s4)
		return s

def build_tree():
	if len(preorder) >= 1:
		if preorder[0] == 'p':
			val = preorder.pop(0)
			return QuadTree(val,build_tree(),build_tree(),build_tree(),build_tree())
		if preorder[0] == 'f' or preorder[0] == 'e':
			val = preorder.pop(0)
			return QuadTree(val)
	return None
def build_rel_tree(t1,t2):
	if t1 != None and t2 != None and (t1.num == 'f' or t2.num == 'f'):
		return QuadTree('f')
	elif t1 != None and t2 != None and t1.num == 'p' and t2.num == 'p':
		return QuadTree('p',build_rel_tree(t1.s1,t2.s1),build_rel_tree(t1.s2,t2.s2),build_rel_tree(t1.s3,t2.s3),build_rel_tree(t1.s4,t2.s4))
	elif t1 != None and t2 != None and t1.num == 'p' and t2.num == 'e':
		return QuadTree('p', t1.s1,t1.s2,t1.s3,t1.s4)
	elif t1 != None and t2 != None and t1.num == 'e' and t2.num == 'p':
		return QuadTree('p', t2.s1,t2.s2,t2.s3,t2.s4)
	elif t1 != None and t2 != None and t1.num == 'e' and t2.num == 'e':
		return QuadTree('e')

def sum_tree(t,lvl):
	if t != None:
		if t.num == 'f':
			return 1024//(4**lvl)
		elif t.num == 'e':
			return 0
		elif t.num == 'p':
			return sum_tree(t.s1,lvl+1)+sum_tree(t.s2,lvl+1)+sum_tree(t.s3,lvl+1)+sum_tree(t.s4,lvl+1)
	return 0

def main():
	global preorder
	cases, c = int(stdin.readline()),0
	while c < cases:
		preorder = list(stdin.readline())
		tree1 = build_tree()
		preorder = list(stdin.readline())
		tree2 = build_tree()
		rel_tree = build_rel_tree(tree1,tree2)
		ans = sum_tree(rel_tree,0)
		print("There are {} black pixels.".format(ans))
		c+=1
main()