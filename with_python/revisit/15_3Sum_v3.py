class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        l = list()
        hash_dict = {nums[i] : i for i in range(len(nums))}
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                target = -nums[i]-nums[j]
                if target in hash_dict:
                    if hash_dict[target] < i and hash_dict[target] < j:
                        taple = [nums[i],nums[j], target]
                        taple.sort()
                        l.append(taple)
        return l

                

Sol = Solution()
nums = [-1,0,1,2,-1,-4]

print(Sol.threeSum(nums))
