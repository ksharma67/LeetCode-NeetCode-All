class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s == '':
            return 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                break
        else:
            return 0
        for j in range(i, -1, -1):
            if s[j] == ' ':
                break
        else:
            j = j - 1
        return i - j
