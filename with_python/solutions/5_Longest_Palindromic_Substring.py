class Solution:
    def is_Palindromic(self,s: str) -> bool:
        return s == s[::-1]
    def longestPalindrome(self, s: str) -> str:
        for l in range(1,len(s)+1)[::-1] :
            for i in range(len(s)-l+1):
                t = s[i:i+l]
                if self.is_Palindromic(t):
                    return t

sol = Solution()
t = sol.longestPalindrome("ac")
print(t)


"""
Runtime: 7860 ms, faster than 15.57% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 14.3 MB, less than 82.84% of Python3 online submissions for Longest Palindromic Substring.
"""


"""
If replace each t with simply s[i:i+l]
Runtime: 7736 ms
Memory Usage: 14.1 MB
"""