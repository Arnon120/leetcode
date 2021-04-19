class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        base = strs[0]
        s = ""
        for i in range(len(base)):
            for val in strs[1::]:
                if i == len(val):
                    return s
                else:
                    if val[i] != base[i]:
                        return s
            s = s + base[i]
        return s