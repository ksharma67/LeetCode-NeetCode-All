class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prev=float("inf")
        l=0
        total=0
        res=0
        for i in range(len(nums)):
            total+=nums[i]
            while total>=target:
                res=i-l+1
                res=min(res,prev)
                prev=res
                total-=nums[l]
                l+=1
        if prev==float("inf"):
            return 0
        else:
            return res
