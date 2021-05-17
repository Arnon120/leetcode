from typing import List
import itertools

""" 
This and the next one are cheating....
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return itertools.permutations(nums,len(nums))