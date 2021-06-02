from typing import List

#recursion is a bad time. And adding the same element to all elemnts is also a bad time...
class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 1:
            return [0,1]
        lower_lvl = self.grayCode(n-1)
        po = 2**(n-1)
        return lower_lvl + ([po + x for x in lower_lvl[::-1]])

for n in range(1,5):
    print(Solution().grayCode(n))


"""
Best time had the same idea.
class Solution:
    def grayCode(self, n: int) -> List[int]:
        i, N, gray = 1, 2**n, [0]
        while i < N:
            gray.extend(i + item for item in gray[::-1])
            i *= 2

        return gray

"""