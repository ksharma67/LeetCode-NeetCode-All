class Solution:
    def findPeakElement(self, nums):
        # If the array contains only one element, it is the peak.
        if len(nums) == 1:
            return 0
        
        # Check if the first element is greater than the second,
        # if so, the first element is a peak.
        if nums[0] > nums[1]:
            return 0
        
        # Check if the last element is greater than the second-to-last,
        # if so, the last element is a peak.
        if nums[len(nums) - 1] > nums[len(nums) - 2]:
            return len(nums) - 1
        
        # Now, use binary search to find the peak element.
        # Set two pointers i and j to the second and second-to-last elements,
        # respectively, because we already checked the first and last elements.
        i = 1
        j = len(nums) - 2
        
        while i <= j:
            # Calculate the middle index.
            mid = i + (j - i) // 2
            
            # If the middle element is greater than its neighbors, it's a peak.
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
            elif nums[mid - 1] < nums[mid]:
                # If the element to the left of mid is less than mid,
                # it means we are in a decreasing portion of the array,
                # so the peak must be on the right side of mid.
                i = mid + 1
            else:
                # Otherwise, we are in an increasing portion of the array,
                # so the peak must be on the left side of mid.
                j = mid - 1
        
        # If no peak is found, return None.
        return None
