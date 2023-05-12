class Solution:
	res = 0 
	def maxLength(self,arr):
		self.backtrack(arr,0,"")
		return self.res

	def backtrack(self,arr,ind,local):
		if len(local)!=len(set(local)):
			return
			
		self.res = max(self.res,len(local))
		for i in range(ind,len(arr)):
			self.backtrack(arr,i+1,local+arr[i])
