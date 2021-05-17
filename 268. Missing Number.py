from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        x = n
        for i in range(n):
            x^=i^nums[i]
        return x
    def missingNumber2(self, nums: List[int]) -> int:
        n = len(nums)
        sum_list = 0
        for c in nums:
            sum_list += c
        sum_index = (n**2 + n)//2
        return sum_index-sum_list

nums = [9,2,4,8,3,5,7,0,1]
out = Solution().missingNumber2(nums)
print(out)