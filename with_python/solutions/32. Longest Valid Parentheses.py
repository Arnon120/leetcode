class Solution:
    def longestValidParentheses(self, s: str) -> int:
        counter_left_brackets = 0
        i = 0
        i_start = 0
        max_so_far = 0
        while i < len(s)-1:
            if s[i] == ')':
                i += 1
                continue
            else: # if s[i] == '(':
                if s[i+1] == '(':
                    i += 1
                    continue
                else: # if s[i] == ')':
                    i_start = i
                    max_so_far = max(max_so_far,2)
                    i = i+2
                    while i < len(s):
                        if s[i] == '(':
                            counter_left_brackets += 1
                            i += 1
                            continue
                        if s[i] == ')':
                            if counter_left_brackets > 0:
                                counter_left_brackets -=1
                                if counter_left_brackets == 0:
                                    max_so_far = max(max_so_far,i - i_start + 1)
                                i += 1
                                continue
                            else: # if counter_left_brackets == 0:
                                if i_start > 0:
                                    if s[i_start-1] == '(':
                                        i_start = i_start-1
                                        max_so_far = max(max_so_far,i - i_start + 1)
                                        i += 1
                                        continue
                                # else for boh levels
        return max_so_far



                

            

"""

    def longestValidParentheses_onlyone_side(self, s: str) -> int:
        i_start = 0
        i_end = i_start + 1
        max_length_string = 0
        while i_start < len(s) and i_end < len(s):
            if s[i_start] == '(' and s[i_end] == ')':
                max_length_string = max(max_length_string, i_end - i_start + 1)
                i_start -= 1
                if i_start < 0:
                    i_start = i_end +1
                    i_end = i_start + 1
                    continue
                i_end += 1
                if i_end >= len(s):
                    break
            else:
                i_start = i_end
                i_end = i_start + 1
                continue
        return max_length_string

"""

sol = Solution()
ss = ["(()","(()()(","()(()(())","()()","(())","(()))","","(",")()())"]
s = ss[2]
print("input: "+s+" output "+str(sol.longestValidParentheses(s)))
