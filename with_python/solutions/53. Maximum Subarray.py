from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_so_far = answer = nums[0]
        
        for curr in nums[1::]:
            max_so_far = max(curr + max_so_far, curr)
            answer = max(max_so_far, answer)
            
        return answer

""""
Same idea - alot simplier.
No need for so many cases etc...


sample 68 ms submission

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if not nums:
            return None
        
        max_so_far = answer = nums[0]
        
        for i in range(1, len(nums)):
            curr = nums[i]
            max_so_far = max(curr + max_so_far, curr)
            answer = max(max_so_far, answer)
            
        return answer



It turns out it is better to just do inplace replacments, on the array.

It turns out that if you cut on the lines of code in the for loop, this is the thing that does the best changes!
"""

numsnums = [
    [-2,1,-3,4,-1,2,1,-5,4],
    [1],
    [5,4,-1,7,8],
    [1,1,1,1],
    [-1,-1,-1,-1],
    [-1,1,-1,1,-1,1],
    [-1],
    [-2,-1],
    [-1,-2]
]
for nums in numsnums:
    res = Solution().maxSubArray(nums) 
    print(nums)
    print(res)          