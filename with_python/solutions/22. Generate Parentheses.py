class Solution:
    def generate_Parenthesis_substring(self, pairs: int, opened: int):
        if pairs == 0 and opened == 0:
            return [""]
        if opened > 0:
            l_1 = [")" + val for val in self.generate_Parenthesis_substring(pairs , opened - 1)]
        else:
            l_1 = []
        if pairs > 0:
            l_2 = ["(" + val for val in self.generate_Parenthesis_substring(pairs - 1 , opened + 1)]
        else:
            l_2 = []
        return l_2 + l_1
    def generateParenthesis(self, n: int):
        if n == 0:
            return []
        else:
            return self.generate_Parenthesis_substring(n, 0)


"""
sol = Solution()
n = 3
l = sol.generateParenthesis(n)
print(l)
"""

"""

Also uses recursion but!
the append is alot simpler: pre + ')'


recusion is left to right - not right to left...
uses the "pre" in a smart way.

less cases?

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(left, right, pre):
            if left == right == 0:
                res.append(pre)

            # the situation left larger than right is impossible to construct 
            if left > right:
                return 
            
            # only able to add ")"
            if left < right:
                dfs(left, right - 1, pre + ')')
            
            if left != 0:
                dfs(left - 1, right, pre + '(')
        dfs(n, n, '')
        return res

"""