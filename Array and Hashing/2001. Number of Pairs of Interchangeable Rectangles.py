class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        rectangles = [w/h for w, h in rectangles]
        count = Counter(rectangles)
        res = 0
        for c in count.values():
            curSum = 0 
            for i in range(1, c):
                curSum += i
            res += curSum
        return res
