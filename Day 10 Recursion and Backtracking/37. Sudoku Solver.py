def isSafe(row, col, board, value):
    n = len(board)

    for i in range(n):
        if board[row][i] == value:
            return False
        if board[i][col] == value:
            return False
        if board[3*(row//3) + (i//3)][3*(col//3) + (i%3)] == value:
            return False

    return True

def solve(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == '.':
                for val in range(1, 10):
                    val = str(val)
                    if isSafe(i, j, board, val):
                        board[i][j] = val
                        remainingBoardSolution = solve(board)
                        if remainingBoardSolution:
                            return True
                        else:
                            board[i][j] = '.'
                return False
    return True


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        solve(board)