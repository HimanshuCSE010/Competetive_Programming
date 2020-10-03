class Solution:
	def combinationSum(self, candidates, target):
		mi = min(candidates)
		n = len(candidates)
		candidates.sort()

		self.result = []
		path = []
		self.backtracking(candidates,0,n,mi,target,path)
		return list(map(list,self.result))

	def backtracking(self,candidates,start,end,mi,target,path):
		if target == 0:
			self.result.append( path.copy() )
			return

		if target < mi:
			return

		for i in range(start,end):
			ele = candidates[i]
			if ele > target:
				return
			self.backtracking(candidates,i,end,mi,target-ele,path+[ele])

if __name__ == "__main__":
	s = Solution()

	lst = [2,3,5]
	target = 8
	print( s.combinationSum(lst,target) )

	lst = [2,3,6,7]
	target = 7
	print( s.combinationSum(lst,target) )

	lst = [2]
	target = 1
	print( s.combinationSum(lst,target) )

	lst = [1]
	target = 1
	print( s.combinationSum(lst,target) )

	lst = [1]
	target = 2
	print( s.combinationSum(lst,target) )