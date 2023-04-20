class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = []
        nums1 = set(nums)
        def sol(path):
            if len(path) == len(nums[0]):
                ans.append(path)
                return
            for i in ["0","1"]:
                sol(path + i)

        sol('')
        for i in ans:
            if i in nums1 or i[::-1] in nums1:
                continue
            else:
                return i
