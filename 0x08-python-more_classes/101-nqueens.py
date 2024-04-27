#!/usr/bin/python3
import sys


def print_board(board):
    print([[i, board[i]] for i in range(len(board))])

def is_safe(board, row, col):
    for i in range(col):
        if board[i] == row or abs(board[i] - row) == abs(i - col):
            return False
    return True

def solve_n_queens(board, col):
    if col == len(board):
        print_board(board)
        return True

    found_any = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[col] = i
            found_any = solve_n_queens(board, col + 1) or found_any
            board[col] = -1
    return found_any

def main():
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

    board = [-1] * n
    if not solve_n_queens(board, 0):
        print("No solution")

if __name__ == "__main__":
    main()
