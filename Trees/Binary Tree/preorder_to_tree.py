class Binary_Tree_Node:
	def __init__(self,data):
		self.data = data
		self.right = None
		self.left = None

def PreOrder(root,result):
	if root is None:
		return
	result.append( root.data )
	PreOrder(root.left, result)
	PreOrder(root.right, result)
	return result

def preorder_to_tree(preorder):
	"""
	constraints: each tree have two type of nodes only "L" is 
	leaf and "I" is internal node. each I have eactly two child
	"""
	if len(preorder) == 0:
		return None
	
	root = Binary_Tree_Node( preorder[0] )
	if preorder[0] == 'L':
		preorder.pop(0)
		return root
	preorder.pop(0)
	l = preorder_to_tree(preorder)
	r = preorder_to_tree(preorder)

	root.left = l
	root.right = r
	return root
	 

if __name__ == "__main__":
	preorder = ['I','I','L','I','L','L','I','L','L']
	root = preorder_to_tree(preorder)
	print( PreOrder(root,[]) )
