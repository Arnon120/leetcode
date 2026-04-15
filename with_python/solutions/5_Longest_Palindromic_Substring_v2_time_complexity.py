class Solution:
    def check_in_palindrome(self, s:str, dynamic_programing: list, i: int, j: int):
        if i == j or i + 1 == j or dynamic_programing[i+1][j-1] != 0:
            return s[i] == s[j]
        return False
            
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length == 0:
            return ""
        dynamic_programing = [[0 for i in s] for i in s]
        """
        for i in range(length):
            dynamic_programing[i][i] = 1
        """
        noted_i = 0
        noted_j = 0
        
        for d in range(length): 
            """Maybe this is enough to deal with length one subwords..."""
            for i in range(length):
                j = i + d
                if j >= length:
                    break
                if self.check_in_palindrome(s,dynamic_programing,i,j):
                    dynamic_programing[i][j] = j-i+1
                    if j-i > noted_i - noted_j:
                        noted_i = i
                        noted_j = j
        return s[noted_i:noted_j+1]


        

sol = Solution()
t = sol.longestPalindrome("qgecuralerljmghebsvkdxatotpbiqmxdyetorjhtmcxbgddcqwktfbpnrthsnctdmchbqqhmgtalwslepvrzsylxvlidzryqrvyoisfeqveqxivnslrtvegctcfdgfojjbohgqxxhltgaxqsfcuitjkyopbafjukbgyvkwddgbvznnvejxjlhgktoowpqlluabvhmoqnibhqlpmqgvhjdxthbhmrfrxlmxnhvhxsezehmvtxpdohjbgmnbvvemqhgaxpvytqyjrifubommzoeuqdidnmambohgegyfftsahhpoivetithnfuzppprkpovpymhqardzlohjwrfiyxcnqgdwslavpepmhopcqdabhmqsoqxjswitkwzkoefhfydeartdhreiyzgummxpbtmrxcogmtwjrhdejprotvhzebdvrbedsieznynuaxqcvuegtefvxltovozpqjqocqvnxkesbewmfeacmrmgehyvrfksbbctcmxnbqnlvogjjgzotghxdrpdzyyrdbpvgusyreehfkqxzcgdekjtahubwvcuiktwdczjxacwuqxrtbhjsoqmbqorihykbzcxlyteoourrhheveamoidfxqudkzrpfftcpropwjeymetuibsdatmbvlmjghexejvplaysxbguijitfvrlkgayprkljshhvlonydoxbcuvbwacyeuvzfqqzmanfioyrybcdhkvlizdagpskdcaloglhluokblzgsppcbj")
print(t)