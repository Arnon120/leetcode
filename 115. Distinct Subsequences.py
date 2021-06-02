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

inputs = [
    ("rabbbit","rabbit"),
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
