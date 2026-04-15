class Solution:
    #def isValidSudoku(self, board: List[List[str]]) -> bool:
    def isValidSudoku(self, board) -> bool:
        def isValidUnit(unitnum: int, board, unittype: str) -> bool:
            Seen_entries = set({})
            for i in range(9):
                if unittype == 'Row':
                    val = board[i][unitnum]
                elif unittype == 'Col':
                    val = board[unitnum][i]
                else: # unittype == 'Cell':
                    val = board[3*(unitnum//3) + (i // 3)][3*(unitnum % 3) + (i % 3)]
                
                if val not in Seen_entries:
                    Seen_entries.add(val)
                elif val =='.':
                    continue
                else:
                    return False
            return True
        for i in range(9):
            if not (isValidUnit(i,board,'Row') and isValidUnit(i,board,'Col') and isValidUnit(i,board,'Cell')):
                return False
        return True

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
bol = Solution().isValidSudoku(board)
print (bol)


"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rec_set = set()
        
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j]!='.':
                    cur = board[i][j]
                    if (i,cur) in rec_set or (cur,j) in rec_set or (i//3,j//3,cur) in rec_set:
                        return False
                    
                    rec_set.add((i,cur))
                    rec_set.add((cur,j))
                    rec_set.add((i//3,j//3,cur))
                    
        return True
"""