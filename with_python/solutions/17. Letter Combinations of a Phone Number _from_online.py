import itertools

class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []
        map_ = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = list(itertools.product(*[list(map_[i]) for i in digits]))
        res = [''.join(obj) for obj in res]
        
        return res

sol = Solution()
digits = "23"
t = sol.letterCombinations(digits)
print(t)