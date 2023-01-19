class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0 for _ in range(len(prices))]
        minPast = prices[0]
        for i in range(1,len(prices)):
            if minPast>prices[i]:
                minPast=prices[i]
            dp[i]=max(dp[i-1],dp[i-1]+prices[i]-prices[i-1],prices[i]-minPast)
        return dp[-1]
