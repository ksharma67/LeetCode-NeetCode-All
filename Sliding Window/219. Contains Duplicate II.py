class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # create a hash map to store the indices of each element
        num_indices = {}
        
        # iterate over the array
        for i, num in enumerate(nums):
            # if the element is already in the hash map and its index difference is <= k, return True
            if num in num_indices and i - num_indices[num] <= k:
                return True
            
            # add the element to the hash map with its index
            num_indices[num] = i
        
        # if we don't find any repeated elements with the required index difference, return False
        return False
