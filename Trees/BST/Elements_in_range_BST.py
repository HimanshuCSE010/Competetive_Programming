class Solution:
	''' 
	T = O(n) 
	S = (1) 
	'''
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def rec(root,low,high):
            if not root:
                return 0
            
            # if current value is less than low then check only 
            # for right child as left any how is low than current
            if root.val < low:
                return rec(root.right, low, high)
            
            # if current value is more than high then check only 
            # for left child as right any how is high than current
            if root.val > high:
                return rec(root.left, low, high)
            
            # if execution reached here means current value is in
            # range low to high
            l = rec(root.left, low, high)       # do same for left sub tree
            r = rec(root.right, low, high)      # do same for right sub tree
            
            return root.val + l + r             # return total sum
        
        return rec(root, low, high)

class BST_Tree_Node:
	""" BST Node """
	def __init__(self,data):
		self.data = data
		self.right = None
		self.left = None

def range_BST(root,k1,k2,result=[]):
	if root is None:
		return

	# no need to go left if root itself is equal or less than k1
	if root.data > k1:
		range_BST(root.left,k1,k2,result)
	# add to result if satisfies
	if k1 <= root.data <= k2:
		result.append(root.data)
	# no need to go right if root itself is equal or more than k2
	if root.data < k2:
		range_BST(root.right,k1,k2,result)

	return result


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

	print( range_BST(root,1,15) )
