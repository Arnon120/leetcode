import itertools
class Solution:
    def isValidSudoku(self, board) -> bool:
        rec_set = set()
        
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j]!='.' and len(board[i][j]) < 2:
                    cur = board[i][j]
                    if (i,cur) in rec_set or (cur,j) in rec_set or (i//3,j//3,cur) in rec_set:
                        return False
                    
                    rec_set.add((i,cur))
                    rec_set.add((cur,j))
                    rec_set.add((i//3,j//3,cur))
                    
        return True
    
    #def solveSudoku(self, board: List[List[str]]) -> None:
    def solveSudoku(self, board) -> None:
        rec_set = set()
        # init rec_set
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j]!='.':
                    cur = board[i][j]
                    #if (i,cur) in rec_set or (cur,j) in rec_set or (i//3,j//3,cur) in rec_set:
                    #    return False
                    rec_set.add((i,cur))
                    rec_set.add((cur,j))
                    rec_set.add((i//3,j//3,cur))
        queue = list()
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j] == '.':
                    board[i][j] = '123456789'
                    for cur in '123456789':
                        if (i,cur) in rec_set or (cur,j) in rec_set or (i//3, j//3, cur) in rec_set:
                            board[i][j] = board[i][j].replace(cur,'')
                    if len(board[i][j]) == 1:
                        cur = board[i][j]
                        queue.append((i,j))
                        # seems like we don't use this...
                        rec_set.add((i,cur))
                        rec_set.add((cur,j))
                        rec_set.add((i//3,j//3,cur))
        def look_for_missing_num(unit_type: str, k: int) -> bool:
            d = dict({})
            was_resolt = False
            for i in range(9):
                if unit_type == 'Row':
                    val = board[k][i]
                elif unit_type == 'Col':
                    val = board[i][k]
                else: # unit_type == 'Cell':
                    val = board[3*(k // 3) + (i//3)][3*(k % 3) + (i % 3)]
                if len(val) > 1:
                    for cur in val:
                        if cur not in d.keys():
                            d[cur] = [i]
                        else:
                            d[cur].append(i)
            for key, value in d.items():
                if len(value) == 1:
                    was_resolt = True
                    if unit_type == 'Row':
                        row_num = k
                        col_num = value[0]
                    elif unit_type == 'Col':
                        row_num = value[0]
                        col_num = k
                    else: # unit_type == 'Cell':
                        row_num = 3*(k // 3) + value[0] // 3
                        col_num = 3*(k % 3) + value[0] % 3
                    board[row_num][col_num] = key
                    queue.append((row_num,col_num))
                    rec_set.add((row_num,key))
                    rec_set.add((key,col_num))
                    rec_set.add((row_num//3,col_num//3,key))
            return was_resolt

        while len(rec_set) < 3 * 9 * 9 - 1:
            while len(queue) > 0 and len(rec_set) < 3 * 9 * 9 - 1:
                tup = queue.pop()
                i = tup[0]
                j = tup[1]
                cur = board[i][j]
                for k in range(0,9):
                    vals = board[i][k]
                    if len(vals) != 1:
                        vals = vals.replace(cur,'')
                        board[i][k] = vals
                        #if not self.isValidSudoku(board):
                        #    print(tup)
                        if len(vals) == 1:
                            queue.append((i,k))
                            rec_set.add((i,vals))
                            rec_set.add((vals,k))
                            rec_set.add((i//3,k//3,vals))
                    vals = board[k][j]
                    if len(vals) != 1:
                        vals = vals.replace(cur,'')
                        board[k][j] = vals
                        #if not self.isValidSudoku(board):
                        #    print(tup)
                        if len(vals) == 1:
                            queue.append((k,j))
                            rec_set.add((k,vals))
                            rec_set.add((vals,j))
                            rec_set.add((k//3,j//3,vals))
                    vals = board[3*(i//3) + (k // 3) ][ 3*(j//3) + (k % 3)]

                    if len(vals) != 1:
                        vals = vals.replace(cur,'')
                        board[3*(i//3) + (k // 3) ][ 3*(j//3) + (k % 3)] = vals
                        #if not self.isValidSudoku(board):
                        #    print(tup)
                        if len(vals) == 1:
                            queue.append((3*(i//3) + (k // 3), 3*(j//3) + (k % 3)))
                            rec_set.add((3*(i//3) + (k // 3),vals))
                            rec_set.add((vals,3*(j//3) + (k % 3)))
                            rec_set.add((i,j,vals))
            #for i in range(9):
            #    for k in range(1,10):
            #        if not (i,str(k)) in rec_set:
            #            print(i,str(k))
            #        if not (i,str(k)) in rec_set:
            #            print(str(k),i)
            #        if not (i,str(k)) in rec_set:
            #            print(i // 3, i % 3, str(k))
            if len(rec_set) < 3 * 9 * 9 - 1:
                for tup in itertools.product(range(9),['Row','Col','Cell']):
                    k = tup[0]
                    unit_type = tup[1]
                    if look_for_missing_num(unit_type, k):
                        break
            if len(rec_set) < 3 * 9 * 9 - 1:
                #for i in range(9):
                #    for k in range(1,10):
                #        if not (i,str(k)) in rec_set:
                #            print(i,str(k))
                #        if not (i,str(k)) in rec_set:
                #            print(str(k),i)
                #        if not (i,str(k)) in rec_set:
                #            print(i // 3, i % 3, str(k))
                print( len(rec_set))
                print('cool stuff: need better algorithm.')
                for i in range(9):
                    pri = '|'
                    for j in range(9):
                        if len(board[i][j]) == 1:
                            pri += board[i][j] + '|'
                        else:
                            pri += '.' +'|'
                    print(pri)
                print('-------------------')
        
        
        
        for i in range(9):
            pri = '|'
            for j in range(9):
                if len(board[i][j]) == 1:
                    pri += board[i][j] + '|'
                else:
                    pri += '.' +'|'
            print(pri)
        for i in range(9):
            for k in range(1,10):
                if not (i,str(k)) in rec_set:
                    print(i,str(k))
                if not (i,str(k)) in rec_set:
                    print(str(k),i)
                if not (i,str(k)) in rec_set:
                    print(i // 3, i % 3, str(k))
            
        




board_0 = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
board_1 = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
board_2 = [[".",".",".","2",".",".",".","6","3"],["3",".",".",".",".","5","4",".","1"],[".",".","1",".",".","3","9","8","."],[".",".",".",".",".",".",".","9","."],[".",".",".","5","3","8",".",".","."],[".","3",".",".",".",".",".",".","."],[".","2","6","3",".",".","5",".","."],["5",".","3","7",".",".",".",".","8"],["4","7",".",".",".","1",".",".","."]]
boards = [board_0,board_1,board_2]
Solution().solveSudoku(boards[2])
"""
This prompts an error with the calculation.
"""

print(boards[2])    