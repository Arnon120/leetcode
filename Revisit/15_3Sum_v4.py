class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        l = list()
        for i in range(len(nums)):
            if i != 0:
                if nums[i] == nums[i-1]:
                    continue
            j = i+1
            k = len(nums) -1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    l.append([nums[i], nums[j], nums[k]])
                    start = nums[j]
                    while j < len(nums) and start == nums[j]:
                        j += 1
                    start = nums[k]
                    while k > -1 and start == nums[k]:
                        k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    start = nums[j]
                    while j < len(nums) and start == nums[j]:
                        j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    start = nums[k]
                    while k > -1 and start == nums[k]:
                        k -= 1
        return l

Sol = Solution()
nums = [0,0,0]

print(Sol.threeSum(nums))
