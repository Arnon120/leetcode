class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_as_string = str(x)
        string_len = len(x_as_string) // 2
        # first_half = x_as_string[:string_len]
        # second_half = x_as_string[-1:-string_len-1:-1]
        return x_as_string[:string_len] == x_as_string[-1:-string_len-1:-1]

    # def isPalindrome(self, x: int) -> bool:
    #     """
    #     First, by hand solution.
    #     """
    #     if x < 0:
    #         return False
        
    #     most_segnificat_digit = 1
    #     while most_segnificat_digit <= x:
    #         most_segnificat_digit *=10
    #     most_segnificat_digit //= 10

    #     while most_segnificat_digit > 1:
    #         if x // most_segnificat_digit != x % 10:
    #             return False
            
    #         x = (x % most_segnificat_digit) // 10
    #         most_segnificat_digit //= 100
        
    #     return True
    
sol = Solution()
tested_values = [
    (0, True), 
    (1, True),
    (9, True),
    (10, False), 
    (11, True), 
    (121, True), 
    (122, False),
    (-121, False)
]
for x, expected in tested_values:
    result = sol.isPalindrome(x)
    assert expected==result, f"tested value is {x}"

print("Got to end of test")
