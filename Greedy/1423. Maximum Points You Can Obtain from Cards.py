class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        new_k = len(cardPoints) - k
        total_sum, k_sum = 0, 0
        # we can do total_sum = sum(cardPoints) 
		# k_sum = sum(cardPoints[:new_k])
        for i in range(len(cardPoints)):
            total_sum += cardPoints[i]
            if i < new_k:
                k_sum += cardPoints[i]
        
        res = total_sum - k_sum
        for i in range(1, k+1):
            k_sum -= cardPoints[i-1]
            k_sum += cardPoints[i+new_k-1]
            res = max(res, total_sum - k_sum)
        return res
