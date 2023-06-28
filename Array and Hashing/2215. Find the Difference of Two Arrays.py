class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        # define set to store elements
        s1 = set(nums1)
        s2 = set(nums2)

        # define output
        out = [[],[]]

        # adding the elements to output if not contains in the set
        for i in s1:
            if i not in s2:  
                out[0].append(i)
        for i in s2:
            if i not in s1:
                out[1].append(i)
        
        return out
