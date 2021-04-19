"""
The hint is binary search

"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2**31 - 1
        
        if dividend > 0:
            dividend = 0 - dividend
            if divisor == - 2147483648:
                return 0
            divisor = 0 - divisor
        is_divisor_negatrive = True 
        if divisor > 0:
            is_divisor_negatrive = False
            divisor = 0 - divisor
        l = []
        i = 0
        accumulated = divisor
        while accumulated >= dividend:
            l.append(accumulated)
            accumulated = accumulated + accumulated
            i += 1
        accumulated = 0
        accumulated_quotient = 0
        j = i-1
        while j >=0:
            if accumulated + l[j] >= dividend:
                accumulated_quotient += 2**j
                accumulated += l[j]
                if accumulated == dividend:
                    break 
            j -= 1
        if is_divisor_negatrive:
            return accumulated_quotient
        else:
            return 0 - accumulated_quotient

sol = Solution()
dividend = -2147483648
divisor = -1
quotient = sol.divide(dividend,divisor)
print(quotient)



"""

using bitwise operatons instead of 2**.




class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # MAX and MIN values for integer
        MAX = 2147483647
        MIN = -2147483648
        # Check for overflow
        if divisor == 0 or (dividend == MIN and divisor == -1):
            return MAX
        # Sign of result`
        sign = -1 if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0) else 1
        # Quotient
        quotient = 0
        # Take the absolute value
        absoluteDividend = abs(dividend)
        absoluteDivisor = abs(divisor)
        # Loop until the  dividend is greater than divisor
        while absoluteDividend >= absoluteDivisor:
            # This represents the number of bits shifted or
            # how many times we can double the number
            shift = 0
            while absoluteDividend >= (absoluteDivisor << shift):
                shift += 1
            # Add the number of times we shifted to the quotient
            quotient += (1 << (shift - 1))
            # Update the dividend for the next iteration
            absoluteDividend -= absoluteDivisor << (shift - 1)
        return -quotient if sign == -1 else quotient
        

"""