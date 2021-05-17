from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            j = nums[i] - 1
            while j < n and j >= 0 and j + 1 != nums[j]:
                k = nums[j] - 1
                nums[j] = j + 1
                j = k
        for i in range(n):
            if i + 1 != nums[i]:
                return i + 1
        return n + 1

nums = [7,8,9,11,12]
out = Solution().firstMissingPositive(nums)
print(out)