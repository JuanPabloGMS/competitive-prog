import sys
from sys import stdin
sys.setrecursionlimit(10**6)

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

def build_tree(pre,ino):
	if len(pre) > 1:
		ind = ino.index(pre[0])
		return BinTree(pre[0],build_tree(pre[1:ind+1],ino[:ind+1]),build_tree(pre[ind+1:],ino[ind+1:]))
	elif len(pre) == 1:
		return BinTree(pre[0])

def post(t):
	if t.l != None:
		postorder.append(post(t.l))
	if t.r != None:
		postorder.append(post(t.r))
	return t.num

def main():
	global inorder,postorder
	data = stdin.readline()
	while data:
		postorder,preorder,inorder = [],[],[]
		data = data.split()
		preorder = data[0]
		inorder = data[1]
		tree = build_tree(preorder,inorder)
		post(tree)
		postorder.append(preorder[0])
		ans = ""
		for i in range(len(postorder)):
			ans+=postorder[i]
		print(ans)
		data = stdin.readline()
main()