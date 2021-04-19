class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        settolist = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k] == 0:
                        triplet = [nums[i],nums[j],nums[k]]
                        triplet.sort()
                        settolist.add(tuple(triplet))
        l = list(list(elem) for elem in settolist)
        return l


Sol = Solution()
nums = [-1,0,1,2,-1,-4]

print(Sol.threeSum(nums))