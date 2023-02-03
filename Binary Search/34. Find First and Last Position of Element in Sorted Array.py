class Solution:

    def lower_bound(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) //2  # safe in case of overflow
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid-1
        
        return l if (0 <= l < len(nums)) and (nums[l] == target) else -1
    
    def upper_bound(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + r - l //2  # safe in case of overflow
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid-1
        
        return r if (0 <= r < len(nums)) and nums[r] == target else -1
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.lower_bound(nums, target), self.upper_bound(nums, target)]
