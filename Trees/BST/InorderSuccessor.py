class BST_Tree_Node:
	""" BST Node """
	def __init__(self,data):
		self.data = data
		self.right = None
		self.left = None

def InorderSuccessor(root):
	""" 
	here we are not considering inorder successor 
	in case in which are parent of a node is its inorder succeccor 
	"""
	if root.right:
		root = root.right
	else:
		return None
	
	while root and root.left:
		root = root.left
	return root.data

if __name__ == "__main__":
	"""      root
		_____ 10______
		|			 |
	____5___	 ____18___
	|		|	 |		 |
  __3		7	 16		 20
  |
  2
	"""
	root = BST_Tree_Node(10)
	root.left = BST_Tree_Node(5)
	root.right = BST_Tree_Node(18)
	a = root.left
	b = root.right
	a.left = BST_Tree_Node(3)
	a.right = BST_Tree_Node(7)
	b.left = BST_Tree_Node(16)
	b.right = BST_Tree_Node(20)
	a.left.left = BST_Tree_Node(2)

	print( InorderSuccessor(root) )
	print( InorderSuccessor(root.left) )
	print( InorderSuccessor(root.right) )
	print( InorderSuccessor(root.right.left) )