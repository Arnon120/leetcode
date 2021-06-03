from typing import List
"""
A better solution does not use the max function.
In order to do that, it start from the end, and checks if there is a way to get up to this point, going backwards.
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n-1):
            if nums[i] <= 0:
                return False
            nums[i+1] = max(nums[i]-1,nums[i+1])
        return True

numsnums = [
    [2,3,1,1,4],
    [3,2,1,0,4],
    [1,1,1,1,1,1],
    [2,0,0],
    [0,1],
    [0],
    [1]
]
for nums in numsnums:
    print( nums )
    print( Solution().canJump(nums) )