class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
	    @lru_cache(None)
	    def dp(target: int) -> int:
		    if target == 0:
			    return 1
		    if target < 0:
			    return 0
		    return sum(dp(target - num) for num in nums)

	    return dp(target)
