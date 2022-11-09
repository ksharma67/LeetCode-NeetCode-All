class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        def recurseFunction(s, i, j) -> None:
            if i==j or i > j:
                return
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            recurseFunction(s, i + 1, j - 1)
        recurseFunction(s, i, j)
