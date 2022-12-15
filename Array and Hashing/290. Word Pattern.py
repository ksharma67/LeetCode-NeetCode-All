class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        map = {}
        map_rev = {}
        if not pattern and not str:
            return True
        if (not pattern and str) or (pattern and not str):
            return False
        str_l = str.split()
        if len(pattern) != len(str_l):
            return False
        for c,word in zip(pattern, str_l):
            if c not in map:
                if word in map_rev:  # no mapping of diff chars to the same word
                    return False
                map[c] = word
                map_rev[word] = c
            elif map[c] != word:  # preserving the order
                return False
        return True
