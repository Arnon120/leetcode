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

"""
Note the #1 solution is:
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        total = length * (length + 1) // 2
        return total - sum(nums)

    which is exactly the same code but uses better functions: 
    sum_index = total, (1 line <-> 1 line, but better implement)
    sum_list = sum(nums) (3 line <-> 0 line, using python inner code)

"""

nums = [9,2,4,8,3,5,7,0,1]
out = Solution().missingNumber2(nums)
print(out)