class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        D = dict({})
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                D[nums[i]+nums[j]] = (i,j)
        best = nums[0]+nums[1]+nums[2]
        for k in range(len(nums)):
            num_3 = nums[k]
            for key,val in D.items():
                if abs(key + num_3 - target) < abs(best - target):
                    if k not in val:
                        best = key + num_3
                        if best == target:
                            return best
        return best

"""
sol = Solution()
nums = [-1,2,1,-4]
target = 1
best = sol.threeSumClosest(nums,target)
print(best)

"""