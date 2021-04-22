import itertools

class Solution:
    #def isValidSudoku(self, board: List[List[str]]) -> bool:
    def isValidSudoku(self, board) -> bool:
        def isValidRow(rownum: int, board) -> bool:
            Seen_entries = set({})
            for i in range(9):
                val = board[i][rownum]
                if val not in Seen_entries:
                    Seen_entries.add(val)
                elif val =='.':
                    continue
                else:
                    return False
            return True
        def isValidCol(colnum: int, board) -> bool:
            Seen_entries = set({})
            for i in range(9):
                val = board[colnum][i]
                if val not in Seen_entries:
                    Seen_entries.add(val)
                elif val =='.':
                    continue
                else:
                    return False
            return True
        def isValidCell(rownum: int, colnum: int, board) -> bool:
            Seen_entries = set({})
            for i, j in itertools.product(range(3), range(3)):
                val = board[colnum+i][rownum+j]
                if val not in Seen_entries:
                    Seen_entries.add(val)
                elif val =='.':
                    continue
                else:
                    return False
            return True
        for i in range(9):
            if not (isValidRow(i,board) and isValidCol(i,board) and isValidCell(3*(i//3),3*(i%3),board)):
                return False
        return True

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
bol = Solution().isValidSudoku(board)
print (bol)