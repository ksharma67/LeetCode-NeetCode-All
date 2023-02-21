class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        nlen = len(needle)
        hlen = len(haystack)
        
        if nlen == hlen and nlen == 0:
            return 0
        
        for i in range(hlen-nlen+1):
            if haystack[i:i+nlen] == needle:
                return i
        
        return -1
