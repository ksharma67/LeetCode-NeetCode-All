class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        values = set(nums)
        missing = []
        for i in range(1,len(nums)+1):
            if i not in values: missing.append(i)
        return missing
