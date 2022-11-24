class Node:
	
	def __init__(self, key):
		
		self.key = key
		self.child = []

def newNode(key):
	temp = Node(key)
	return temp	

def LevelOrderTraversal(root):

	if (root == None):
		return


	q = []
	q.append(root) 
	while (len(q) != 0):
	
		n = len(q)
		
		while (n > 0):
	
			
			p = q[0]
			q.pop(0)
			print(p.key, end=' ')
			
			for i in range(len(p.child)):
			
				q.append(p.child[i])
			n -= 1
		print() 
	
