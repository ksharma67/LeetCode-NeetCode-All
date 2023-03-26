class Solution:
    result = {1:1,2:1,3:2,4:4,5:6,6:9,7:12,8:18,9:27,10:36}
    def integerBreak(self, n: int) -> int:
        try:
            return self.result[n]
        except:
            x = float("-inf")
            for i in range(1,n):
                j = n-1
                while j>0:
                    if i+j==n:
                        k = self.integerBreak(i)*self.integerBreak(j)
                        x = max(x,k)
                    j-=1
            self.result[n] = x
            return self.result[n]
