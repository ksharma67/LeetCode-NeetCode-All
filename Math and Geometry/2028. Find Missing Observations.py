class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        #finding the equal distribution of remaining sum
        temp = mean*(n+len(rolls)) - sum(rolls)
        each = temp//n
        rem = temp%n
        
        #return empty if out of dice range
        if (not (1<=(each + 1)<=6) and rem>0) or not (1<=each<=6):
            return []
        
        res = [each]*n
        i = 0
        #adding the remainder to each possible
        while rem > 0 and i<n:
            res[i] += 1
            rem -= 1
            i += 1
            
        return res
