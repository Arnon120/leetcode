"""
Runtime: 88 ms, faster than 38.01% of Python3 online submissions for Search in Rotated Sorted Array.
Memory Usage: 14.8 MB, less than 22.57% of Python3 online submissions for Search in Rotated Sorted Array.

Out of range of graphs it was so bad!
The problem was the use of recusion.
Maybe you should not use recursion!
"""

class Solution:
    #def search(self, nums: List[int], target: int) -> int:
    def search(self, nums: list, target: int) -> int:
        #
        def search_in_sorted_part(nums: list, target: int):
            n = len(nums)
            if n == 0:
                return -1
            elif nums[n//2] == target:
                return n//2
            elif nums[n//2] > target:
                res = search_in_sorted_part(nums[0:n//2:], target)
                if res == -1:
                    return -1
                else:
                    return res
            else: #nums[n//2] < target:
                res = search_in_sorted_part(nums[(n//2)+1::],target)
                if res == -1:
                    return -1
                else:
                    return n//2 + 1 + res
        #
        def search_in_roteted_list(nums: list,target: int):
            n = len(nums)
            if n <3:
                for k in range(n):
                    if nums[k] == target:
                        return k
                return -1
            if nums[0] < nums[n//2]:
                if nums[0] <= target and target <= nums[n//2]:
                    res = search_in_sorted_part(nums[0:(n//2)+1:],target)
                    if res == -1:
                        return -1
                    else:
                        return res 
                else: # target < nums[0] or nums[n//2] < target
                    res = search_in_roteted_list(nums[(n//2) +1::1],target)
                    if res == -1:
                        return -1
                    else:
                        return n//2 + 1 + res 
            else:
                if nums[n//2 + 1] <= target and target <= nums[n-1]:
                    res = search_in_sorted_part(nums[(n//2) +1::1],target)
                    if res == -1:
                        return -1
                    else:
                        return n//2 + 1 + res
                else:
                    res = search_in_roteted_list(nums[0:(n//2)+1:],target)
                    if res == -1:
                        return -1
                    else:
                        return res
        return search_in_roteted_list(nums,target)

sol = Solution()
nums = [3]
target = 3
i = sol.search(nums,target)
print(i)