# In this implementation you remember too many things and for too long.
# 
# at the i'th iteration, you care not about the i-2'th iteration
# you don't care about the things at the ends.
# 
# 
# This obviesly cats things in half.
# 
# Or by about 4 times :) 
class Solution:
    # runtime_comp: O(m \times k)
    # mem_comp: O(m)
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        k = len(t)
        numDistinct_array = [None for _ in s]
        for i in range(k):
            cur = t[i]
            sum = 0
            if i == 0:
                for j in range(m):
                    if s[j] == cur:
                        numDistinct_array[j] = (i,1)
            else: # if i > 0:
                for j in range(m):
                    temp_sum = sum
                    if numDistinct_array[j] != None and numDistinct_array[j][0] == i-1:
                        sum += numDistinct_array[j][1]
                    if cur == s[j]:
                        numDistinct_array[j] = (i,temp_sum)
        # last iteration to count everything
        sum = 0
        for j in range(m):
            if numDistinct_array[j] != None and numDistinct_array[j][0] == k-1:
                sum += numDistinct_array[j][1]
        return sum
        
        
"""        

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(t)
        n = len(s)
        dp = [1] * (n+1)
        L = n - m
        for i in range(1, m+1):
            # at the i'th iteration it shows in the array the numDistinct of s[0:j] at the point j, for t[0:i].
            # it does not show the same thing for too many s[0:j] for j we will not care about...
            next_row = [0] * (n+1)
            for j in range(i, i+L+1):
                next_row[j] = next_row[j-1]
                if s[j-1] == t[i-1]:
                    next_row[j] += dp[j-1]
            dp = next_row

        return dp[n]

Is there a way to make 'i' start at 0?
maybe there is no logical need for that - as i corresponds to the length of the substring of t.

"""

inputs = [
    ("rabbbitx","rabbit"),
    ("a","a"),
    ("aa","a"),
    ("a","aa"),
    ("aa","aa"),
    ("babgbag","bag")
    ]
for input in inputs:
    s = input[0]
    t = input[1]
    sol = Solution().numDistinct(s,t)
    print(str(input) + " " + str(sol))



