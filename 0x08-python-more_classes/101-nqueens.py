import sys

def is_safe(board, row, col):
    for i in range(col):
        if board[i] == row or abs(board[i] - row) == abs(i - col):
            return False
    return True

def solve_n_queens(board, col, n):
    if col >= n:
        print([[i, board[i]] for i in range(n)])
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col):
            board[col] = i
            res = solve_n_queens(board, col + 1, n) or res
            board[col] = -1  # backtrack

    return res
