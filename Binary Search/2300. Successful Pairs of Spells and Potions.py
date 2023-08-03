class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def binary_search(temp,m,target):
            l = 0
            r = m-1
            while l < r:
                mid = l + (r-l)//2
                if temp[mid] >= target:
                    r = mid
                else:
                    l = mid+1 
            if temp[l] >= target:
                return l
            else:
                return m
        n = len(spells)
        m = len(potions)
        ans = [0]*n
        potions = sorted(potions)
        for i in range(n):
            if spells[i] >= success :
                ans[i] = m
            else:
                if success%spells[i] == 0:
                    target = success//spells[i]
                else:
                    target = success//spells[i] + 1
                ans[i] = m - binary_search(potions,m,target)
        return ans
