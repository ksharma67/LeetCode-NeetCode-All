class Solution:
    def partitionString(self, s: str) -> int:
        checkUniqueAlphabet = set()
        i = 0
        minCount = 0
        while i < len(s):
            minCount += 1
            while i < len(s) and s[i] not in checkUniqueAlphabet:
                checkUniqueAlphabet.add(s[i])
                i += 1
            checkUniqueAlphabet.clear()
        return minCount
