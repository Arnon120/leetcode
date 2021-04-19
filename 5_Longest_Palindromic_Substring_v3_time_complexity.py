class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length == 0:
            return ""
        dynamic_programing = [[0,1] for i in range(length)]
        noted_i = [None,0]

        Check_even = True
        Check_odd = True
        max_d = 1
        for d in range(length):
            """
            d stands for the length of the word we know of in the string at this point, starting at i
            """
            parity = d%2
            if parity == 0 and Check_even == False:
                continue
            if parity == 1 and Check_odd == False:
                continue
            something = False
            for i in range(1, length - d):
                if d == 0 or d == dynamic_programing[i][parity]:
                    if s[i-1] == s[i+d]:
                        dynamic_programing[i-1][parity] = d+2
                        noted_i[parity] = i-1
                        something = True
                        max_d = d+2
            if something == False:
                if parity == 0:
                    Check_even = False
                if parity == 1:
                    Check_odd = False
                if Check_even == False and Check_odd == False:
                    break
        return s[
            noted_i[max_d%2]:
            noted_i[max_d%2] + 
            dynamic_programing
                [noted_i[max_d%2]]
                [max_d%2] ]


        

sol = Solution()
t = sol.longestPalindrome("qgecuralerljmghebsvkdxatotpbiqmxdyetorjhtmcxbgddcqwktfbpnrthsnctdmchbqqhmgtalwslepvrzsylxvlidzryqrvyoisfeqveqxivnslrtvegctcfdgfojjbohgqxxhltgaxqsfcuitjkyopbafjukbgyvkwddgbvznnvejxjlhgktoowpqlluabvhmoqnibhqlpmqgvhjdxthbhmrfrxlmxnhvhxsezehmvtxpdohjbgmnbvvemqhgaxpvytqyjrifubommzoeuqdidnmambohgegyfftsahhpoivetithnfuzppprkpovpymhqardzlohjwrfiyxcnqgdwslavpepmhopcqdabhmqsoqxjswitkwzkoefhfydeartdhreiyzgummxpbtmrxcogmtwjrhdejprotvhzebdvrbedsieznynuaxqcvuegtefvxltovozpqjqocqvnxkesbewmfeacmrmgehyvrfksbbctcmxnbqnlvogjjgzotghxdrpdzyyrdbpvgusyreehfkqxzcgdekjtahubwvcuiktwdczjxacwuqxrtbhjsoqmbqorihykbzcxlyteoourrhheveamoidfxqudkzrpfftcpropwjeymetuibsdatmbvlmjghexejvplaysxbguijitfvrlkgayprkljshhvlonydoxbcuvbwacyeuvzfqqzmanfioyrybcdhkvlizdagpskdcaloglhluokblzgsppcbj")
"""
t = sol.longestPalindrome("ac")
"""
print(t)