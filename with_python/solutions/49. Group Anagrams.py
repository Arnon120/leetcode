from typing import List


"""
Remember python has very nice data structures.
You were thinking of a dictionary, but you implemented it as a list, used breaks and things...

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g = {}
        for s in strs:
            key = tuple(sorted(s))
            if key in g:
                g[key].append(s)
            else:
                g[key] = [s]
        return g.values()


"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        for s in strs:
            flag = False
            sSorted = sorted(s)
            for t in output:
                if sSorted == t[0]:
                    t.append(s)
                    flag = True
                    break
            if not flag:
                output.append([sSorted,s])
        return [l[1::] for l in output]

inputs = [
    ["eat","tea","tan","ate","nat","bat"],
    [""],
    ["a"]
]
for strs in inputs:
    print(strs)
    print(Solution().groupAnagrams(strs))