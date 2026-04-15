class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.split(' ')
        num_of_words = len(l)
        if num_of_words == 0:
            return 0
        for word in l[::-1]:
            len_word = len(word)
            if len_word > 0:
                return len_word
        return 0



"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])
"""