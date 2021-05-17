from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            j = nums[i] - 1
            while j < n and j >= 0:
                nums[j],nums[i] = nums[i], nums[j]
                j = nums[i] - 1
                if nums[i] == i + 1:
                    break
        for i in range(n):
            if i + 1 != nums[i]:
                return i + 1
        return n + 1
        
nums = [1,1] #breaks this!!
out = Solution().firstMissingPositive(nums)
print(out)


"""
God Demn it, the good solution is so similar to my solution! To the last solution - not this one.
Best time is like mine - attached:
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Replace all the non positive numbers with a special number n+1
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n+1
        
        # print(nums)
        # Try to put the elements in their correct locations. Put k in index k-1
        i = 0
        while i < n:
            j = nums[i] - 1
            if j < n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i+=1
        # print(nums)
        # Return the (index+1) where number is mismatching with its location
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        # If all the elements are placed at their correct locations, return n+1
        return n+1



This is average time... So similar to currect version.
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_set=set(nums)
        max_val=max(nums)
        
        if max_val<=0:
            return 1

        for i in range(1,max_val):
            if i not in nums_set:
                return i
        return max_val+1

"""