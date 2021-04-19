from collections import defaultdict


class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        if len(nums) <= 3 and sum(nums) != 0:
            return []
        
        counter = defaultdict(int)
        for v in nums:
            counter[v] += 1
        
        uni_nums = sorted(counter.keys())
        
        best = nums[0]+nums[1]+nums[2]
        
        for i in range(len(uni_nums)):
            a = uni_nums[i]
            if a * 3 == 0 and counter[a] >=3:
                res.append([a,a,a])
            for j in range(i+1, len(uni_nums)):
                b = uni_nums[j]
                if 2*b+a==0 and counter[b]>1:
                    res.append([a,b,b])
                if 2*a+b==0 and counter[a]>1:
                    res.append([a,a,b])
                c=0-a-b
                if c>b and counter[c]>0:
                    res.append([a,b,c])
                
        return res

"""
sol = Solution()
nums = [-1,2,1,-4]
target = 1
best = sol.threeSumClosest(nums,target)
print(best)

"""