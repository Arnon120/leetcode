from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            j = nums[i]
            while j < n and j != nums[j]:
                k = nums[j]
                nums[j] = j
                j = k
        for i in range(n):
            if i != nums[i]:
                return i
        return n

nums = [3,0,1]
out = Solution().missingNumber(nums)
print(out)