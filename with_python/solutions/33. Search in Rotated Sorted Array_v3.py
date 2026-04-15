class Solution:
    #def search(self, nums: List[int], target: int) -> int:
    def search(self, nums: list, target: int) -> int:
        left_index = 0
        right_index = len(nums) -1
        while left_index < right_index:
            mid_index = (left_index + right_index) // 2
            left_val = nums[left_index]
            right_val = nums[right_index]
            mid_val = nums[mid_index]
            if mid_val == target:
                return mid_index
            
            if mid_val <= left_val: # pivot is on left part:
                if mid_val < target and target <= right_val: # target is in range
                    left_index = mid_index + 1
                else: # target <= right_val
                    right_index = mid_index -1
            if left_val <= mid_val: # the pivot is not in this range:
                if left_val <= target and target < mid_val:
                    right_index = mid_index -1
                else:
                    left_index = mid_index + 1

        if nums[left_index] == target:
            return left_index
        return -1 

sol = Solution()
nums = [3,1]
target = 0
i = sol.search(nums,target)
print(i)



"""

Some change of sides:
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
    #def search(self, nums: list, target: int) -> int:
        left_index = 0
        right_index = len(nums) -1
        while left_index < right_index:
            mid_index = (left_index + right_index) // 2
            left_val = nums[left_index]
            right_val = nums[right_index]
            mid_val = nums[mid_index]
            if mid_val == target:
                return mid_index
            
            if mid_val <= left_val: # pivot is on left part:
                if target > mid_val and target <= right_val: # target is in range
                    left_index = mid_index + 1
                else: # target <= right_val
                    right_index = mid_index -1
            if left_val <= mid_val: # the pivot is not in this range:
                if target >= left_val and target < mid_val:
                    right_index = mid_index -1
                else:
                    left_index = mid_index + 1

        if nums[left_index] == target:
            return left_index
        return -1 


"""
This code got better score than last code!


Runtime: 36 ms, faster than 89.33% of Python3 online submissions for Search in Rotated Sorted Array.
Memory Usage: 14.8 MB, less than 22.57% of Python3 online submissions for Search in Rotated Sorted Array.

"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
    #def search(self, nums: list, target: int) -> int:
        left_index = 0
        right_index = len(nums) -1
        while left_index < right_index:
            mid_index = (left_index + right_index) // 2
            left_val = nums[left_index]
            right_val = nums[right_index]
            mid_val = nums[mid_index]
            if mid_val == target:
                return mid_index
            
            if mid_val <= left_val: # pivot is on left part:
                if target > mid_val and target <= right_val: # target is in range
                    left_index = mid_index + 1
                else: # target <= right_val
                    right_index = mid_index -1
            if mid_val >= left_val: # the pivot is not in this range:
                if target >= left_val and target < mid_val:
                    right_index = mid_index -1
                else:
                    left_index = mid_index + 1

        if nums[left_index] == target:
            return left_index
        return -1 