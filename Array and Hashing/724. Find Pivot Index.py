class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        # Calculate total sum
        total_sum = sum(nums)
        
        # Initialize left edge sum
        left_sum = 0
        
        for i in range(len(nums)):
            # Calculate right side of index by subtracting current index and left side from total_sum
            right_sum = total_sum - nums[i] - left_sum
            # Check for equality 
            if left_sum == right_sum:
			   # Return pivot index if left_sum equals right_sum
                return i
            # Update left of index
            left_sum += nums[i]
		# Return -1 if no pivot index is found	
        return -1
