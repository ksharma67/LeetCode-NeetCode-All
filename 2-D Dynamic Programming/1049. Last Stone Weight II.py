class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        n = len(stones)
        memo = {}

        def go(pos, res):

            if pos == n:
                return res if res >= 0 else float('inf')

            cur = (pos, res)
            if cur in memo:
                return memo[cur]

            memo[cur] = min(
                float('inf'),
                go(pos+1, res-stones[pos]), # negative
                go(pos+1, res+stones[pos]) # positive
            )

            return memo[cur]


        return go(0, 0) 
        
