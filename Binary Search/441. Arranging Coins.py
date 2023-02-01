class Solution:
    def arrangeCoins(self, n: int) -> int:
        start = 0
        end = n
        while start <= end:
            mid = start+(end-start)//2
            k = mid*(mid+1)//2
            if k == n:
                return mid
            elif k < n:
                start = mid+1
            else:
                end = mid-1
        return end
