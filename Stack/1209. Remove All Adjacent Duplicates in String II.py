class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in s:
            if len(stack) == 0:
                stack.append([i, 1])
            else:
                if i == stack[-1][0]:
                    stack[-1][1] += 1
                    if stack[-1][1] == k:
                        stack.pop()
                else:
                    stack.append([i,1])
        res = ''
        for i in stack:
            res += i[0] * i[1]
        return res
