class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ''
        for args in zip(*strs):
            if all(arg == args[0] for arg in args):
                pre += args[0]
            else:
                break
        return pre
