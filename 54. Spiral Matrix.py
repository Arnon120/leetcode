from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        """
        if m == 0:
            return []
        """
        n = len(matrix[0])
        """
        if n == 0:
            return []
        """
        K = n*m
        output = [0]*K
        
        k = 0
        left = -1
        right = n 
        up = 0
        down = m 
        i = 0
        j = 0
        if n == 1:
            dirction = 'down'
        else:
            dirction = 'right'
        while left <= right and up <= down and k < K:
            output[k] = matrix[j][i]
            k+= 1
            if dirction == 'right':
                i += 1
                if i + 1== right:
                    dirction = 'down'
                    right -= 1
            elif dirction == 'down':
                j += 1
                if j + 1 == down:
                    dirction = 'left'
                    down -= 1
            elif dirction == 'left':
                i -= 1
                if i -1 == left:
                    dirction = 'up'
                    left += 1
            elif dirction == 'up':
                j -= 1
                if j - 1 == up:
                    dirction = 'right'
                    up += 1
        return output
        
matrices = [
    #[[1,2,3],[4,5,6],[7,8,9]],
    #[[1,2,3,4],[5,6,7,8],[9,10,11,12]],
    #[[1]]
    #[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]],
    #[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]],
    #[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25],[26,27,28,29,30]],
    #[[1,2,3,4]],
    [[1],[2],[3],[4]]
]
for matrix in matrices:
    print(matrix)
    print(Solution().spiralOrder(matrix))