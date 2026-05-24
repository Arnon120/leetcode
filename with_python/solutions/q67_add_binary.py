class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # a_as_int = int(a, 2)
        # b_as_int = int(b, 2)
        # c_as_int = a_as_int + b_as_int
        # text = f"{c_as_int:b}"
        # return text
        return f"{int(a,2) + int(b,2):b}"
    
sol = Solution()

assert(sol.addBinary("1", "1") == "10")