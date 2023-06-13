class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        maxim = nums[0]
        prefix_sum = nums[0]

        for idx in range(1, len(nums)):
            curr = nums[idx]
            prefix_sum += curr
            if curr > maxim:
                maxim = max(maxim, math.ceil(prefix_sum / (idx + 1)))


        return maxim
