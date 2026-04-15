class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for val in s:
            if val == '{' or val == '(' or val == '[':
                stack.append(val)
                continue
            elif len(stack) == 0:
                return False
            top_stak = stack.pop()
            if (top_stak == '{' and val != '}') or (top_stak == '(' and val != ')') or (top_stak == '[' and val != ']'):
                return False
        return len(stack) == 0

sol = Solution()
s = "{[]}"

boo = sol.isValid(s)
print(boo)



"""

See how similar is the best solution!!

Uses the list of values an the function "in"



class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        o_brackets = ['(', '[', '{']
        c_brackets = [')', ']', '}']
        for c in s:
            if c in o_brackets:
                stack.append(c)
            if c in c_brackets:
                if not stack:
                    return False
                last_bracket = stack.pop()
                if (
                    c == ')' and last_bracket != '(' or
                    c == '}' and last_bracket != '{' or
                    c == ']' and last_bracket != '['
                ):
                    return False
        return len(stack) == 0

"""