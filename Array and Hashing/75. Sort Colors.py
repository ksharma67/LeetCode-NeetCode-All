class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a=nums.count(0)
        b=nums.count(1)
        for i in range(len(nums)):
            if a!=0:
                nums[i]=0
                a-=1
            elif b!=0:
                nums[i]=1
                b-=1
            else:
                nums[i]=2
