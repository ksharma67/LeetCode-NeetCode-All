class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        if s == s[::-1]:
            return True 
        i = 0
        j = n-1
        while(i<=j):
            if s[i] != s[j]: 
                if s[i+1: j+1][::-1] == s[i+1: j+1] or s[i: j] == s[i: j][::-1]:  
                    return True
                else:
                    return False
            else:
                i += 1 
                j -= 1 
