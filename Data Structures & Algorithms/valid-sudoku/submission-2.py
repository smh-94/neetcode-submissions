class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #we use default dict because it handles missing keys by initializing them
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        #squares keys will be defined by (r//3,c//3)
        #we rely on integer division to figure out which square we're in on the sudoku puzzle


        for r in range(9):
            for c in range(9):
                #skip on empty squares, only checking if given nums are valid
                if board[r][c] == ".":
                    continue
                #check if current number exists in any of the 3 rules sets
                #return false if in there already
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares [(r//3,c//3)]:
                    return False
                #add to sets
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        #return true when complete
        return True


        #board=[
            # ["1","2",".",".","3",".",".",".","."],
            # ["4",".",".","5",".",".",".",".","."],
            # [".","9","1",".",".",".",".",".","3"],
            # ["5",".",".",".","6",".",".",".","4"],
            # [".",".",".","8",".","3",".",".","5"],
            # ["7",".",".",".","2",".",".",".","6"],
            # [".",".",".",".",".",".","2",".","."],
            # [".",".",".","4","1","9",".",".","8"],
            # [".",".",".",".","8",".",".","7","9"]]
            

