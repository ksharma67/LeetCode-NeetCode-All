class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        # sort the given list
        nums.sort()
        
        # place all the value in the result list keep one element distance between them
        # use two pointer algorithm 
        # so either keep two small values on left and right of the larger value 
        # or keep larger value on left and right of the smaller value
        ans = list()
        
        i = 0
        j = len(nums) - 1
        
        while len(ans) != len(nums):
            
            # append the left value to answer list and increment left pointer
            ans.append(nums[i])
            i += 1
            
            # check if value at left pointer is less than the right pointer 
            # if yes append the value of right to answer and decrement right pointer
            if nums[i] < nums[j]:
                ans.append(nums[j])
                j -= 1
                
        # once all the element are placed return the answer
        return ans
