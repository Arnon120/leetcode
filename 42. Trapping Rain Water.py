from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        if right <= 0:
            return 0
        left_bound = height[left]
        right_bound = height[right]
        sum = 0
        while left < right:
            if left_bound < right_bound:
                left += 1
                current_height = height[left]
                if current_height < left_bound:
                    sum += left_bound - current_height
                else:
                    left_bound = current_height
            #### something symmetric...
            else: # left_bound >= right_bound
                right -= 1
                current_height = height[right]
                if current_height < right_bound:
                    sum += right_bound - current_height
                else:
                    right_bound = current_height
        return sum

"""



This version has way less if statments.
and no need to check for the len = 0 case.
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lmax, rmax = 0, 0
        vol = 0

        while l < r:
            lmax = max(lmax, height[l])
            rmax = max(rmax, height[r])

            if lmax < rmax:
                vol += lmax - height[l]
                l += 1
            else:
                vol += rmax - height[r]
                r -= 1

        return vol



Here is the best time solution:


class Solution:
    def trap(self, height: List[int]) -> int:        
        left,left_max = 0,0
        right,right_max = len(height)-1,0
        ans = 0
        
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1
                
        return ans
"""


inputs = [
    #[0,1,0,2,1,0,1,3,2,1,2,1],
    #[4,2,0,3,2,5],
    #[1,0,1],
    #[0,1],
    #[0,1,0],
    #[1,1],
    #[6,0,9],
    #[6,0,9,0,5],
    [0],
    [5],
    []
]
for input in inputs:
    print("input: "+str(input)+" output: "+str(Solution().trap(input)))
