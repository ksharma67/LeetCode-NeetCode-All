class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        start,end=0,len(nums)-1
        co=end
        out=[0]*(end+1)
        while(start<=end):
            if abs(nums[start])>abs(nums[end]):
                out[co]=nums[start]**2
                start+=1
            else:
                out[co]=nums[end]**2
                end-=1
            co-=1
        return out
