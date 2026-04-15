import itertools
import copy
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
        def preform_obvious_moves(board):
            # init queue, dicts and board
            queue = []
            initialized_dict = dict(zip([str(i) for i in range(9)],[[i for i in range(9)] for i in range(9)]))
            # Row, Col, Cell  struct_num in {0,1,2}
            # k allways corresponds to number in struct 
            dicts = (copy.deepcopy(initialized_dict),
                    copy.deepcopy(initialized_dict), 
                    initialized_dict)
            def update_dicts(dicts,i,j,val):
                for struct_type in range(3):
                    if struct_type == 0:
                        struct_num = i
                        k = j
                    elif struct_type == 1:
                        struct_num = j
                        k = i
                    else: # struct_type == 2
                        struct_num = 3 * (i // 3) + (j // 3)
                        k = 3*(i % 3) + (j % 3)
                    # removes the consideration of the value board[i][j]
                    dicts[struct_type][struct_num].pop(val , None)
                    # for any other value it can not appear in location k
                    for val, lis in dicts[struct_type][struct_num].items():
                        lis.remove(k)
                        if len(lis) == 1:
                            """
                            Triger something!
                            """
                            print('Should trigger something!')
            for i in range(9):
                for j in range(9):
                    if len(board[i][j]) > 1:
                        continue
                    elif board[i][j] == '.':
                        board[i][j] = '123456789'
                    else:
                        queue.append((i,j,board[i][j]))
                        update_dicts(dicts,i,j,board[i][j])
                        # problem, we have yet to remove the elements form board.
            while len(queue) > 0:
                tup = queue.pop(0)
                i = tup[0]
                j = tup[1]
                val = tup[2]
                for k in range(9):
                    for struct in {'Row','Col','Cell'}:
                        if struct == 'Row':
                            row_num = i
                            col_num = k
                        elif struct == 'Col':
                            row_num = k
                            col_num = j
                        else: # stuct = 'Cell'
                            row_num = 3 * (i // 3) + (k // 3)
                            col_num = 3 * (j // 3) + (k % 3)
                        if len(board[row_num][col_num]) > 1:
                            board[row_num][col_num].replace(val,'')
                            new_val = board[row_num][col_num]
                            if len(new_val) == 1:
                                queue.append((row_num,col_num,new_val))
                                update_dicts(dicts,row_num,col_num,new_val,)
            print (board)
        preform_obvious_moves(board)
            
        




board_0 = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
board_1 = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
board_2 = [[".",".",".","2",".",".",".","6","3"],["3",".",".",".",".","5","4",".","1"],[".",".","1",".",".","3","9","8","."],[".",".",".",".",".",".",".","9","."],[".",".",".","5","3","8",".",".","."],[".","3",".",".",".",".",".",".","."],[".","2","6","3",".",".","5",".","."],["5",".","3","7",".",".",".",".","8"],["4","7",".",".",".","1",".",".","."]]
boards = [board_0,board_1,board_2]
Solution().solveSudoku(boards[0])
print(boards[0])    