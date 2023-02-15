class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # first assume everyone flies to a
        a_sum = sum(a_cost for a_cost, _ in costs)
        # select the n largest diff, and sum them
        max_diff_sum = sum(heapq.nlargest(len(costs) // 2, (a_cost - b_cost for a_cost, b_cost in costs)))
        # minimum cost = a_sum - max_diff_sum
        return a_sum - max_diff_sum
