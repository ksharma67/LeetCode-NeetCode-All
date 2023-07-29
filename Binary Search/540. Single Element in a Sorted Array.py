class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start, end = 0, len(nums) // 2
        ans = -1
        while start <= end:
            mid = (start + end) // 2
            idx = mid * 2
            if idx + 1 >= len(nums) or nums[idx] != nums[idx + 1]:
                end = mid - 1
                ans = nums[idx]
            else:
                start = mid + 1
        return ans
