class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(gen):
            ans = cur = float('-inf')
            for x in gen:
                cur = x + max(cur, 0)
                ans = max(ans, cur)
            return ans
        
        S = sum(nums)
        if len(nums) == 1:
            return S
        
        ans1 = kadane(iter(nums))
        ans2 = S + kadane(-nums[i] for i in range(1, len(nums)))
        ans3 = S + kadane(-nums[i] for i in range(len(nums) - 1))
        return max(ans1, ans2, ans3)
