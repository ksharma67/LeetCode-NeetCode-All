class Solution:
    def totalFruit(self, fr: list[int]) -> int:
        
        l = i = 0                            # [1] left and intermediate indices
        m = 0                                # [2] max interval length
        bs = [-1,-1]                         # [3] fruit counts in the basket
        
        for r in range(len(fr)):             # [4] move right end
            if fr[r] != bs[1]:               # [5] when encountered a different fruit
                if fr[r] != bs[0]: l = i     #     - update left end for the new earliest type
                i = r                        #     - update index of the first entrance of this type
                bs[0], bs[1] = bs[1], fr[r]  #     - update earliest/latest pair in the basket
            m = max(m, r - l + 1)            # [6] compute length of current interval

        return m
