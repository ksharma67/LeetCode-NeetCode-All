class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # variable to keep track of the number of modifications
        count = 0
        # iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # check if the current element is less than the previous element
            if nums[i] < nums[i-1]:
                # if it is, increment the count
                count += 1
                # if we have already made a modification, return False
                if count > 1:
                    return False
                # if the current element is less than or equal to the element before the previous element
                # we modify the current element to be equal to the previous element
                if i < 2 or nums[i] >= nums[i-2]:
                    nums[i-1] = nums[i]
                # otherwise, we modify the previous element to be equal to the current element
                else:
                    nums[i] = nums[i-1]
        # if we reach the end of the loop without returning False, return True
        return True
