from collections import Counter
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]
        #candidates.sort()
        candidates_count = Counter(candidates)
        dp[0].append([])
        for c,n in candidates_count.most_common():
            for j in range(1,n+1):
                appended = [c for _ in range(j)]
                added = c*j
                for i in range(added, target + 1):
                    for combo in dp[i-added]:
                        if len(combo) == 0 or combo[-1] != c:
                            dp[i].append(combo + appended)
        return dp[target]


candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
target = 10
output = Solution().combinationSum2(candidates,target)
print(output)
