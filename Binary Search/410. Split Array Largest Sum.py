class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # Define the binary search range
        left = max(nums)
        right = sum(nums)
        
        # Define a helper function to check if it's possible to split the array into k subarrays
        def is_possible(mid):
            count = 1
            curr_sum = 0
            for num in nums:
                curr_sum += num
                if curr_sum > mid:
                    count += 1
                    curr_sum = num
                    if count > k:
                        return False
            return True
        
        # Binary search
        while left < right:
            mid = (left + right) // 2
            if is_possible(mid):
                right = mid
            else:
                left = mid + 1
        
        # Return the answer
        return left
