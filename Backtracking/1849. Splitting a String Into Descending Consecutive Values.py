import math

class Solution:
    def splitString(self, s: str) -> bool:
        def rec(idx, parts, prev_val):
            if idx == L:
                return parts >= 2
            
            for i in range(idx, L):
                num = int(s[idx : i + 1])
                if prev_val == math.inf or num == prev_val - 1:
                    if rec(i + 1, parts + 1, num):
                        return True
            return False
        
        L = len(s)
        return rec(0, 0, math.inf)
