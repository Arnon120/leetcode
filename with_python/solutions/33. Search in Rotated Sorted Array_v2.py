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
                if target < mid_val or right_val < target:
                    right_index = mid_index - 1
                else: # mid_val < target and target < mid_val
                    left_index = mid_index + 1
            else: # left_val < mid_val, pivot is on right or not in range
                if left_val <= target and target < mid_val:
                    right_index = mid_index -1
                else: # target < left_val or mid_val < target
                    left_index = mid_index +1

        if nums[left_index] == target:
            return left_index
        return -1 

sol = Solution()
nums = [1,3]
target = 1
i = sol.search(nums,target)
print(i)