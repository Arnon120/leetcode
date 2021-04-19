"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        original_length = len(nums)
        offset = 0
        for i in range(original_length):
            if nums[i] != val:
                nums[i - offset] = nums[i]
            else: #nums[i] == val
                offset += 1
        return original_length - offset
"""

class Solution:
    def removeElement(self, nums, val: int) -> int:
        original_length = len(nums)
        offset = 0
        for i in range(original_length):
            if nums[i] != val:
                nums[i - offset] = nums[i]
            else: #nums[i] == val
                offset += 1
        return original_length - offset

sol = Solution()
nums = [3,2,2,3]
val = 2
new_len = sol.removeElement(nums,val)
print('newlen = '+str(new_len)+' new_nums = '+str(nums))