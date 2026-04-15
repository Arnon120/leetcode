class Solution:
    def plusOne(self, digits):
        for i in range(len(digits))[::-1]:
            digits[i] += 1
            if digits[i] != 10:
                break
            else:    
                digits[i] = 0
                if i ==0:
                    digits = [0].extend(digits)
        return digits