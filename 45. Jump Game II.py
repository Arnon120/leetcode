from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        reachability = list(range(n))
        for i in range(n):
            k = min(nums[i]+1,n-i)
            for j in range(1,k):
                reachability[i+j] = min(1 + reachability[i],reachability[i+j])
        return reachability[-1]

nums = [2,3,0,1,4] #breaks this!!
out = Solution().jump(nums)
print(out)



"""
Interesting implemantation for setting multiple values to the array if they are the same...

class Solution:
    def jump(self, nums: List[int]) -> int:
        l=len(nums)
        if l==1: return 0
        dp = [0] * l
        f = 0
        for i, n in enumerate(nums):
            if i+n > f:
                dp[f + 1:i + n + 1] = [dp[i] + 1] * (i + n - f)
                f = i + n
                if i+n >=l-1: break
        return dp[-1]


"""