from typing import List
"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.
"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        if n == 0:
            return [newInterval]
        left = 0
        right = n-1
        a = newInterval[0]
        b = newInterval[1]
        b_right = intervals[right][1]
        if a > b_right:
            intervals.insert(right+1, newInterval)
            return intervals
        while left < right:
            mid = (left+right) //2
            b_mid = intervals[mid][1]
            if b_mid < a:
                left = mid+1
            else: # a <= b_mid
                right = mid
        left_crit = right
        if b < intervals[left_crit][0]:
            intervals.insert(left_crit,newInterval)
            return intervals
        left = left_crit
        right = n-1
        while left < right:
            mid = (left + right+1) //2
            a_mid = intervals[mid][0]
            if b < a_mid:
                right = mid -1
            else:
                left = mid
        right_crit = left
        return intervals[0:left_crit] + [[min(intervals[left_crit][0],a),max(intervals[right_crit][1],b)]] + intervals[right_crit+1:n]


inputs_outputs = [
    ([[1,6],[8,10],[15,18]],[5,7],[[1,7],[8,10],[15,18]]),
    ([[1,6],[8,10],[15,18]],[5,9],[[1,10],[15,18]]),
    ([[1,6],[8,10],[15,18]],[5,17],[[1,18]]),
    ([[1,6],[8,10],[15,18]],[5,19],[[1,19]]),
    ([[1,6],[8,10],[15,18]],[11,12],[[1,6],[8,10],[11,12],[15,18]]),
    ([[1,3],[6,9]],[2,5],[[1,5],[6,9]]),
    ([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8],[[1,2],[3,10],[12,16]]),
    ([],[5,7],[[5,7]]),
    ([[1,5]],[2,3],[[1,5]]),
    ([[1,5]],[2,7],[[1,7]]),
    ([[3,4]],[1,2],[[1,2],[3,4]]),
    ([[3,4]],[5,6],[[3,4],[5,6]])
]
for instance in inputs_outputs:
    intervals = instance[0]
    newInterval = instance[1]
    output = Solution().insert(intervals,newInterval)
    expected_output = instance[2]
    if output == expected_output:
        print (True)
    else:
        print ("intervals = "+str(intervals) + " newInterval = "+str(newInterval)+ " output = "+str(output) + 'expected_output = '+ str(expected_output))

"""
Best
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        new_intervals = []
        for i in range(len(intervals)):
            if intervals[i][0] < newInterval[0]:
                new_intervals.append(intervals[i])
            else:
                break
            
        new_intervals.append(newInterval)
        for j in range(i, len(intervals)):
            new_intervals.append(intervals[j])
        
        # merge
        res = []
        for interval in new_intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        
        return res
"""