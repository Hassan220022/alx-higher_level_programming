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

def main(n):
    board = [-1] * n
    if not solve_n_queens(board, 0, n):
        print("No solution")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    main(n)
