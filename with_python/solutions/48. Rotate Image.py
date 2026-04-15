from typing import List


# The follwing line explains why this is stright wrong answer.
# This is worst time than transpose then switch rows, as this is switching rows is very very cheap - comparing to how mach change you gain.
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # if n is even, m = k,
        # else, k = m+1
        m = n // 2
        k = (n+1) // 2 
        for i in range(m):
            for j in range(k):
                #i_1 , j_1 = i , j
                #i_2 , j_2 = j_1 , n - i_1 -1 # = j, n - i - 1 = j, -i
                #i_3, j_3 = j_2, n - i_2 - 1 # = -i, -j
                #i_4, j_4 = j_3, n - i_3 - 1 # = -j, i
                # matrix[i_1][j_1], matrix[i_2][j_2], matrix[i_3][j_3], matrix[i_4][j_4] = matrix[i_4][j_4], matrix[i_1][j_1], matrix[i_2][j_2], matrix[i_3][j_3]
                #print("for i = "+str(i)+" and j="+str(j)+":")
                #print (str(matrix[i_1][j_1])+" = ? = "+ str(matrix[i][j]))
                #print (str(matrix[i_2][j_2])+" = ? = "+ str(matrix[j][-i-1]))
                #print (str(matrix[i_3][j_3])+" = ? = "+ str(matrix[-i-1][-j-1]))
                #print (str(matrix[i_4][j_4])+" = ? = "+ str(matrix[-j-1][i]))

                matrix[i][j], matrix[j][-i-1], matrix[-i-1][-j-1], matrix[-j-1][i] = matrix[-j-1][i], matrix[i][j], matrix[j][-i-1], matrix[-i-1][-j-1]

        return


matrices = [
    [[1,2,3],[4,5,6],[7,8,9]], 
    [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]],
    [[1]],
    [[1,2],[3,4]]
]

for matrix in matrices:
    print(matrix)
    Solution().rotate(matrix)
    print("roteated"+str(matrix))
