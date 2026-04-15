class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        H = {}
        start = 0 
        length = 0
        if len(s) == 0:
            return length
        for i in range(len(s)):
            if s[i] in H and start <= H[s[i]]:
                if length == 1:
                    start = i
                else:
                    start = H[s[i]]+1
                H[s[i]] = i
            else:
                H[s[i]] = i
                length = max(length, i - start + 1)
        return length

sol = Solution()

s = "aababcabcdbdecabc"
length = sol.lengthOfLongestSubstring(s)
print(length)
            