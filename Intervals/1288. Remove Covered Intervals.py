class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        d=dict()   
        high=-1
        ans=0
        totalIntervals = len(intervals)
		
        for i in range(len(intervals)):
            if intervals[i][0] in d.keys():
                if d[intervals[i][0]]< intervals[i][1]:
                    d[intervals[i][0]] = intervals[i][1]
            else:
                d[intervals[i][0]]  = intervals[i][1]
        for i in sorted(d):
            if d[i] > high:
                high = d[i]
                ans+=1
        return ans
            
        
        
        
