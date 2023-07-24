class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        n = len(target)
        maxMask = 1 << n
        # dp[i] := min # of stickers to spell out i, where i is the bit mask of
        # target.
        dp = [float('inf')] * maxMask
        dp[0] = 0
        
        # Preprocess the stickers to create a mapping of character frequencies
        stickerCounts = []
        for sticker in stickers:
            stickerCounts.append(collections.Counter(sticker))
        
        for mask in range(maxMask):
            if dp[mask] == float('inf'):
                continue
            # Try to expand from `mask` by using each sticker.
            for i, stickerCount in enumerate(stickerCounts):
                # Skip over stickers that do not contain any characters we need
                if not any(c in stickerCount for c in target):
                    continue
                superMask = mask
                for c, freq in stickerCount.items():
                    for j, t in enumerate(target):
                        # Try to apply it on a missing char.
                        if c == t and not (superMask >> j & 1):
                            superMask |= 1 << j
                            freq -= 1
                            if freq == 0:
                                break
                dp[superMask] = min(dp[superMask], dp[mask] + 1)
        
        return -1 if dp[-1] == float('inf') else dp[-1]
