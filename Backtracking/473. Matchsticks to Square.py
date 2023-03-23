class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        
        sides = [0]*4
        if sum(matchsticks)%4!=0:
            return False
        s = sum(matchsticks)//4
        
        matchsticks.sort(reverse=True)
        
        def helper(i):
            if i == len(matchsticks):
                return True
            
            for j in range(4):
                
                if sides[j]+matchsticks[i]<=s:
                    sides[j]+=matchsticks[i]
                    if helper(i+1):
                        return True
                    sides[j]-=matchsticks[i]
            return False
        
        return helper(0)
