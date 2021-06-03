from typing import List

"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = []
        Left_bound = intervals.pop(0)
        while len(intervals) > 0:
            cur = intervals.pop(0)
            if Left_bound[1] >= cur[0]:
                Left_bound[1] = max(Left_bound[1],cur[1])
            else: # Left_bound[1] < cur[0]
                output.append(Left_bound)
                Left_bound = cur
        output.append(Left_bound)
        return output

inputs_outputs = [
    #([[1,3],[2,6],[8,10],[15,18]],[[1,6],[8,10],[15,18]]),
    #([[1,4],[4,5]], [[1,5]]),
    #([[8,10],[2,6],[1,3],[15,18]],[[1,6],[8,10],[15,18]]),
    #([[4,5],[1,4]], [[1,5]]),
    #([[1,4]],[[1,4]]),
    ([[1,3],[2,6],[8,10],[0,19],[15,18]],[[0,19]])
]
for instance in inputs_outputs:
    intervals = instance[0]
    output = Solution().merge(intervals)
    expected_output = instance[1]
    print(output == expected_output)
    print(output)