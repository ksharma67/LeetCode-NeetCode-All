class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        gaps = {0 : 0} 
        for i in wall:
            temp = 0
            for j in i[:-1]:
                temp += j
                if(temp in gaps):
                    gaps[temp] += 1
                else:
                    gaps[temp] = 1
        return len(wall) - max(gaps.values())
