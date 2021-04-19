class Solution:
    Num_to_Letters = {
        '2' : ['a','b','c'],
        '3' : ['d','e','f'],
        '4' : ['g','h','i'],
        '5' : ['j','k','l'],
        '6' : ['m','n','o'],
        '7' : ['p','q','r','s'],
        '8' : ['t','u','v'],
        '9' : ['w','x','y','z']
    }
    def letterCombinations(self, digits: str):
        if len(digits) == 0:
            return []
        l = [""]
        for digit in digits:
            new_l = []
            for preffix in l:
                for letter in self.Num_to_Letters[digit]:
                    new_l.append(preffix + letter)
            l = new_l
        return l


"""
sol = Solution()
digits = "23"
t = sol.letterCombinations(digits)
print(t)
"""